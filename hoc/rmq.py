import math
n,q=input().split(' ')
n=int(n)
q=int(q)
rmq=[]
rmq2=[]
a=[]
def minUV(u,v):
    u-=1
    v-=1
    k=int(math.log2(v-u+1))
    return min(rmq[u][k],rmq[v-(1<<k)+1][k])
def maxUV(u,v):
    u-=1
    v-=1
    k=int(math.log2(v-u+1))
    return max(rmq2[u][k],rmq2[v-(1<<k)+1][k])
for i in range (0,n,1):
    x=int(input())
    a.append(x)
LogN=int(math.log2(n))+3
for i in range (0,n+10,1):
    tmp=[]
    for j in range (0,LogN,1):
        tmp.append(0)
    rmq.append(tmp)
for j in range (0,LogN,1):
    for i in range (0,n,1):
        if j==0:
            rmq[i][j]=a[i]
        elif i+(1<<j) -1 <=(n-1):
            rmq[i][j]=min(rmq[i][j-1],rmq[i+(1<<(j-1))][j-1])
    
for i in range (0,n+10,1):
    tmp=[]
    for j in range (0,LogN,1):
        tmp.append(0)
    rmq2.append(tmp)
for j in range (0,LogN,1):
    for i in range (0,n,1):
        if j==0:
            rmq2[i][j]=a[i]
        elif i+(1<<j) -1 <=(n-1):
            rmq2[i][j]=max(rmq2[i][j-1],rmq2[i+(1<<(j-1))][j-1])
o=[]
for i in range (0,q,1):
    u,v=input().split(' ')
    u=int(u)
    v=int(v)
    print(maxUV(u,v)-minUV(u,v))
