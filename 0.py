import time
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
#print(chinese_zodiac[0:-1])
zodiac_name = ("摩羯座","水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座","射手座")
zodiac_dates = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
def calculate_zodiac_sign(birthdate):
    month, day = birthdate.month, birthdate.day
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "Gemini"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "Libra"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "Scorpio"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"
def calculate_zodiac_sign_withoutjudge(birthdate):
  month, day = birthdate.month, birthdate.day
  zodiac_day = filter(lambda x: x<=(month,day),zodiac_dates)
  zodiac_day=list(zodiac_day)
  print(zodiac_day)
  zodiac_len = len(list(zodiac_day))%12
  return zodiac_len
# 示例用法
def calculate_zodiac_sign_withoutjudge2(month,day):
 for num in range(len(zodiac_name)):
    if zodiac_dates[num] >= (month,day):
        print(zodiac_name[num])
        break
    elif month ==12 and day >=24:
        print(zodiac_name[0])
        break
def calculate_zodiac_sign_withoutjudge3(month,day):
  n = 0
  while zodiac_dates[n]<(month,day):
     if month ==12 and day>=24:
         n=0
         break
  print(zodiac_name[n])
import datetime
cz_num, z_num ={},{}
for x in chinese_zodiac:
    cz_num[x]=0
for x in zodiac_name:
    z_num[x]=0
Option='Y'
while Option=='Y':
    # year = int(input('请输入您的出生年份:'))
    # month = int(input("请输入您的出生月份:"))
    # day = int(input("请输入您的出生发日期:"))
   year, month, day, num =  0, 0, 0, 0
   try:
    birth=input('请输入您的出生日期:')
    for x in range(len(birth)):
        if birth[x] == ' ' and year != 0:
            month = int(birth[num:x])
            num=x+1
        elif birth[x]==' ' :
            year = int(birth[0:x])
            num=x+1
        elif year != 0 and month != 0:
            day = int(birth[num:len(birth)])
    birthdate = datetime.date(year, month, day)
    zodiac_sign = calculate_zodiac_sign(birthdate)
    print('属' + chinese_zodiac[birthdate.year % 12] + ',', zodiac_sign + ',',zodiac_name[calculate_zodiac_sign_withoutjudge(birthdate)])
    cz_num[chinese_zodiac[birthdate.year % 12] ]+=1
    z_num[zodiac_name[calculate_zodiac_sign_withoutjudge(birthdate)]]+=1
    quantity = input("您要查阅统计数量吗，想要查阅请输入y:")
    if(quantity =='y'):
        for each_key in cz_num.keys():
            print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))
        for each_key in z_num.keys():
            print('星座 %s 有 %d 个' % (each_key, z_num[each_key]))
    else:
        print("您选择不查阅")
    Option = input("您想要继续吗？继续请输入Y:")
   except ValueError:
       print("您输入的出生日期有误，月份请勿超过12，日请勿超过31，请重新输入")





