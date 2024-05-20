import threading
from threading import  current_thread
import  time as t
def myfunc(arg1,arg2):
    print(current_thread().name, "start")
    print(str(arg1)+','+str(arg2))
    print(current_thread().name, "end")
for i in range(1,20,2):
     t1=threading.Thread(target=myfunc,args=(i,i+1))
     t2=threading.Thread(target=myfunc,args=(i+1,i+2))
     t1.run()
    # t.sleep(2)
     t2.run()
    # t.sleep(2)
print(current_thread().name, "end")
class Mythread(threading.Thread):
    def start(self):
        print(current_thread().getName(), "start")
        print("run")
        print(current_thread().getName(), "end")
        self.run()
# for i in range(1,20,2):
#     t1=Mythread(target=myfunc,args=(i,i+1))
#     t2 = Mythread(target=myfunc, args=(i+3, i + 4))
#     t1.start()
#     t2.start()
# print(current_thread().getName(),"end")
