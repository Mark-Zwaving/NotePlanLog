import init
import sources.model.fn as fn
import sources.model.html as html
import sources.model.error_handling as err_h
import sources.model.translate as t
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login
from note_plan_log.models import Log

def process_post( request ):
    id          = -99
    date        = fn.get_now()
    time_start  = fn.get_now_hh() + ':00'
    time_end    = fn.get_now_hh_plus_1() + ':00'
    title       = ''
    text        = ''
    succes      = ''
    setback     = ''
    reflect     = ''
    link_act    = 1
    post        = False

    if request.method == 'POST':
        post = True

        date        = request.POST.get('date')
        time_start  = request.POST.get('time_start')
        time_end    = request.POST.get('time_end')
        title       = request.POST.get('title')
        text        = request.POST.get('text')
        succes      = request.POST.get('succes')
        setback     = request.POST.get('setback')
        reflect     = request.POST.get('reflect')

        if request.POST.get('link_act'):
            link_act = request.POST.get('link_act')

        if request.POST.get('save_log') == 'save_log': # check if the save button is used
            log = Log()
            log.date        =  date
            log.time_start  =  time_start
            log.time_end    =  time_end
            log.title       =  title
            log.text        =  text
            log.succes      =  succes
            log.setback     =  setback
            log.reflect     =  reflect
            log.user_id     =  request.user.id
            log.is_active   =  1
            log.save()

            id = log.id

        else:
            id = request.POST.get('id_log')

            query = Q( user_id=request.user.id )
            query.add( Q(id=id), Q.AND )
            query.add( Q(is_active=1), Q.AND )

            log = Log.objects.all().get(query)

            if request.POST.get('update_log') == 'update_log': # check if the update button is used
                log.date       =  date
                log.time_start =  time_start
                log.time_end   =  time_end
                log.title      =  title
                log.text       =  text
                log.succes     =  succes
                log.setback    =  setback
                log.reflect    =  reflect
                log.save()

            elif request.POST.get('delete_log') == 'delete_log': # check if the register button is used
                log.is_active = 0
                log.save()

                id          = -99
                date        = fn.get_now()
                time_start  = fn.get_now_hh() + ':00'
                time_end    = fn.get_now_hh_plus_1() + ':00'
                title       = ''
                text        = ''
                succes      = ''
                setback     = ''
                reflect     = ''
                post        = False


    # Update form data
    return {
        'id':         id,
        'date':       date,
        'time_start': time_start,
        'time_end':   time_end,
        'title':      title,
        'text':       text,
        'succes':     succes,
        'setback':    setback,
        'reflect':    reflect,
        'link_act':   link_act,
        'post':       post
    }

def log_write_page( request ):
    page = html.write_log_page
    page.web_language = t.get_lang_act(request)

    form_data = process_post( request )

    return {
        'page': page,
        'form_data': form_data
    }

def log_read_page( request ):
    page = html.read_log_page
    page.web_language = t.get_lang_act(request)

    form_data = process_post( request )

    logs = []

    try:
        # Show only active logs
        query = Q(user_id=request.user.id)
        query.add(Q(is_active=1), Q.AND)

        logs = Log.objects.all().filter(query)

    except ObjectDoesNotExist:
        pass

    logs = logs[::-1] # Reverse log order

    num = 1
    for log in logs: # Update logs for html page
        log.num        = num
        log.date = str(log.date)
        log.time_start = str(log.time_start)[:5]
        log.time_end   = str(log.time_end)[:5]
        num += 1

    # Update page values
    page.rows_count = len(logs)
    page.max_per_page = init.web_max_logs_plans_per_page
    page.link_act = form_data['link_act']

    return {
        'page': page,
        'form_data': form_data,
        'logs': logs
    }
