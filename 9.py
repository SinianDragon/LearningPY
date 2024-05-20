import  numpy as np
import  pandas as pd
from numpy import  nan as na
from random import  randint
from pandas import  Series,DataFrame
arr1=np.array([1,2,3,4])
arr2=np.array([1.2,2.3,3.4,4.5])
print(arr1.dtype),print(arr2.dtype),print(arr1+arr2),print((arr2+arr1)*10)
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3),print(np.zeros((4,4))),print(np.ones((5,5))),print(np.empty((3,3,3)))
arr4=np.arange(10)
print(arr4)
arr4[5:8]=10
print(arr4)
arr4_copy=arr4[5:8].copy()
arr4_copy[:]=15
print(arr4_copy),print('')
obj1=Series([4,5,6,7])
print(obj1),print(obj1.index)
obj2=Series([4,5,6,7],index=['a','b','c','d'])
obj2['a']=8
print(obj2)
ditc1={'lz':100,'oybh':99,'trz':59,'lhy':99}
ditc2=Series(ditc1)
ditc2['trz']=99
print(ditc2)
ditc2.index=['linzhe','ouyangbaohua','turuizhe','linhaoyuan']
print(ditc2)
data1={'city':['shanghai','shenzhen','beijing','guangzhou'],
      'year':[2016,2017,2018,2019],'pop':[1.5,1.6,1.7,1.8]}
data2=DataFrame(data1,columns=['year','pop','city'])
print(data2),print(data2.city)
data2['num']=1000
data2['Capital']=data2['city']=='beijing'
print(data2)
data3 = Series([1,na,2])
print(data3.dropna())
data4=DataFrame([[1,6.5,3],[2,na,na],[na,na,na]])
data4[4]=na
print(data4)
print(data4.dropna(axis=1,how='all'))
data4.fillna(0,inplace=True)#注意fillna函数不会返回自己,不要傻傻的print这个值,只会return一个bool判断运行有无出错
print(data4)
test={'Linzhe':{18:90,20:100},'Turuizhe':{18:100,20:90}}
test=DataFrame(test)
print(test),print(test.T)
obj3=Series([1,2,3,4],index=['a','b','c','d'])
obj3=obj3.reindex(['a','b','c','d','e',],fill_value=0)
print(obj3)
obj4=Series(['blue','red','yellow','purple'],index=[0,2,4,6])
print(obj4)
obj4=obj4.reindex(range(7),method='ffill')
print(obj4)
obj5=Series(np.random.randn(12),index=[['a','a','a','a','b','b','b','b','c','c','c','c'],[1,2,3,4,1,2,3,4,1,2,3,4]])
print(obj5['b':'c']),print(obj5['b'][3]),print(obj5.unstack())#unstack后变成二维的数据了即Dataframe类型的数据
