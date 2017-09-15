# Hint:  use Google to find python function
import datetime as dt
def date_diff(begin_date, end_date, format_string):
    d1=dt.datetime.strptime(begin_date, format_string).date()
    d2=dt.datetime.strptime(end_date, format_string).date()
    return (d2 - d1).days

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
print(date_diff(date_start, date_stop, '%m-%d-%Y' ))

####b)
date_start = '12312013'
date_stop = '05282015'
print(date_diff(date_start, date_stop, '%m%d%Y'))

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
print(date_diff(date_start, date_stop, '%d-%b-%Y'))
