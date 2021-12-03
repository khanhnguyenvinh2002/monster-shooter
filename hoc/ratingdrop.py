import math
for _ in range(int(input())):
    a,b = input().split()
    a=int(a)
    b=int(b)
    n=max(a,b)
    k=min(a,b)
    if n==k:
        print(0)
        continue
    elif n%2==1:
        print(-1)
        continue
    
    elif n%k!=0:
        print(-1)
        continue
    else:
        l=0
        while n/k>1:
            if n<=k:
                break
            if n%k==0:
                if (n/k)%2==0:
                    n=n/2
                    l+=1
                else:
                    l=0
                    print(-1)
                    break
            else:
                l=0
                print(-1)
                break
        if l==0:
            continue
        elif l%3==0:
            print(l//3)
            continue
        else:
            print(l//3+1)
            continue