import datetime
import json
import urllib
import time
from util import *
currency_csv = 'currency.csv'
def currency_now_from_yahoo():
    d = {}
    r = open_url('http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=HKDCNY=X')
    if r is None:
        return None
    r = r.split(',')
    d['currency'] = float(r[1])
    d['date'] = r[2]
    t = d['date'].replace('"', '').split('/')
    for i in range(len(t)):
        t[i] = int(t[i])
    d['date'] = datetime.datetime(t[2], t[0], t[1])
    return d

def currency_now():
    with open(currency_csv, 'rb') as f:
        i = -2
        while True:
            f.seek(i,2)
            c = f.read(1)
            if c == '\n':
                break
            i -= 1
        l = f.read()
        d = {}
        d['date'], d['currency'] = l.split(',')
        d['date'] = s_to_date(d['date'])
        d['currency'] = float(d['currency'])
        if d['date'].date() == datetime.datetime.now().date():
            return d['currency']
        else:
            return None

def append_currency_now():
    if currency_now() is not None:
        return True
    wait = 1
    for i in range(1, 10):
        d = currency_now_from_yahoo()
        if d is not None:
            append_data(d)
            return True
        else:
            print 'sleep %ds then try again...' % (wait)
            time.sleep(wait)
            wait = wait * i
    return False
def append_data(d):
    s = ('%s,%.3f\n') % (d['date'].strftime('%Y-%m-%d'), d['currency'])
    with open(currency_csv, 'ab+') as f:
        f.write(s)

def save_data_to_csv(data):
    with open(currency_csv, 'wb') as f:
        for d in data:
            s = ('%s,%.3f\n') % (d['date'].strftime('%Y-%m-%d'), d['currency'])
            f.write(s)

def load_data():
    data = []
    with open(currency_csv, 'rb') as f:
        lines = f.readlines()
    for l in lines:
        d = {}
        d['date'], d['currency'] = l.split(',')
        d['date'] = s_to_date(d['date'])
        d['currency'] = float(d['currency'])
        data.append(d)
    return data


def load_data_from_origin():
    data = []
    with open( 'FRB_H10.csv', 'rb') as f:
        lines = f.readlines()
    lines = lines[1:]
    for l in lines:
        if l[0] == '"':
            continue
        d = {}
        d['date'], cny_usd, hkd_usd = l.split(',')
        if cny_usd == 'ND' or hkd_usd == 'ND':
            continue
        else:
            d['currency'] = float(cny_usd) / float(hkd_usd)
        t = d['date'].split('-')
        for i in range(len(t)):
            t[i] = int(t[i])
        d['date'] = datetime.datetime(*t)
        data.append(d)
    return data

def currency_in_date(data, date):
    for d in data:
        if d['date'] == date:
            return d['currency']
    return None

if __name__ == '__main__':
    append_currency_now()
