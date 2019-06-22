import init
import sources.model.html as html
import sources.model.error_handling as err_h
import sources.model.translate as t
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from note_plan_log.models import Note

def notes_page(request):
    page = html.notes_page
    page.web_language = t.get_lang_act(request)
    post, succes, err, succes_text = False, False, err_h.Error(False,[]), ''

    form_data = {
        'title':      '',
        'err_title':  err,
        'text':       '',
        'date_set':   ''
    }

    if request.method == 'POST': # Check if something is posted
        post = True

        if request.POST.get('save_note') == 'save_note': # Check if the save note button is used

            title, err_title = err_h.check_string_base (
                                        err_h.Error(False,[]),
                                        request.POST.get('inputTitle'),
                                        'Title' )
            form_data = {
                'title':      title,
                'err_title':  err_title,
                'text':       request.POST.get('inputText'),
                'date_set':   request.POST.get('inputDateSet')
            }

            # Check for errors
            if ( err_title.found ):
                succes = False

            else:
                succes = True
                succes_text = 'Notitie succesvol toegevoegd'
                note = Note()
                note.title = form_data['title']
                note.text  = form_data['text']
                note.date  = form_data['date_set']
                note.user_id = request.user.id
                note.is_active = 1
                note.save() # Save in DB

        elif request.POST.get('delete_note') == 'delete_note':
            succes = True
            note_id = request.POST.get('note_id')

            query = Q( user_id=request.user.id )
            query.add( Q(id=note_id), Q.AND )
            query.add( Q(is_active=1), Q.AND )

            Note.objects.all().filter(query).update(is_active=0)

            succes_text = 'Notitie succesvol verwijderd'

    # Read all data from database
    query = Q( user_id=request.user.id )
    query.add( Q(is_active=1), Q.AND )

    notes = Note.objects.all().filter(query)
    notes = notes[::-1] # Reverse log order

    # Add nums id's for pagination
    num = 1
    for note in notes:
        note.num = num
        num += 1

    page.rows_count = len(notes)
    page.max_per_page = init.web_max_notes_per_page

    return {
        'page': page,
        'notes': notes,
        'succes': succes,
        'succes_txt': succes_text,
        'form_data': form_data
    }
