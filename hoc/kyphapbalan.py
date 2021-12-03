import re
top_stack=-1
top_queue=-1
stack=[]
queue=[]
def isEmptyStack():
    if top_stack==-1:
        return True
    else:
        return False
def pushStack(x):
    global top_stack
    top_stack=top_stack+1
    stack.append(0)
    stack[top_stack]=x
def popStack():
    global top_stack
    stack[top_stack]=0
    top_stack-=1
def getTopStack():
    global top_stack
    return stack[top_stack]
def isEmptyQueue():
    global top_queue
    if top_queue==-1:
        return True
    else:
        return False
def pushQueue(x):
    global top_queue
    top_queue+=1
    queue.append(0)
    queue[top_queue]=x
def popQueue():
    global top_queue
    queue[top_queue]=0
    top_queue-=1
def getTopQueue():
    global top_queue
    return queue[top_queue]
def getQueue():
    global lst
    lst=[]
    for i in range (len(queue)):
        lst.append(queue[i])
    return lst
def switchQtoS():
    if getTopStack()!="(":
        pushQueue(getTopStack())
        popStack()
        return switchQtoS()
    else:
        popStack()
        return 
def Priority(n):
    if n=="*"or n=="/":
        return 2
    elif n=="+" or n=="-":
        return 1
    else: 
        return 0
def checkPriority(n,k):
    if Priority(n) >=Priority(k):
        return 1
    else:
        return 0
def cong(a,b):
    return a+b
def tru(a,b):
    return(a-b)
def nhan(a,b):
    return(a*b)
def chia(a,b):
    c=a/b
    return c
n=input()
nlist=[]
for i in range(len(n)):
    nlist.append(n[i])
j=0
i=0
while j<len(n):
    if nlist[i].isdigit()== True and nlist[i+1].isdigit() ==True:
        nlist[i]=nlist[i]+nlist[i+1]
        nlist.pop(i+1)
        j+=1
    else:
        i+=1
        j+=1
print(nlist)

for i in range (len(nlist)):
    if nlist[i].isdigit() == True :
        pushQueue(int(nlist[i]))
        nlist[i]=0
    else:
        pushStack(nlist[i])
        nlist[i]=0
        if getTopStack()==")":
            popStack()
            switchQtoS()
        if "(" not in stack:
            if top_stack>=1:
                if Priority(stack[top_stack-1])==2:
                    pushQueue(stack[top_stack-1])
                    stack.pop(top_stack-1)
                    top_stack-=1
        elif "(" in stack:
            if Priority(stack[top_stack-1])==2 and stack[top_stack]!="(":
                pushQueue(stack[top_stack-1])
                stack.pop(top_stack-1)
                top_stack-=1
while top_stack!=-1:
    pushQueue(stack[top_stack])
    popStack()
print(top_stack)
getQueue()
mang=[]
print(lst,stack)
for i in range(len(lst)):
    mang.append(lst[i])
    if lst[i]=="+":
        a=cong(mang[-3],mang[-2])
        mang[-3]=a
        del mang[-2:]
    if lst[i]=="-":
        a=tru(mang[-3],mang[-2])
        mang[-3]=a
        del mang[-2:]
    if lst[i]=="*":
        a=nhan(mang[-3],mang[-2])
        mang[-3]=a
        del mang[-2:]
    if lst[i]=="/":
        a=chia(mang[-3],mang[-2])
        mang[-3]=a
        del mang[-2:]
print(mang[0])