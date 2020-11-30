price = {'김밥':5000, '어묵': 3000, '떡볶이' : 2000}
print(price['김밥'])
price['김밥']=7000
print(price)
print(price.keys())
print(len(price))

for k in price.keys():
    print(" %s -> %s" % (k, price[k]))

price['순대'] = 2500
print(price)