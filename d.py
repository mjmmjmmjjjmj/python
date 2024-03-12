#a, b = map(int, input().split())
#print(a+b)

#a, b= map(int, input().split())
#print(a+b, a-b, a*b, a//b, a%b)

#이거는 됨
#for i in [1, 2, 3, 4, 5]
#print(i)

#이거도 됨for s in range(1, 6) :
    #print(s)

for i in range(1, 6):
    if (i % 2 == 0) :
        print(i, '2')
    elif(1 %3 ==0):
        print(i, '3')
    elif(1%4==0) :
        print(i, 4)
    else:
        print('unknown')

