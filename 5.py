import os
import  time as t
t.time()
from math import cos
print(cos(20))
import modeul5
modeul5.modeulfunc(3,4)
class  character():
    def __enter__(self):
     print("run")
    def __exit__(self, exc_type, exc_val, exc_tb):
     if exc_tb is None:
       print("正常退出，无异常 ")
     else:
       print("异常结束，异常为:%s"%exc_type)

    def __init__(self,name,hp,occu):
        self.name = name
        self.hp = hp
        self.occu = occu
    def move(self):
        print("Moving")
    def print(self):
            print('Charactername: ' + self.name + ',Characterhp: ' + str(self.hp) + ',Characteroccu: ' + self.occu)
class player(character):
    def __init__(self,name,hp,occu):
        self.name=name
        self.hp=hp
        self.occu=occu
    def change_name(self,newname):
        self.name=newname
class npc(character):
    def __init__(self,name,hp,weapon,occu):
        self.name=name #加了__前缀的属性无法在外部进行修改操作,只能读不能写,只能通过内部方法改变。
        self.hp=hp
        self.occu=occu
        self.__weapon=weapon
    def printweapon(self):
            print(self.__weapon)
player1=player('Felix',15000,'Warroir')
player1.print()
player1.change_name('Dantin')
player1.print()
npc1=npc('Vergil','30000','Yamato','Samurai')
npc1.printweapon()
#print(npc1.__weapon)#加了下划线外部无法访问
#npc1.print()
with character("Tom",2000,"assasssin"):
    print("running character")
    raise ZeroDivisionError