from price import * 
def tradeSZ000895():
    total = 0.00
    count = 0
    code = 'SZ000895'
    c = buy(code, 17.88, 100)
    total += c[0]
    count += c[2]
    print c[0], c[1], c[2]
    c = sell(code, 18.16, 100)
    total += c[0]
    count += c[2]
    print c[0], c[1], c[2]
    print total

def tradeSH600039():
    total = 0.00
    count = 0
    code = 'SH600039'
#    c = buy(code, 4.43, 500)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#    c = buy(code, 4.42, 500)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#    c = sell(code, 4.50, 300)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#    c = sell(code, 4.48, 200)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    print code, total, count, _round(total/count, 3)
#
    c = buy(code, 4.50, 500)
    print c[0], c[1], c[2]
    total += c[0]
    count += c[2]
    c = buy(code, 4.38, 800)
    print c[0], c[1], c[2]
    total += c[0]
    count += c[2]
    c = sell(code, 4.52 , 1300)
    print c[0], c[1], c[2]
    total += c[0]
    count += c[2]
    print total
def tradeSH601939():
#    total = 0.00
#    count = 0
#    c = buy('SH601939', 6.35, 100)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    c = buy('SH601939', 6.23, 100)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    c = buy('SH601939', 5.96, 200)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    c = buy('SH601939', 5.71, 200)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    c = buy('SH601939', 5.11, 600)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    print '=', total, count, abs(total/count)
#    c = buy('SH601939', 4.94, 600)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    c = buy('SH601939', 4.94, 2000)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    c = buy('SH601939', 4.68, 1600)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    
#    c = sell('SH601939', 4.90, 1000)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#    
#    c = sell('SH601939', 4.95, 1500)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#
#    c = buy('SH601939', 4.61, 3000)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#    c = sell('SH601939', 4.69, 3000)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#    c = sell('SH601939', 4.92, 1000)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#
#    c = sell('SH601939', 5.00, 1000)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#    c = sell('SH601939', 4.98, 600)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
#
#    print total, count, abs(total/count)
#    total -= 300
#    count += 100
#    print total, count, abs(total/count)
#
#    total = 7944.00
#    count = 400
#    print (10000-7944.0), count, abs((10000.00-7944.00)/count)
#    c = buy('sh601939', 5.08, 400)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]

#    c = sell('sh601939', 5.12, 400)
#    print c[0], c[1], c[2]
#    total += c[0]
#    count += c[2]
    c = sell('sh601939', 5.5, 100)
    print c[0], c[1], c[2]

    #print total, count, abs(total/count)
def planSH601939():
    spent = -2066
    count = 400
    total = 10000 + spent
    i = 1
    while True:
        price = 5.00 * (0.97 ** i)
        if  price < 3.46:
            break
        if price < 4.5:
            x = 400
        else:
            x = 100 
        c = cost('SH601939', price, x)
        if total + c[0] < 0.0:
            break
        total += c[0]
        spent += c[0]
        count += c[2]
        print money_round(abs(c[0]), 2), money_round(c[1],3), c[2]
        i += 1
    print '^', spent, count, money_round(spent/count, 3)

def planSZ000623():
    total = 0.00
    count = 0
    code = 'SZ000623'
    c = cost(code, '21.57', 100)
    total += c[0]
    count += c[2]
    c = cost(code, '19.21', 100)
    total += c[0]
    count += c[2]
    c = cost(code, '16.00', 100)
    total += c[0]
    count += c[2]
    c = cost(code, '13.00', 100)
    total += c[0]
    count += c[2]
    c = cost(code, '12.11', 200)
    total += c[0]
    count += c[2]
    print total, count, money_round(total/count, 3)

if __name__ == '__main__':
    c = cost('SH601939', '5.66', 200)
    print c
#    print '===== 601939 ===='
#    tradeSH601939()
#    print '===== 60039 ===='
#    tradeSH600039()
#    print '===== 000895 ===='
#    tradeSZ000895()
#    print '===== 000623 ===='
#    planSZ000623()
#    planSH601939()
#    print '===== 600039 ===='
#    deal_with_SH600039()
#    total = 0
#    count = 0
#    c = cost('SH600039', 4.43, 500)
#    print c[4], c[5]
#    total += c[3]
#    count += c[5]
#    c = cost('SH600039', 4.42, 500)
#    print c[4], c[5]
#    total += c[3]
#    count += c[5]
#    count -= 300
#    total -= 4.50 * 300
#    count -= 200
#    total -= 4.48 * 200
#    print total, count, total/count




