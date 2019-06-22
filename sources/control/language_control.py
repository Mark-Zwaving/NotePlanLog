import init
import sources.model.html as html
import sources.model.error_handling as err_h
import sources.model.translate as t
from note_plan_log.models import Settings

def language_page(request):
    page = html.lang_page
    if request.user.is_authenticated:
        if request.method == 'GET':
            lang = request.GET.get('lang')
            if lang.upper() in ['NL','EN']:
                init.web_language = lang.upper()
                # Update database
                set = Settings.objects.get(user_id_id=request.user.id)
                set.language = init.web_language
                set.save()

    page.web_language = t.get_lang_act(request)

    return {
        'page': page
    }
