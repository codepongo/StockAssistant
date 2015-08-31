from util import *
def file_from_code(code):
    return code + '.csv'
def load_stock(code):
    '''load the stock data from $code$.csv file'''
    data = []
    with open(file_from_code(code), 'rb') as f:
        lines = f.readlines()
    lines = lines[1:]
    for l in lines:
        d = {}
        d['date'], d['open'], d['high'], d['low'], d['close'] = l.split(',')[:5]
        d['date'] = s_to_date(d['date'])
        d['open'] = float(d['open'])
        d['high'] = float(d['high'])
        d['low'] = float(d['low'])
        d['close'] = float(d['close'])
        data.append(d)
    data.reverse()
    return data


def stock_in_date(data, date):
    '''the stock data in $date$'''
    for d in data:
        if d['date'] == date:
            return d
    return None

def append_stock_to_now(code, data = None):
    if data is None:
        data = load_stock(code)
    from_date = data[-1]['date'].date() + datetime.timedelta(days=1)
    return append_stock_from_to_now(code, from_date, data)

def append_stock_from_to_now(code, from_date, data = None):
    if data is None:
        stock = load_stock(code)
    print from_date
    now = datetime.datetime.now().date()
    yesterday = now - datetime.timedelta(days=1)
    print now, yesterday
    # because the data from yahoo is delay a day so, check yesterday
    if stock_in_date(data, yesterday) is not None:
        return True
    url = 'http://ichart.yahoo.com/table.csv?s=%s&a=%02d&b=%02d&c=%4d&d=%02d&e=%02d&f=%4d&g=d' % (code, from_date.month-1, from_date.day, from_date.year, now.month-1, now.day, now.year)
    r = open_url(url)
    if r is None:
        return False
    with open(file_from_code(code), 'rb+') as f:
        title_len = len('Date,Open,High,Low,Close,Volume,Adj Close\n')
        f.seek(title_len, 0)
        f.write(r[title_len:])
    return True

if __name__ == '__main__':
    append_stock_to_now('601939.ss')
    append_stock_to_now('0939.hk')
    append_stock_to_now('600039.ss')
    append_stock_to_now('000001.ss')
