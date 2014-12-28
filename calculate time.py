#coding:utf-8

#b)随机选择有限域上的元素做100000个乘法和100000个求逆元，测试计算时间。

from finitefield  import *
import time

#随机获取多个多项式
num=20
polys=GetManyElements(num)

#乘法（第一个分别和第一个到最后一个做乘法）
beginTime = time.clock()
multiPs=[]
p1=polys[0]
for p2 in polys:
    multiPs.append(PolyMulti(p1, p2))

print '有限域乘法耗时：',time.clock()-beginTime
#求逆
beginTime = time.clock()
invPs=[]
for p in polys:
    invPs.append(PolyInv(p))
#     print PolyMulti(invPs[-1], p)

print '有限域求逆耗时：',time.clock()-beginTime












