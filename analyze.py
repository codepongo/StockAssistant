import sys
import datetime
import currency
import stock

def average_price(code):
    average = 0.00
    stocks = stock.load_stock(code)
    for s in stocks:
        average += (s['low'] + s['high']) / 2
    average = average / len(stocks)
    return code, average


def low_during_days(days):
    '''the last day before that the stock price is falling during $days$'''
    date = []
    last = 0
    for d in data:
        if d['close'] - d['open'] < 0:
            last += 1
            if last > 7:
                date.append(d['date'])
                last = 0
        else:
            last = 0
    return date

def data_from_date_with_count(count, date):
    '''the $count$ stock data from $date$'''
    r = []
    flag = False
    for d in data:
        if d['date'] == date:
            flag = True
        if flag:
            r.append(d)
            count -= 1
        if count == 0:
            flag = False
    return r
            

def ccbc_low_during_7_days():
    '''the date the stock price is falling during 7 days'''
    data = loaddata('601939.ss')
    date = low_during_days(7)
    print date
    for d in date:
        print d
        data = data_from_date_with_count(7, d)
        for d in data: 
            print d['date'], (d['close'] - d['open'])/d['open'] * 100

def ccbc_cn_vs_hk():
    ''' the ccbc in china stock market and hongkong stock market'''
    cn = loaddata('601939.ss')
    print len(cn)
    hk = loaddata('0939.hk')
    print len(cn), len(hk)
    total = 0.0
    count = 0
    for c in cn:
        h = data_in_date(hk, c['date'])
        if h == None:
            continue
        currency_ = currency.currency_in_date(currency.loaddata(), c['date'])
        if currency_ == None:
            continue
        count += 1
        total += c['close'] - h['close'] * currency_
    print total/count

def lowest_price(code):
    stocks = stock.load_stock(code)
    r = stocks[0]
    for s in stocks:
        if r['low'] > s['low']:
            r = s
    return r

def days_price_low_than(code, price):
    stocks = stock.load_stock(code)
    total = 0
    days = 0
    for s in stocks:
        if s['high'] < price:
            days += 1
        total +=1
    return total, days
if __name__ == '__main__':
    print lowest_price('601939.ss')
    print average_price('601939.ss')
    print lowest_price('000623.sz')
    print average_price('000623.sz')
#    print days_price_low_than('600039.ss', 4.43)
