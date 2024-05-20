# 这是一个示例 Python 脚本。
# 按 Shift+E 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#,encoding='GB18030')
import re
def cacul_item(hero):
    with open("3-game.txt",encoding='utf-8') as f:
     data=f.read().replace('\n','')
     hero_num=re.findall(hero,data)
     print("%s 在游戏里面出现了 %s 次。"%(hero,len(hero_num)))
    return hero_num
def print_num(txt):
    name_dictonary = {}
    with open(txt) as f:
        for hero in f:
            print(hero.replace('\n',''))
            names = hero.replace('\n','').split('|')
            for n in names:
                name_num = cacul_item(n)
                name_dictonary[n] = name_num
    for n in name_dictonary:
     print(n,"+",len(name_dictonary[n]))
# f=open("hero.txt")
# print(f.read().replace('\n','').split('|'))
#print_num("3-hero.txt")
# f2=open("3-weapon.txt",encoding='utf-8')
# print(f2.read())
# def cacul_lenth(first,*other):
#     return 1+len(other)
# print(cacul_lenth(123,{321,432,543},421))
# other={321,432,543}
# print(len(other))
# list1=[1,2,3]
# print(list1[0])
# it = iter(list1)
# print(next(it))
def frange(start,end,step):
    x = start
    while x<end:
        yield x#print(x),yield生成器每次返回一个值
        x+=step
# for i in frange(10,20,0.5):
#     # print(i)
def ffrange(start,end,step):
    x = start
    while x < end:
       num = yield x  # print(x),yield生成器每次返回一个值，并保存当前状态(在此步暂停，以下的语句都不运行)，以便下一次调用
       print("当前num传入的值是%s"%(num))
       if num is not None:
         x = num
       x = x+ step
    return x
ff = ffrange(10,20,1)
# print(next(ff))
# print(ff.send(15))
# for i in ff:
#       print(i)
sum1=lambda item: item[0]
sum2=lambda item: item[1]
asd={'a' : 'aa','b' : 'bb'}
for i in asd.items():
    print(sum1(i))
    print(sum2(i))
print(asd.items())



