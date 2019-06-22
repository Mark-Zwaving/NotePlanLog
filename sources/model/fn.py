# -*- coding: utf-8 -*-
'''Library contains casual functions for different purposes'''

__author__     =  "Mark Zwaving"
__email__      =  "markzwaving@gmail.com"
__copyright__  =  "Copyright 2019 (C) Mark Zwaving. All rights reserved."
__license__    =  "GNU Lesser General Public License (LGPL)"
__version__    =  "0.9.1"
__maintainer__ =  "Mark Zwaving"
__status__     =  "Development"

import os, sys
import sources.model.dates as dates
from datetime import datetime, timedelta

# Some quick,short functions
s_add        = lambda s,a:      f'{s}{a}'
add_s        = lambda a,s:      f'{a}{s}'
add_s_add    = lambda a1,s,a2:  s_add(add_s(a1,s),a2)
s_nl         = lambda s:        s_add(s,c.ln)
ln_s_ln      = lambda s:        add_s_add(c.ln,s,c.ln)
mk_path      = lambda dir,add:  os.path.abspath(os.path.join(dir,add))
rm_s_from_s  = lambda rs,s:     replace_s_by_s(rs,'',s)
rm_tab       = lambda s:        rm_s_from_s('\t',s)
rm_ln        = lambda s:        rm_s_from_s('\n',s)
rm_lr        = lambda s:        rm_s_from_s('\r',s)
rm_dbl_s     = lambda s:        replace_s_by_s('  ',' ',s)
clean_s      = lambda s:        rm_dbl_s(rm_lr(rm_ln(rm_tab(s))))
rm_s         = lambda s:        replace_s_by_s(' ','',s)
add_0_lt     = lambda d:        '0'+str(d) if d<10 else str(d)
ask          = lambda s:        fn.san(input(s))
get_act_yyyymmdd  = lambda : datetime.now().strftime('%Y%m%d')
get_act_yyyy      = lambda : datetime.now().strftime('%Y')
get_act_date_txt  = lambda : dates.DateAll(get_act_yyyymmdd()).text()
get_now           = lambda : datetime.now().strftime('%Y-%m-%d')
get_now_hh        = lambda : datetime.now().strftime('%H')

def println(s):   print(s_nl(s))
def lnprintln(s): print(ln_s_ln(s))

def get_now_plus():
    now = datetime.now()
    return ( now if int( now.strftime('%H') ) < 23
                 else now + timedelta( days = 1 )
             ).strftime('%Y-%m-%d')

def get_now_hh_plus_1():
    ihh = int( datetime.now().strftime('%H') )
    return add_0_lt(ihh+1) if ihh < 23 else '00'

def get_now_hh_plus_2():
    ihh = int( datetime.now().strftime('%H') )
    if ihh == 22:
        return '00'
    elif ihh == 23:
        return '01'
    else:
        return add_0_lt(ihh+2)

def join_list(l, sep):
    s, ndx, end = '', 0, len(l)
    while ndx < end:
        s += l[ndx]
        ndx += 1
        if ndx != end:
            s += sep
    return s

def replace_s_by_s(f,r,s):
    if s:
        if f in s:
            while f in s:
                s = s.replace(f, r);
    return s

def pause(s):
    input(s)

def stop():
    s = f"Exit program ? Press 'q' or 'Q' to exit..."
    if ask(s) in ['Q','q']:
        sys.exit('Programm stopped...')

def san(s):
    '''Function sanitizes input for use'''
    s = rm_lr(rm_ln(rm_tab(rm_dbl_s(str(s))))).strip().lower()
    return False if s == '' or not s else s
