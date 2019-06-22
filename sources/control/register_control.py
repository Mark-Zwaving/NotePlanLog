import init
import sources.model.fn as fn
import sources.model.html as html
import sources.model.error_handling as err_h
import sources.model.translate as t
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from note_plan_log.models import Settings

def register_page( request ):
    page = html.register_page
    post, succes, err = False, False, err_h.Error(False,[])
    form_data = {
        'fname': '',
        'lname': '',
        'email': '',
        'phone': '',
        'password1': '',
        'password2': '',
        'birthday': '',
        'function': [],
        'gender': '',
        'err_fname': err,
        'err_lname': err,
        'err_email': err,
        'err_phone': err,
        'err_password1': err,
        'err_password2': err,
        'err_birthday': err,
        'err_function': err,
        'err_gender': err,
        'fname_class': '',
        'lname_class': '',
        'email_class': '',
        'phone_class': '',
        'password1_class': '',
        'password2_class': '',
        'birthday_class': '',
        'function_class': '',
        'gender_class': '',
    }

    if request.method == 'POST': # Check if something is posted
        if request.POST.get('register') == 'register': # check if the register button is used
            post = True

            fname = request.POST.get('inputFirstName')
            lname = request.POST.get('inputLastName')
            email = request.POST.get('inputEmail')
            phone = request.POST.get('inputPhone')
            password1  = request.POST.get('inputPassword1')
            password2  = request.POST.get('inputPassword2')
            birthday   = request.POST.get('inputBirthday')
            function_l = request.POST.getlist('checkInputFunction')
            gender     = request.POST.get('radioInputGender')

            fname, err_fname = err_h.check_string(err_h.Error(False,[]), fname, 'firstname')
            lname, err_lname = err_h.check_string(err_h.Error(False,[]), lname, 'lastname')
            email, err_email = err_h.check_email(err_h.Error(False,[]), email, 'email')
            phone, err_phone = err_h.check_phone(err_h.Error(False,[]), phone, 'phone')
            password1, err_password1 = err_h.check_password(err_h.Error(False,[]), password1, 'password')
            password2, err_password2 = err_h.check_password(err_h.Error(False,[]), password2, 'password repeat')
            birthday, err_birthday   = err_h.check_birthday(err_h.Error(False,[]), birthday, 'birthday')
            function_l, err_function = err_h.check_function(err_h.Error(False,[]), function_l, 'function')
            gender, err_gender       = err_h.check_gender(err_h.Error(False,[]), gender, 'gender')

            if not err_password1.found or not err_password2.found:
                	password2, err_password2 = err_h.check_both_passwords(err_password2, password1, password2)

            # Check email in databases
            if not err_email.found:
                email, err_email = err_h.is_email_taken(err_email, email)

            # Update form data
            form_data = {
                'fname': fname,
                'lname': lname,
                'email': email,
                'phone': phone,
                'password1': password1,
                'password2': password2,
                'birthday': birthday,
                'function': fn.join_list(function_l,','),
                'gender': gender,
                'err_fname': err_fname,
                'err_lname': err_lname,
                'err_email': err_email,
                'err_phone': err_phone,
                'err_password1': err_password1,
                'err_password2': err_password2,
                'err_function': err_function,
                'err_birthday': err_birthday,
                'err_gender': err_gender,
                'fname_class': ' is-invalid' if err_fname.found else ' is-valid',
                'lname_class': ' is-invalid' if err_lname.found else ' is-valid',
                'email_class': ' is-invalid' if err_email.found else ' is-valid',
                'phone_class': ' is-invalid' if err_phone.found else ' is-valid',
                'password1_class': ' is-invalid' if err_password1.found else ' is-valid',
                'password2_class': ' is-invalid' if err_password2.found else ' is-valid',
                'birthday_class': ' is-invalid' if err_birthday.found else ' is-valid',
                'function_class': ' is-invalid' if err_function.found else ' is-valid',
                'gender_class': ' is-invalid' if err_gender.found else ' is-valid',
            }

            # Check for errors
            if ( err_fname.found     or err_lname.found     or
                 err_password1.found or err_password2.found or
                 err_email.found     or err_phone.found     or
                 err_birthday.found  or err_function.found  or
                 err_gender.found ):
                 succes = False
            else:
                succes = True
                # Save data in databases
                user = User.objects.create_user( form_data['fname'],
                                     form_data['email'],
                                     form_data['password1']
                                     )
                user.last_name    = form_data['lname']
                user.is_superuser = 0
                user.is_active    = 1
                user.webuser.birthdate = form_data['birthday']
                user.webuser.function  = form_data['function']
                user.webuser.gender    = form_data['gender']
                user.webuser.phone     = form_data['phone']
                user.save()

                username = User.objects.get(email=email.lower()).username
                user = authenticate( request, username=username, password=password1 )
                if user is not None:
                    login(request, user)
                    sets = Settings( language="EN", user_id=request.user.id )
                    sets.save()

        else:
            print("Ja, er is gepost maar niet op de button geklikt !")

    else:
        print("Er is niks gepost !")

    return {
        'page': page,
        'post': post,
        'succes': succes,
        'form_data': form_data
    }
