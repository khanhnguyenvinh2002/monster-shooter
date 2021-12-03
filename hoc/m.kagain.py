T=int(input())
for i in range(T):
    t=int(input())
    N=input().split()
    N.insert(0,0)
    n=len(N)-1
    for i in range(len(N)):
        N[i]=int(N[i])
    num=[]
    L=[]
    R=[]
    for i in range (0,len(N)+10,1):
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
    print(mx,L[pos]+1,R[pos]-1)
        
        