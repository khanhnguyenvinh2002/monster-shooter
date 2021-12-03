t=int(input())
canh1=[]
canh2=[]
for i in range (0,t,1):
    a,b=input().split(' ')
    a=int(a)
    b=int(b)
    canh1.append(a)
    canh2.append(b)
for i in range (0,t,1):
    if 2*canh1[i]>=canh2[i] and 2*canh2[i]>=canh1[i]:
        print(min((canh1[i]**2)*4,(canh2[i]**2)*4))
    elif 2*canh1[i]<=canh2[i]:
        print(canh2[i]**2)
    elif 2*canh2[i]<=canh1[i]:
        print(canh1[i]**2)
