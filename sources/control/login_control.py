import init
import sources.model.html as html
import sources.model.error_handling as err_h
import sources.model.translate as t
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login_page(request):
    page = html.login_page
    page.web_language = t.get_lang_act(request)

    post, succes, err = False, False, err_h.Error(False,[])
    form_data = {
        'email': '',
        'password': '',
        'err_email': err,
        'err_password': err,
        'email_class': '',
        'password_class': '',
    }

    if request.method == 'POST': # Check if something is posted
        if request.POST.get('login') == 'login': # check if the register button is used
            # Get post vars
            email    = request.POST.get('inputEmail')
            password = request.POST.get('inputPassword')
            # Error checking
            email, err_email = err_h.check_email(err_h.Error(False,[]), email, 'email')
            password, err_password = err_h.check_password(err_h.Error(False,[]), password, 'password')

            # Update form data
            form_data = {
                'email': email,
                'password': password,
                'err_email': err_email,
                'err_password': err_password,
                'email_class':    ' is-invalid' if err_email.found else    ' is-valid',
                'password_class': ' is-invalid' if err_password.found else ' is-valid',
            }

            # Check for errors
            if ( err_password.found or err_email.found ):
                succes = False
            else:
                succes = True
                username = User.objects.get(email=email.lower()).username
                user = authenticate( request, username=username, password=password )
                if user is not None:
                    login(request, user)
                else:
                    pass

    return {
        'page': page,
        'post': post,
        'succes': succes,
        'form_data': form_data
    }
