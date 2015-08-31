import sys
import datetime
import currency

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


if __name__ == '__main__':
    analyze_0939_cn_vs_hk()
