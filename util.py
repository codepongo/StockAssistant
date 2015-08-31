import datetime
import urllib
def s_to_date(s):
    t = s.split('-')
    for i in range(len(t)):
        t[i] = int(t[i])
    return datetime.datetime(*t)

def money_round(f,n):
    carry = 1
    for i in range(n):
        carry *= 10
    f *= carry
    approximate = int(f)
    if f - approximate >= 0.5:
        approximate += 1

    approximate = float(approximate)
    for i in range(n):
        approximate /= 10
    return approximate

def open_url(url):
    try:
        r = urllib.urlopen(url)
        if 200 != r.getcode():
            raise
    except:
        print 'except'
        return None
    return r.read()

