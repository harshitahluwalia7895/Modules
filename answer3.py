import datetime
d=datetime.date.today()
m=d.month
print("Current month is ",m)


print('Another method')
d2=datetime.date.today()
m1=d2.strftime("Current month  is %B")
print(m1)





