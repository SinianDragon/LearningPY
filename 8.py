import time
import  os
import  random
import  datetime
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.now())
deltatime=datetime.timedelta(minutes=20)
print(datetime.datetime.now()+deltatime)
one_day=datetime.datetime(2008,8,28)
deltaday=datetime.timedelta(days=30)
print(one_day+deltaday)
random1=random.randint(1,10)
print(random1)
print(random.choice(['a','aa','b','bb','c','cc']))
print(os.path.isdir('/C'))