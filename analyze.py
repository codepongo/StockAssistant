#coding:utf8
import sys
import datetime
import currency
import stock
import rightsoffering

def is_down_in_day(s):
    if s['close'] < s['open']:
        return True
def is_up_in_day(s):
    if s['close'] > s['open']:
        return True
def change_of_day(s):
    return s['close'] - s['open'] 

def change_of_days(before, after):
    return after['close'] - before['open']

def tomorrow_up_when_how_many_is_down_today(stocks, percent, days):
    gain = 0
    total = 0
    length = len(stocks)
    for i in range(len(stocks)):
        if i+days+1 >= length:
            break
        percent_of_today = change_of_days(stocks[i], stocks[i+days]) * 100 /stocks[i-1]['close']
        if percent_of_today < percent:
            total += 1
            if change_of_day(stocks[i+days+1]) > 0:
                gain += 1
            else:
                pass
    if total == 0:
        return 0
    return gain * 100 / total

def x():
    win = 0
    days = [0, 0, 0]
    stocks = rebabilitate_forward('000623', 'sz')
    for i in range(len(stocks)):
        cur = stocks[i]
        if not is_down_in_day(cur):
            continue
        days[0] += 1
        if i -1 < 0:
            continue

        prev = stocks[i-1]
        if not is_up_in_day(prev):
            continue
        days[1] +=1
        if cur['low'] >= prev['low'] or cur['high'] >= prev['high']:
            continue
        days[2] += 1
        if i + 1 >= len(stocks):
            continue
        key = None
        j = i + 1
        while True:
            next = stocks[j]
            if not is_up_in_day(next):
                break
            if cur['low'] >= next['low'] or cur['high'] >= next['high']:
                break
            if next['low'] <= cur['low'] and next['high'] <= cur['high']:
                j = j + 1
                continue
            if next['low'] >= cur['low'] and next['high'] >= cur['high']:
                key = stocks[j]
                break
        if key == None:
            continue
        print str(key['date'])[:10]
        if stocks[j+1]['open'] > key['open']:
            win += 1
        return win/len(stocks)
        
def rebabilitate_forward(code, market):
    stocks = stock.load_stock(code+'.'+market)
    rights_offering = rightsoffering.load(code)
    for s in stocks:
        rate = 1.00
        for r in rights_offering:
            if s['date'] <= r['date']:
                rate = rate * (1 + r['dividend'])
        s['open'] = s['open'] * rate
        s['close'] = s['close'] * rate
        s['high'] = s['high'] * rate
        s['low'] = s['low'] * rate
    return stocks



def average_price(code):
    stocks = stock.load_stock(code)
    return code, average_price_in_data(stocks)

def average_price_in_data(stocks):
    average = 0.00
    for s in stocks:
        average += (s['low'] + s['high']) / 2
    average = average / len(stocks)
    return average


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

def highest_price_in_data(stocks):
    r = stocks[0]
    for s in stocks:
        if r['high'] < s['high']:
            r = s
    return r

def lowest_price_in_data(stocks):
    r = stocks[0]
    for s in stocks:
        if r['low'] > s['low']:
            r = s
    return r


def lowest_price(code):
    stocks = stock.load_stock(code)
    lowest_price_in_data(stocks)


def days_price_low_than(code, price):
    stocks = stock.load_stock(code)
    return days_price_low_than_in_data(price, stocks)

def days_price_low_than_in_data(price, stocks):
    dates = []
    days = 0
    for s in stocks:
        if s['low'] < price:
            days += 1
            dates.append(s['date'])
    return len(stocks), days, dates

def ccbc_percent_when_hz500_down_5_percent():
    ccbc = stock.load_stock('601939.ss')
    hz500 = stock.load_stock('000300.ss')
    for i in xrange(len(hz500)-1):
        if (hz500[i+1]['open'] - hz500[i]['close']) * 100 / hz500[i]['open'] < -5:
            for v in ccbc:
                if hz500[i]['date'] == v['date']:
                    print hz500[i]['close'], hz500[i+1]['open']
                    print "%.2f" % ((v['close'] - v['open']) * 100 / v['open'])
def agv_when(data):
    code = '000001'
    market = 'ss'
    szzs = stock.load_stock(code+'.'+market)
    date = []
    for ss in szzs:
        if ss['open'] < 2760 and ss['open'] > 2650:
            date.append(ss['date'])
    price = 0.00
    count = 0
    for d in data:
        if d['date'] in date:
            count += 1
            avg = (d['close'] + d['open']) / 2 
            price += avg
    return price/count




if __name__ == '__main__':
    code = '000623'
    market = 'sz'
    
    stocks = stock.load_stock(code+'.'+market)
    days = 4
    for i in range(10 * days):
        percent = -i
        print '%.2f%% -- %.2f%%' % (percent, tomorrow_up_when_how_many_is_down_today(stocks, percent,days))

    stocks = rebabilitate_forward(code, market)
    for i in range(10 * days):
        percent = -i
        print '%.2f%% -- %.2f%%' % (percent, tomorrow_up_when_how_many_is_down_today(stocks, percent,days))
    sys.exit(0)




    code = '601939'
    market = 'ss'
    data = stock.load_stock(code+'.'+market)
    data = rebabilitate_forward(code, market)
    avg = agv_when(data)
    current = data[-1]['close']
    print code, current, avg, (current - avg) * 100 / 14.86
    
    code = '000623'
    market = 'sz'
    data = stock.load_stock(code+'.'+market)
    data = rebabilitate_forward(code, market)
    avg = agv_when(data)
    current = data[-1]['close']
    print code, current, avg, (current - avg) * 100 / 14.86

    code = '600036'
    market = 'ss'
    data = stock.load_stock(code+'.'+market)
    data = rebabilitate_forward(code, market)
    avg = agv_when(data)
    current = data[-1]['close']
    print code, current, avg, (current - avg) * 100 / 14.86


    code = '600511'
    market = 'ss'
    data = stock.load_stock(code+'.'+market)
    avg = agv_when(data)
    current = data[-1]['close']
    print code, current, avg, (current - avg) * 100 / 14.86

    sys.exit(0)





    code = '601939'
    market = 'ss'
    stocks = stock.load_stock(code+'.'+market)
    print 'low:', lowest_price_in_data(stocks)['low']
    print 'high:', highest_price_in_data(stocks)['high']
    avg = average_price_in_data(stocks)
    print 'avg:', avg
    cur = 5.09
    r = days_price_low_than_in_data(cur, stocks)
    print 'low than',cur, ':', 100 * r[1] / r[0], '%'

    print 'right offering****'
    stocks = rebabilitate_forward(code, market)
    print 'low:', lowest_price_in_data(stocks)['low']
    print 'high:', highest_price_in_data(stocks)['high']
    avg = average_price_in_data(stocks)
    print 'avg:', avg
    cur -5.09
    r = days_price_low_than_in_data(cur, stocks)
    print 'low than',cur, ':', 100 * r[1] / r[0], '%'
    sys.exit(0)
#    ccbc_percent_when_hz500_down_5_percent()


#    stocks = stock.load_stock('000623.sz')
#    print lowest_price_in_data(stocks)['low']
#    print highest_price_in_data(stocks)['high']
#    r = days_price_low_than_in_data(15.77, stocks)
#    print r[:2]
#    print average_price_in_data(stocks)
#    print lowest_price('601939.ss')
#    print average_price('601939.ss')
#    print lowest_price('000623.sz')
#    print average_price('000623.sz')
#    print days_price_low_than('600039.ss', 4.43)
