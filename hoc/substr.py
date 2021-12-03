A=input()
B=input()
HA=[]
HB=[]
base=1000000007
M=[1]
for i in range(1,len(A)+10):
    M.append((M[i-1]*43)%base)
def buildHash(k,C):
    C.append(0)
    '''
    for i in range(len(k)+10):
        C.append(0)'''
    for i in range(1,len(k)+1):
        C.append(0)
        C[i]=(43*C[i-1]+ord(k[i-1]))%base
buildHash(A,HA)
buildHash(B,HB)
def getHash(L,R,C):
    return((C[R]-C[L-1]*M[R-L+1])%base)
for i in range(1,len(A)-len(B)+2):
    if getHash(i,i+len(B)-1,HA)==HB[len(B)]:
        print(i,end=" ")


