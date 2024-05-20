import  re
import  zodiac7 as z
# p1=re.compile("ca+.t")#  *代表前面的字符出现0次到无数次，？代表出现0次或者1次，+代表1次或者无数次
# print(p1.match("caaaaaaaaabt"))
# print(p1.match("cbt"))
# p1=re.compile("ca?.t")#  *代表前面的字符出现0次到无数次，？代表出现0次或者1次，+代表1次或者无数次
# print(p1.match("cbt"))
# print(p1.match("caaaaaaaaabt"))
# p2=re.compile("ca{4,6}t")#大括号内是a可以有几个
# print(p2.match("caaaat"))
# print(p2.match("caat"))
# p3=re.compile("^cat")#以cat开头的字符
# p4=re.compile("cat$")#以cat结尾的字符?
# print(p3.match("catlinzhe"))
# print(p4.match('asdadcat'))
# p5=re.compile("ca[bcd]t")#中括号内包含符合的所有字符
# print(p5.match("cadt"))
# print(p5.match("caat"))
# print(p5.match("cabt"))
# print(p5.match("caet"))
#()分组取出功能，十分强大，经常性使用
p=re.compile(r"(\d+)-(\d+)-(\d+)")
flag=True
while flag==True:
 try :
    str=input("请输入出生年月日，并以-连接: ")
    p_2=re.sub(r'#.*','',str)
    p_2=re.sub(r'\D','',p_2)
    print(p_2)
    #bitth = p.match(str)
    bitth=p.search(str)
    if bitth is None:
        raise NameError
    else:
        #year, month, day = p.match(str).groups(),还可以使用findall（）函数它可以查找所有符合的字符串而并非第一次出现的
        year, month, day = p.search(str).groups()#search会在整一条字符串内寻找符合的字符串并获取它的位置
        flag=False
        pass
 except NameError:
     print("您输入的方式或内容有误，请重新输入，注意不能包含除-以外的特殊字符，不要输入字母")
print("您的出生年月日是：%s-%s-%s"%(year,month,day))
birthdate = z.datetime.date(int(year), int(month), int(day))
zodiac_sign = z.calculate_zodiac_sign(birthdate)
print('属' + z.chinese_zodiac[birthdate.year % 12] + ',', zodiac_sign + ',',z.zodiac_name[z.calculate_zodiac_sign_withoutjudge(birthdate)])


