from price import *
def trade_SH600039():
    total = 0.00
    count = 0
    code = 'SH600039'
    c = buy(code, 4.43, 500)
    print c[0], c[1], c[2]
    total += c[0]
    count += c[2]

    c = buy(code, 4.42, 500)
    print c[0], c[1], c[2]
    total += c[0]
    count += c[2]

    c = sell(code, 4.50, 300)
    print c[0], c[1], c[2]
    total += c[0]
    count += c[2]

    c = sell(code, 4.48, 200)
    print c[0], c[1], c[2]
    total += c[0]
    count += c[2]
    print code, total, count, _round(total/count, 3)

def tradeSH601939():
    pass
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

if __name__ == '__main__':
    print '===== 601939 ===='
    tradeSH601939()
    planSH601939()
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




