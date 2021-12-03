n=int(input())
lst=[]
a=0
for i in range (0,n,1):
    x=int(input())
    lst.append(x)
for i in range (0,n,1):
    for j in range (i+1,n,1):
        if lst[i]>lst[j]:
            a+=1
print(a)