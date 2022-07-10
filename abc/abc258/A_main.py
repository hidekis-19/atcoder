import datetime
k = int(input())

t1 = datetime.time(21, 0)
t2=  datetime.datetime.combine(datetime.date.today(), t1) + datetime.timedelta(minutes=k)
print(t2.strftime("%H:%M"))
