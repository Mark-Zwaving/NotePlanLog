''' Library contains a class to handle dates'''

__author__     =  "Mark Zwaving"
__email__      =  "markzwaving@gmail.com"
__copyright__  =  "Copyright 2019 (C) Mark Zwaving. All rights reserved."
__license__    =  "GNU Lesser General Public License (LGPL)"
__version__    =  "0.9"
__maintainer__ =  "Mark Zwaving"
__status__     =  "Development"

import datetime
import init

class DateAll():
    def __init__(self, yyyymmdd):
        if init.web_language == 'NL':
            self.months = [ 'januari', 'februari', 'maart', 'april',
                            'mei', 'juni', 'juli', 'augustus',
                            'september', 'oktober', 'november', 'december'
                            ]
            self.days   = [ 'maandag', 'dinsdag', 'woensdag', 'donderdag',
                            'vrijdag', 'zaterdag', 'zondag'
                            ]
        else: # DEFAULT EN
            self.months = [ 'january', 'february', 'march', 'april',
                            'may', 'june', 'july', 'august',
                            'september', 'oktober', 'november', 'december'
                            ]
            self.days   = [ 'monday', 'tuesday', 'wednesday', 'thursday',
                            'friday', 'saturday', 'sunday'
                            ]

        self.y, self.m, self.d = int(yyyymmdd[:4]), int(yyyymmdd[4:6]), int(yyyymmdd[6:8])
        self.date = datetime.date(self.y, self.m, self.d)

    def weekday(self): return self.days[self.date.weekday()]
    def month(self):   return self.months[self.date.month-1]
    def yyyy(self):    return str(self.y)
    def mm(self):      return str(self.m) if self.m > 9 else "0%i" % self.m
    def dd(self):      return str(self.d) if self.d > 9 else "0%i" % self.d
    def text(self):    return f'{self.weekday()}, {self.dd()} {self.month()} {self.yyyy()}'
    def yyyy_mm_dd(self): return f'{self.yyyy()}-{self.mm()}-{self.dd()}'

def cnt_days(ymd_s, ymd_e):
    ys, ms, ds = ymd_s[:4], ymd_s[4:6], ymd_s[6:8]
    ye, me, de = ymd_e[:4], ymd_e[4:6], ymd_e[6:8]

    d0 = datetime.date( int(ys), int(ms), int(ds) )
    d1 = datetime.date( int(ye), int(me), int(de) )

    delta = ( d1 - d0 ).days
    return delta
