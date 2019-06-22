# -*- coding: utf-8 -*-
'''Library made to translate text from English into one or more other languages'''

__author__     =  "Mark Zwaving"
__email__      =  "markzwaving@gmail.com"
__copyright__  =  "Copyright 2019 (C) Mark Zwaving. All rights reserved."
__license__    =  "GNU Lesser General Public License (LGPL)"
__version__    =  "0.3"
__maintainer__ =  "Mark Zwaving"
__status__     =  "Development"

import init
from django.contrib.auth.models import User
from note_plan_log.models import Settings

def get_lang_act(request):
    if request.user.is_authenticated:
        init.web_language = Settings.objects.get(
                                user_id=request.user.id
                                ).language

    return init.web_language

class Lang:
    def __init__(self, EN, NL):
        self.lang = init.web_language.upper()
        self.default = EN
        self.EN = EN
        self.NL = NL

    def search(self, s):
        if s == self.EN:
            return True
        elif s == self.NL:
            return True

        return False

    def get(self):
        if self.lang == 'EN':
            return self.EN
        elif self.lang == 'NL':
            return self.NL

        return self.default

translate_pool = [
    Lang('Good bye', 'Tot ziens'),
    Lang('Welcome', 'Welkom'),
    Lang('Adress', 'Adres'),
    Lang('Meer informatie', 'More information'),
    Lang('Write a log', 'Schrijf een log'),
    Lang('Read a log', 'Lees een log'),
    Lang('Write a plan', 'Schrijf een planning'),
    Lang('Read a plan', 'Lees een planning'),
    Lang('Language setting', 'Taalinstelling'),
    Lang('All Rights Reserved', 'Alle Rechten Voorbehouden'),
]

def tr(s):
    for l in translate_pool:
        oke = l.search(s)
        if oke:
            return l.get()

    return s
