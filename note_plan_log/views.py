from django.shortcuts import render
from django.contrib.auth import logout
import sources.model.html as html
import sources.model.fn as fn
import sources.model.translate as t
from sources.control.language_control import language_page
from sources.control.login_control    import login_page
from sources.control.register_control import register_page
from sources.control.notes_control    import notes_page
from sources.control.log_control      import log_write_page, log_read_page
from sources.control.plan_control     import plan_write_page, plan_read_page

def home_view(request):
    page = html.home_page
    page.web_language = t.get_lang_act(request)
    content = {
        'page': page
    }
    return render(request, "home.html", content)

def write_plan_view(request):
    page = html.write_plan_page
    page.web_language = t.get_lang_act( request )
    page.time_hh_s = fn.get_now_hh_plus_1()
    page.time_hh_e = fn.get_now_hh_plus_2()

    return render( request,
                   "write-plan.html",
                   plan_write_page( request )
                   )

def write_log_view(request):
    page = html.write_log_page
    page.web_language = t.get_lang_act(request)

    return render( request,
                   "write-log.html",
                   log_write_page( request )
                   )

def read_log_view(request):
    page = html.read_log_page
    page.web_language = t.get_lang_act(request)
    return render( request,
                   "read-log.html",
                   log_read_page( request )
                   )

def read_plan_view(request):
    page = html.read_plan_page
    page.web_language = t.get_lang_act(request)

    return render( request,
                   "read-plan.html",
                   plan_read_page( request )
                   )

def about_view(request):
    page = html.about_page
    page.web_language = t.get_lang_act(request)
    content = {
        'page': page
    }
    return render(request, "about.html", content)

def logout_view(request):
    page = html.logout_page
    page.web_language = t.get_lang_act(request)

    logout(request)
    content = {
        'page': page
    }
    return render(request, "logout.html", content)

def login_view( request ):
    return render( request,
                   "login.html",
                   login_page(request)
                   )

def register_view(request):
    return render( request,
                   "register.html",
                   register_page(request)
                   )

def language_view(request):
    return render( request,
                   "language.html",
                   language_page(request)
                   )

def notes_view(request):
    return render( request,
                   "notes.html",
                   notes_page(request)
                   )
