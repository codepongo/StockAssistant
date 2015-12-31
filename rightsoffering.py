#coding:utf8
from util import *
import HTMLParser
def code_to_file(code):
    return code + '.rightsoffering.csv'
def load(code):
    data = []
    with open(code_to_file(code), 'rb') as f:
       lines = f.readlines()
    for l in lines:
        d = {}
        d['date'], d['dividend'] = l.split(',')
        d['date'] = s_to_date(d['date'])
        d['dividend'] = float(d['dividend'])
        data.append(d)
    return data

def save_to(code, data):
    with open(code_to_file(code), 'wb') as f:
        for d in data:
            s = ('%s,%.3f\n') % (d['date'].strftime('%Y-%m-%d'), d['dividend'])
            f.write(s)

def rights_offering(data):
    r = []
    for d in data:
        if d['dividend'] != '--' or d['transfer'] != '--':
            i = {}
            i['date'] = s_to_date(d['ex-dividend'])

            i['dividend'] = 0.0
            if d['dividend'] != '--':
                i['dividend'] += float(d['dividend'])
            if d['transfer'] != '--':
                i['dividend'] += float(d['transfer'])
            i['dividend'] /= 10.00
            r.append(i)
    r.reverse()
    return r

def dividend_bonus(code, data):
    with open(code+'.dividend.bonus.csv', 'wb') as f:
        f.write('简介,公告日,分红,送股,转增股,登记日,除权日,备注\n')
        for d in data:
            s = d['name'] + ',' + d['bulletin'] + ',' + d['bonus'] + ',' + d['dividend'] + ',' + d['transfer'] + ',' + d['record'] + ',' + d['ex-dividend'] + ',' + d['remark'] + '\n' 
            s = s.encode('utf8')
            f.write(s)

    
def feed_from_hexun(code):
    url = 'http://stock.quote.stockstar.com/dividend/bonus_%s.shtml' % (code)
    r = open_url(url)
    class Parser(HTMLParser.HTMLParser):
        def __init__(self):
            self.keys = ['name', 'bulletin', 'bonus', 'dividend', 'transfer', 'record', 'ex-dividend', 'remark']#简称，公告日，分红，送股，转增股，登记日，除权日，备注
            self.should_fetch_data = None 
            self.data = []
            self.cur = {}
            HTMLParser.HTMLParser.__init__(self)
        def handle_starttag(self, tag, attrs):
            if tag == 'tbody':
                for key, value in attrs:
                    if key == 'class' and value == 'tbody_right':
                        self.should_fetch_data = False
                        return
            if self.should_fetch_data == False and tag == 'td':
                self.should_fetch_data = True
                return

        def handle_endtag(self, tag):
            if self.should_fetch_data and tag == 'tbody':
                self.should_fetch_data = False
        def handle_data(self, data):
            if self.should_fetch_data:
                for i in range(len(self.keys)):
                    if not self.cur.has_key(self.keys[i]):
                        self.cur[self.keys[i]] = data.decode('gbk')
                        if i == len(self.keys) - 1:
                            self.data.append(self.cur)
                            self.cur = {}
                        break
    if r == None:
        return None
    p = Parser()
    p.feed(r)
    return p.data

if __name__ == '__main__':
    code = '000623'
    dividend_bonus(code, feed_from_hexun(code))
    #save_to(code, rights_offering(feed_from_hexun(code)))

