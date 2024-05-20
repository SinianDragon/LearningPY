import  time
from functools import  reduce
#iterable是一个迭代器变量，相当于一个栈，一个迭代容器，内涵init初始化函数和iter把自身变成iterrator的函数
#而iterator是一个迭代方法，类似于一个函数类，内涵init初始化函数和next函数向外每次提取一个栈顶的值，并且最好iterrator有一个iter->
#->函数，这样的话它也可以自身iter自身变成自己，即self。
def caculte_num(x,y):
    print(x),print(y)
    print(list(filter(lambda  x:x+1,x)))
    print( list(filter(lambda x:(x>2 or x<0),y)))
    print(list(map(lambda x,y:x+y,x,y)))
    print(reduce(lambda x,y : x-y ,x,1))#注意此处前面lambada函数内的x是后面传入值x后面的那个1
    return 0
x=[-2,1,2,3,4,5,6,7]
y=[-1,2,3,4,5,6,7,8]
dict1={'a':'aa','b':'bb'}
dict2=zip(dict1.values(),dict1.keys())#zip将前后值相加并矩阵转置导致值调换。
for i in dict2:
    print(i)

def count(num=0):
    couter =[num]

    def caclu():
     couter[0] +=1
     return couter[0]

    return caclu
count5,count10=count(5) ,count(10)
count10(),count5(),count10(),count10(),count10(),count10(),count5(),count5()
print(count5()),print(count10())
caculte_num(x,y)

def tips_new(tip,second):
 def tips(func):
    def inter(a,b):
        print("start @%s-%s"%(tip,func.__name__))
        start=time.time()
        func(a,b)
        time.sleep(second)
        print("stop")
        stop=time.time()
        return -start+stop+a+b
    return  inter
 return tips
@tips_new("addtips",1)
def add(a,b):
    print(a+b)
    return  a+b
@tips_new("subtips",2)
def sub(a,b):
    print(a-b)
    return  a-b
#有参数的tips_new调用add(3,1),等价于add=tips_new("add",1)(add)
#没有参数的tips调用add(3,1),等价于add=tips(add)
print(add(3,1))
print(sub(5,1))
