# -*- coding: utf-8 -*-
'''Library contains classes for errorhandling with forms'''

__author__     =  "Mark Zwaving"
__email__      =  "markzwaving@gmail.com"
__copyright__  =  "Copyright 2019 (C) Mark Zwaving. All rights reserved."
__license__    =  "GNU Lesser General Public License (LGPL)"
__version__    =  "0.4"
__maintainer__ =  "Mark Zwaving"
__status__     =  "Development"

import re
import sources.model.fn as fn
from validate_email import validate_email
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Error():
    found = False
    text  = []
    def __init__(self, found, text):
        self.found = found
        self.text  = text

def check_string_base(err, s, e):
    if s in ['',None,False]:
        s = ''
        err.found = True
        err.text.append(f'{e} may not be empthy.'.capitalize())
    else:
        s = fn.clean_s(s) # Sanitize string
        if s in ['',None,False]:
            s = ''
            err.found = True
            err.text.append(f'{e} may not only contain whitespaces.'.capitalize())

    return s, err

def check_string(err, s, e):
    if s in ['',None,False]:
        s = ''
        err.found = True
        err.text.append(f'{e} may not be empthy.'.capitalize())
    else:
        s = fn.rm_s(fn.clean_s(s)) # Sanitize string
        if s in ['',None,False]:
            s = ''
            err.found = True
            err.text.append(f'{e} may not only contain whitespaces.'.capitalize())

    return s, err

def check_password(err, s, e):
    # Check sanity string
    s, err  = check_string(err, s, e)
    if err.found:
        return s, err

    min, max, l = 12, 30, len(s)
    # Check min length
    if l < min:
        err.found = True
        err.text.append(f'Password is too short. Minimum characters must be {min}.')

    # Check max length
    if l > max:
        err.found = True
        err.text.append(f'Password is too long. Maximum characters must be {max}.')

    return s, err

def check_both_passwords(err, s1, s2):
    if s1 != s2:
        err.found = True
        err.text.append(f'Both passwords are not the same.')

    return s2, err

def check_email(err, s, e):
    # Check sanity string
    s, err = check_string(err, s, e)
    if err.found:
        return s, err

    # Check email
    err = Error(False, [])
    min, max, l = 6, 254, len(s)

    # Check min length
    if l < min:
        err.found = True
        err.text.append('Emailadress is too short.')

    # Check max length
    if l > max:
        err.found = True
        err.text.append('Emailadress is too long. Maximum characters must be 254.')

    # Check for '@'
    if "@" not in s:
        err.found = True
        err.text.append("Emailadress must contain a '@' character.")

    # Check for '.'
    if "." not in s:
        err.found = True
        err.text.append("Emailadress must contain a '.' character.")

    # Check for failures
    if not err.found:
        reg = r"[^.@\s]{1,250}@[^@\s]{1,63}\.[^@\s]{2,63}"
        # reg = "^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$"
        if re.fullmatch(reg, s) == None:
            err.found = True
            err.text.append("Error in emailadress.")

    # Extra check for failures
    if not err.found:
        if not validate_email(s):
            err.found = True
            err.text.append("Error in emailadress.")

    return s, err

def is_email_taken(err, e1):
    try:
        mail  = User.objects.get( email=e1.lower() )
    except ObjectDoesNotExist:
        mail = None

    if mail != None:
        err.found = True
        err.text.append(f'Email already used.')

    return e1, err

def check_birthday(err, s, e):
    # Check sanity string
    s, err = check_string(err, s, e)
    if err.found:
        return s, err

    y, m, d = s.split('-')
    given_date     = datetime( int(y), int(m), int(d) )
    date_too_young = datetime.now()
    date_too_old   = datetime( 1900, 1, 1 )

    if given_date > date_too_young:
        err.found = True
        err.text.append("Birthdate cannot be in the future")

    if given_date < date_too_old:
        err.found = True
        err.text.append("Birthdate is too old")

    return s, err

def check_phone(err, s, e):
    # Check sanity string
    s, err = check_string(err, s, e)
    if err.found:
        return s, err

    reg = r"[\.\_\+\-\s0-9]{9,12}"
    if re.fullmatch(reg, s) == None:
        err.found = True
        err.text.append("Error in phonenumber.")

    return s, err

def check_function(err, sl, e):
    # Check sanity list
    if not sl:
        err.found = True
        err.text.append("Select at least one function")
        return sl, err

    for s in sl:
        if s not in ['S', 'P', 'T']:
            err.found = True
            err.text.append("Unknown {s} function selected")

    return sl, err

def check_gender(err, s, e):
    # Check sanity string
    if s in ['',None]:
        err.found = True
        err.text.append(f'Select a gender.')
    else:
        s = fn.rm_s(fn.clean_s(s)) # Sanitize string
        if s == '':
            err.found = True
            err.text.append(f'Select a gender.')

    if err.found:
        return s, err

    if not err.found:
        if s not in ['M', 'V', 'N']:
            err.found = True
            err.text.append("Gender unknown")

    return s, err
