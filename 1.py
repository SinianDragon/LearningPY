# alist=[i*i for i in range(1,12) if(i%2=20=0)]
# print(alist)
# zodiac_name = ("摩羯座","水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座","射手座")
# adic={i:0 for i in zodiac_name}
# print(adic)
#file1.write('lz is a dumbass')
#file1.close()
# file1=open('name.txt','a')
# file1.write('lz is not a dumbass now')
# file1.close()
# file1=open('name.txt')
# file1.read(10)
# print(file1.tell())
# print(file1.read())
# file1.seek(0)
# print(file1.tell())
# file1.seek(10,0)  #0从开头开始偏移，1从当前位置开始偏移，2从结尾开始偏移
# print(file1.tell())
# print(file1.read())
flag = True
year = 0
while flag == True:
 flag = False
 try:
    year=int(input("请输入您的出生年份:"))
    print(year/4)
 except ValueError as V:
 # except  Exception (ValueError, AttributeError, KeyError, ZeroDivisionError):
    print("请输入完整的数字，不要带字母或者特殊字符 %s"%(V))
    flag = True
 except ZeroDivisionError:
  print("0不能作为除数")
  flag = True
 finally:
     print('',end='')

print("您的出生的年份为: %d "%(year))
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
