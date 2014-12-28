#coding:utf-8

import random

#多项式表示：pn(x)=sum(ak*x^k)，k=0,...,7
#a)在x86/windows平台上实现有限域GF(28)的运算。


def PolyAdd(p1,p2):
    #F2上多项式相加
    
    p=[0]*len(p1)
    for k in range(len(p1)):
        p[k]=(p1[k]+p2[k])%2
        
    return p

def PolyMulti(p1,p2):
    #F2上多项式相乘
    p=[0]*(len(p1)+len(p2)-1)
    for k in range(len(p)):
        for i in range( 0,min(len(p1),k+1)   ):
            j=k-i
            if j<len(p2):
#             for j in range(len(p2)):
#                 if i+j==k:
                p[k]+=p1[i]*p2[j]
        p[k] %=2
    
    #模不可约多项式mx=1+x+x**3+x**4+x**8
    mp=[1,1,0,1,1,0,0,0,1]
    p,q= PolyMod(p,mp)
    return p

def PolyMod(x,y):
    #x多项式对y多项式的模，x=q*y+r，得到商q和余r
    
    p=list(x)
    p2=list(y)
    
    if p2[0]==1 and (not any(p2[1:])):
        return ([0,0,0,0,0,0,0,0],p)

    quot=[0]*8
    p2Len=1
    for k in range(len(p2)):
        if p2[k]:
            p2Len=k+1
    for k in range(len(p)-1,p2Len-2,-1):
        if p[k]:
            quot[k-p2Len+1]=1
            for i in range(p2Len):
                p[k-p2Len+i+1]+=p2[i]
                p[k-p2Len+i+1] %=2
    p.extend([0]*8)
    p=p[0:8]
    for k in range(len(p)):
        p[k] %=2
    
    #p为余，quot为商
    return (p,quot)
                
def PolyInv(p):
    #F2多项式的逆，采用欧几里得算法，辗转相除
    #ap+bm=1，则a为p的逆
    #
    
    mp=[1,1,0,1,1,0,0,0,1]
    
    xk=mp
    yk=p
    
    #xk,yk,rk表示为mp和p的组合系数
    xkPoly=[[1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    ykPoly=[[0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]
    rkPoly=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    
    while True:
        #辗转相处
        rk,qk=PolyMod(xk,yk)
        #余项为0
        if not any(rk):
            break
        
        #计算余项对应的mp,p的组合多项式
        rkPoly=[None,None]
        rkPoly[0]=PolyAdd(xkPoly[0],  PolyMulti(qk, ykPoly[0])      )
        rkPoly[1]= PolyAdd(xkPoly[1],   PolyMulti(qk, ykPoly[1])      )
        
        #进行下一次相除
        xk=yk
        yk=rk
        xkPoly=ykPoly
        ykPoly=rkPoly

    return rkPoly[1]
    

    
       
def GetManyElements(num):
    #得到随机的num个多项式,不能是0多项式
    
    polys=[None]*num
    indexs=[random.randint(1,2**8-1) for k in range(num)]
    #indexs=random.sample(range(2**8),num)
    for k in range(num):
        index=indexs[k]
        #将数字转换为对应的多项式
        polys[k]=Num2Poly(index)
    return polys


def Num2Poly(n):
    #将数字转换为对应的多项式
    poly=[0]*8
    for k in range(8):
        if n %2:
            poly[k]=1
        n =int(n/2)
    return poly



if __name__ =="__main__":
    #测试脚本
    p1=[1,1,0,1,1,0,0,0]
    p2=[1,1,0,1,0,0,0,0]
    print 'p1=',p1
    print 'p2=',p2
    print 'p1+p2=',PolyAdd(p1, p2)
    print 'p1*p2=',PolyMulti(p1, p2)
    
    invP=PolyInv(p2)
    print 'P2的逆:', invP
    print 'p2*invp2=',PolyMulti(p2,invP)





