n=int(input())
a=[]
lst=[]
for i in range (0,n,1):
    x=int(input())
    a.append(x)
for i in range (0,n,1):
    lst.append(1)
print(a)
for i in range (0,n,1):
    for k in range (0,i,1):
        if a[k]<a[i]:
            lst[i]=max(lst[i],lst[k]+1)
x=lst[0]
print(lst)
for i in range(0,n,1):
    if lst[i]>x:
        x=lst[i]
print(x)
h=1
b=0
kq=[]
while h<=x:
    if lst[b]==h:
        h+=1
        kq.append(a[b])
        b+=1
    else:
        b+=1
print(kq)