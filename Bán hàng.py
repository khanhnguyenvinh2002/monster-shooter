Cart=[]
name =[]
giaTien=[]
theLoai=[]
soLuong=[]
xuatXu=[]

fName=open("name.txt","r")
a=int(fName.readline()) # DOc so luony item trong file
for i in range (a):    
    name.append(fName.readline())#doc tung dong du lieu
fgiaTien=open("giaTien.txt","r")
b=int(fgiaTien.readline()) # DOc so luony item trong file
for i in range (b):    
    giaTien.append(int(fgiaTien.readline()))
ftheLoai=open("theLoai.txt","r")
c=int(ftheLoai.readline()) # DOc so luony item trong file
for i in range (c):    
    theLoai.append(ftheLoai.readline())
fxuatXu=open("xuatXu.txt","r")
d=int(fxuatXu.readline()) # DOc so luony item trong file
for i in range (d):    
    xuatXu.append(fxuatXu.readline())
fsoLuong=open("soLuong.txt","r")
e=int(fsoLuong.readline()) # DOc so luony item trong file
for i in range (e):    
    soLuong.append(int(fsoLuong.readline()))

# 1 Them du lieu trong cac file, sao cho co khoang 10 mat hang
# 2 Chay lai tat ca cac case co the co cua project
while True :
    print('''
    ==================== mart ===================
    1. Check the list of products
    2. Find information of the product by name
    3. Find information of the product by category
    4. Find information of the product by maximum price
    5. Muc nguoi ban hang
    ''')
    choice = int(input('select your number : '))
    a=0
    xnmh=0
    while choice == 1 :
        print('''
    press X to go back
    press C to continue''')
        for i in range(len(name)):
            print('id',i+1,':',name[i])
        a= input('Do you want to go back or buy : ')
        if a== 'X'or a== 'C':
            break  
    while choice == 2:#thu 1 bi sai
        print('''
    press X to go back
    press C to continue''')
        for i in range(len(name)):
            print('id',i+1,name[i])
        nameP = int(input(" insert number: "))
        for i in range(len(name)):
            if nameP==i:
                print('category: ',theLoai[i],", amount left: ",soLuong[i],", each product costs: ",giaTien[i],", made in: ",xuatXu[i])
        a= input('Do you want to go back or continue: ')
        if a== 'X' or  a== 'C':
            break
    while choice == 3:
        print('''
    press X to go back
    press C to continue''')
        print('''
    1.  food
    2.  drink
    3.  stationary
    4.  x
    5.  y
    6.  z
    7.  t
    8.  m
    9.  n
    10. p''') 
        theLoaiP = int(input("insert number: "))
        listT=[" ","food","drink","stationary","x","y","z","t","m","n","p"]
        for i in range (len(theLoai)):
            k = len(theLoai[i])
            for j in range(0,k):
                if listT[theLoaiP] == theLoai[i][j]:#co bi sai
                    print(name[i],' ',soLuong[i]," ",giaTien[i]," ",xuatXu[i])
        a= input('Do you want to go back or continue: ')
        if a== 'X' or a== 'C':
            break
    while choice == 4:
        print('''
    press X to go back
    press C to continue''')
        tien= int(input('insert the maximum amount of money :'))
        for j in range(len(giaTien)):
                if giaTien[j]<=tien:
                    print(name[j])
        a= input('Do you want to go back or continue: ')
        if a== 'X' or a== 'C':
            break
    if a=='C':
        print("Which product do you want to buy? insert the id: ")
        ide=int(input())
        print(soLuong[ide-1],'products left')
        sl=int(input('Input number of products you want to buy: '))
        if sl>int(soLuong[ide-1]):
            print('not enough products, try again')
        else:
            print('You will buy ',soLuong[ide-1],name[ide-1],' with a total cost of ',giaTien[ide-1]*sl,('. Do you want to buy more?','(press y to print the receipt)'))
            soLuong[ide-1]=soLuong[ide-1]-sl
            if sl!=0:
                temp=[]
                temp.append(sl)
                temp.append(name[ide-1])
                temp.append(giaTien[ide-1])
                Cart.append(temp)
            else:
                print('This buy will be deleted due to 0 product selected')
            xnmh =input('Do you want to buy more or continue: ')
            if xnmh=='y':
                print("Seller insert the code :")
                ma=input()
                if ma=='dunglanhuvay':
                    
                    print('Complete!')
                    print()
                    print('{:=^40}'.format("mart"))
                    print('{:<10}'.format('Name'),'{:<10}'.format("Amount",'{:<10}'.format("Unit price"),'{:<10}'.format("Total cost")))
                    for i in range(len(Cart)):
                        print('{:<10}'.format(Cart[i][1]),'{:<10}'.format(Cart[i][0]),'{:<10}'.format(Cart[i][2]),'{:<10}'.format((Cart[i][0])*(Cart[i][2])))
                    print('{:^15}'.format("CAM ON CAC BAN DA GHE THAM"))
                
fName.close()
fgiaTien.close()
fxuatXu.close()
fsoLuong.close()
ftheLoai.close()


