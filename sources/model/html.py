# -*- coding: utf-8 -*-
'''Library contains a class for default values for a webpage'''

__author__     =  "Mark Zwaving"
__email__      =  "markzwaving@gmail.com"
__copyright__  =  "Copyright 2019 (C) Mark Zwaving. All rights reserved."
__license__    =  "GNU Lesser General Public License (LGPL)"
__version__    =  "0.4"
__maintainer__ =  "Mark Zwaving"
__status__     =  "Development"

import init
import sources.model.fn as fn
import sources.model.dates as dates
from   sources.model.translate import tr

class Page():
    '''Class stores page values for a html page'''
    head_title        = ''
    head_charset      = init.web_charset
    head_author       = init.web_author
    head_description  = ''
    head_robots       = init.web_robots
    head_viewport     = init.web_viewport
    body_title        = ''
    body_header       = ''
    body_description  = ''
    body_content      = ''
    body_footer       = ''
    footer_date_text  = fn.get_act_date_txt()
    footer_date_yyyy  = fn.get_act_yyyy()
    footer_adress     = init.web_adress
    footer_place      = init.web_place
    footer_email      = init.web_email
    footer_mobiel     = init.web_mobiel
    footer_all_rights = tr('All Rights Reserved')
    web_language      = init.web_language
    date_now          = fn.get_now()
    time_hh_s         = fn.get_now_hh()
    time_hh_e         = fn.get_now_hh_plus_1()
    input_required    = 'required'
    form_validate     = 'novalidate'
    NUM               =  1
    link_act          =  1

    def __init__(self):
        pass

home_page = Page()
home_page.head_title        =  'Welkom bij log en plan'
home_page.head_description  =  'Welkom op deze website'
home_page.head_robots       =  'follow, index'
home_page.body_title        =  ''
home_page.body_description  =  ''
home_page.body_content      =  ''

notes_page = Page()
notes_page.head_title        =  'Notities'
notes_page.head_description  =  'Maak hier uw eigen notities'
notes_page.head_robots       =  'follow, index'
notes_page.body_title        =  notes_page.head_title
notes_page.body_description  =  ''
notes_page.body_content      =  ''
notes_page.input_required    = 'required'
notes_page.form_validate     = 'validate'

write_log_page = Page()
write_log_page.head_title        =  'Log a day'
write_log_page.head_description  =  'Page for logging days'
write_log_page.head_robots       =  'follow, index'
write_log_page.body_title        =  'Schrijf'
write_log_page.body_description  =  ''
write_log_page.body_content      =  ''

read_log_page = Page()
read_log_page.head_title        =  'Read a log'
read_log_page.head_description  =  'Page for reading logs'
read_log_page.head_robots       =  'follow, index'
read_log_page.body_title        =  'Logs'
read_log_page.body_description  =  ''
read_log_page.body_content      =  ''

write_plan_page = Page()
write_plan_page.head_title        =  'Write a plan'
write_plan_page.head_description  =  'Page for writing plans'
write_plan_page.head_robots       =  'follow, index'
write_plan_page.body_title        =  'Schrijf'
write_plan_page.body_description  =  ''
write_plan_page.body_content      =  ''

read_plan_page = Page()
read_plan_page.head_title        =  'Read a plan'
read_plan_page.head_description  =  'Page for reading plans'
read_plan_page.head_robots       =  'follow, index'
read_plan_page.body_title        =  'Planning'
read_plan_page.body_description  =  ''
read_plan_page.body_content      =  ''

about_page = Page()
about_page.head_title        =  'Informatie'
about_page.head_description  =  'informatie over de website'
about_page.head_robots       =  'follow, index'
about_page.body_title        =  about_page.head_title
about_page.body_description  =  ''
about_page.body_content      =  ''

register_page = Page()
register_page.head_title        =  'Register'
register_page.head_description  =  'Page to register a new user'
register_page.head_robots       =  'follow, index'
register_page.body_title        =  register_page.head_title
register_page.body_description  =  register_page.head_description
register_page.body_content      =  ''

login_page = Page()
login_page.head_title        =  'Login'
login_page.head_description  =  'Page to login'
login_page.head_robots       =  'follow, index'
login_page.body_title        =  ''
login_page.body_description  =  ''
login_page.body_content      =  ''

logout_page = Page()
logout_page.head_title        =  'Logout'
logout_page.head_description  =  'Page to logout'
logout_page.head_robots       =  'follow, index'
logout_page.body_title        =  logout_page.head_title
logout_page.body_description  =  ''
logout_page.body_content      =  ''

lang_page = Page()
lang_page.head_title        =  'Languages'
lang_page.head_description  =  'Select a language'
lang_page.head_robots       =  'follow, index'
lang_page.body_title        =  lang_page.head_title
lang_page.body_description  =  ''
lang_page.body_content      =  ''

webpages = [ home_page, notes_page, write_log_page, read_log_page,
             write_plan_page, read_plan_page, about_page, register_page,
             login_page, logout_page, lang_page ]
