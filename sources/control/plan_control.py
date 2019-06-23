import init
import sources.model.fn as fn
import sources.model.html as html
import sources.model.error_handling as err_h
import sources.model.translate as t
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login
from note_plan_log.models import Plan

def process_post( request ):
    post       = False
    id         = -99
    date       = fn.get_now_plus()
    time_start = fn.get_now_hh_plus_1() + ':00'
    time_end   = fn.get_now_hh_plus_2() + ':00'
    title      = ''
    text       = ''
    link_act   = 1

    if request.method == 'POST':
        post = True

        date       = request.POST.get('date')
        time_start = request.POST.get('time_start')
        time_end   = request.POST.get('time_end')
        title      = request.POST.get('title')
        text       = request.POST.get('text')

        if request.POST.get('link_act'):
            link_act = request.POST.get('link_act')

        if request.POST.get('save_plan') == 'save_plan': # check if the save button is used
            plan = Plan()
            plan.date       = date
            plan.time_start = time_start
            plan.time_end   = time_end
            plan.title      = title
            plan.text       = text
            plan.user_id    = request.user.id
            plan.is_active  = 1
            plan.save()

            id = plan.id
        else:
            id = request.POST.get('id_plan')

            query = Q( user_id=request.user.id )
            query.add( Q(id=id), Q.AND )
            query.add( Q(is_active=1), Q.AND )

            plan = Plan.objects.all().get(query)

            if request.POST.get('update_plan') == 'update_plan': # check if the update button is used
                plan.date       = date
                plan.time_start = time_start
                plan.time_end   = time_end
                plan.title      = title
                plan.text       = text
                plan.save()

            elif request.POST.get('delete_plan') == 'delete_plan': # check if the register button is used
                plan.is_active = 0
                plan.save()
                # Reset form
                id         = 0
                date       = fn.get_now_plus()
                time_start = fn.get_now_hh_plus_1() + ':00'
                time_end   = fn.get_now_hh_plus_2() + ':00'
                title      = ''
                text       = ''

    # Update form data
    return {
        'id': id,
        'date': date,
        'time_start': time_start,
        'time_end': time_end,
        'title': title,
        'text': text,
        'link_act': link_act,
        'post': post
    }

def plan_write_page( request ):
    page = html.write_plan_page
    page.web_language = t.get_lang_act(request)

    form_data = process_post( request )

    return {
        'page': page,
        'form_data': form_data
    }

def plan_read_page( request ):
    page = html.read_plan_page
    page.web_language = t.get_lang_act(request)

    form_data = process_post( request )

    plans = []

    try:
        query = Q( user_id=request.user.id )
        query.add( Q(is_active=1), Q.AND ) # Show only active planning
        plans = Plan.objects.all().filter(query)
    except ObjectDoesNotExist:
        pass

    plans = plans[::-1] # Reverse plan order

    num = 1
    for plan in plans: # Update plans for html page
        plan.num        = num
        plan.date       = str(plan.date)
        plan.time_start = str(plan.time_start)[:5]
        plan.time_end   = str(plan.time_end)[:5]
        num += 1

    # Update page values
    page.rows_count = len(plans)
    page.max_per_page = init.web_max_logs_plans_per_page
    page.link_act = form_data['link_act']

    return {
        'page': page,
        'form_data': form_data,
        'plans': plans
    }
