M,N=input().split()
M=int(M)
N=int(N)
lst=[]
toida=0
for i in range(M):
    x=input().split()
    lst.append(x)
    if i>0:
        for j in range(N):
            if int(lst[i-1][j])==0:
                if int(lst[i][j])==1:
                    lst[i][j]=1
                else:
                    lst[i][j]=0
            else:
                if int(lst[i][j])==0:
                    lst[i][j]=0
                else:
                    lst[i][j]=int(lst[i-1][j])+1
for i in range(M):
    N=lst[i]
    N.insert(0,0)
    n=len(N)-1
    for i in range(n+1):
        N[i]=int(N[i])
    num=[]
    L=[]
    R=[]
    for i in range (0,n+11,1):
        L.append(0)
        R.append(0)
    stck=[]
    size=0
    for i in range (1,n+1,1):
        if size==0:
            L[i]=0
        else:
            while  size>0 and N[stck[size-1]]>=N[i]:
                del stck[size-1]
                size-=1
        if size > 0:
            L[i]=stck[size-1]
        stck.append(i)
        size+=1
    stck2=[]
    size=0
    for i in range (n,0,-1):
        if size==0:
            R[i]=n+1
        else:
            while size>0 and N[stck2[size-1]]>=N[i]:
                del stck2[size-1]
                size-=1
        if size > 0:
            R[i]=stck2[size-1]
        if size==0:
            R[i]=n+1
        stck2.append(i)
        size+=1
        
    pos=0
    mx = 0
    for i in range(1,n+1,1):
        if N[i]*(R[i]-L[i]-1) == mx:
            if L[i]<L[pos]:
                pos = i
        if N[i]*(R[i]-L[i]-1)>mx:
            mx = N[i]*(R[i]-L[i]-1)
            pos = i
    if mx>toida:
        toida=mx
print(toida)
