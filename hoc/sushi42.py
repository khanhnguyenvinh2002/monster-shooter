def dodai(l,r,i):
    ans=0
    while l<=r:
        mid= (l+r)//2
        if mid<=i:
            if tong[i]-tong[mid-1]==(i-mid+1)*int(a[i]):
                r=mid-1
                ans=max(ans,(i-mid+1))
            else:
                l=mid+1
        else:
            if tong[mid]-tong[i]==(mid-i)*int(a[i+1]):
                l=mid+1
                ans=max(ans,(mid-i))
            else:
                r=mid-1
    return ans
tong=[0]
n, a = int(input()), input().split()
daymax=0
a.insert(0,0)
for i in range (1,n+1,1):
    tong.append(tong[i-1]+int(a[i]))
for i in range (1,n,1):
    if a[i]!=a[i+1]:
        daymax=max(daymax,2*min(dodai(1,i,i),dodai(i+1,n,i)))
print(daymax)
    