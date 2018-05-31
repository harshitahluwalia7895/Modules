import datetime
d=datetime.date.today()
m=d.month
print(m)


print('Another method')
d2=datetime.date.today()
mm=d2.strftime("%B")
print(mm)

