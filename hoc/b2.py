n=int(input())
k=0
def sum(n):
    summ=0
    while n>0:
        summ+=n%10
        n//=10
    return summ
for i in range (0,14,1):
    if n<10**i:
        k=i
        break
a=10**(k-1)-1
l=0
for i in range (1,10,1):
    if n<i*(10**(k-1))+a:
        l=i-1
        break
h=n-(l*(10**(k-1))+a)
a=sum(h)
print((9*(k-1))+l+a)

'''

def sum(n):
    i=12
    k=0
    while i>0:
        k+=n%(10)
        n=n//10
        i-=1
    return k
x=sum(n)
for i in range (0,n+1,1):
    if (sum(n-i)+sum(i))>x:
        x=(sum(n-i)+sum(i))
print(x)
'''