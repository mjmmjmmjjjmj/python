#입출력과 사칙연산
#2557 : Hello World
print("Hello World!")
       
# 1000, 10869 : A+B, 사칙연산
A, B=input().split()
A= int (A)
B= int (B)
print(A+B)
print(A-B)
print(A*B)
print(A//B) 
#/는 나누기 연산자, //는 정수 나누기 연산자-> 몫 구할 때는 //
print(A%B)

# 조건문
# 1330 두 수 비교하기
A, B = input().split()
A= int (A)
B= int (B)
if A > B : print(">")
elif A < B : print("<")
else : print ("==")

#9498 시험 성적
x = input()
x = int(x)
# x = int(x) <=100 여기서 <=100 없어야 하나봄
if 90<=x<=100 : print("A")
elif 80<=x<=89 : print("B")
elif 70<=x<=79 : print("C")
elif 60<=x<=69 : print("D")
else : print("F")

#반복문 : 구구단, 합
#2739 구구단 
n = int(input())
1<=n<=9
for i in range(1, 10):
    print (n, '*', i, '=', n*i)

#8393 합
n = int(input())
# 1<=n<=10000
total_sum = 0
for i in range (1, n+1) :
    total_sum += i
    
print(total_sum)

#1차원 배열 10807, 10871, 10818, 3052 
# 10807 개수 세기

n = int(input())
count = 0
for v in range (-100, 101) :
    if v < n : 
        count += 1
print(count)

# 10871 X보다 작은 수
# map(함수, iterable 데이터)

N, X = map(int, input().split())
A = list(map(int, input().split()))

result = []
for num in A :
    if num < X :
        result.append(num)

for item in result : 
    print(item, end = ' ')
# 10818 최소, 최대

N = int(input())
numbers = list(map(int, input().split()))

min_value = numbers[0]
max_value = numbers[0]

for num in numbers :
    if num < min_value:
        min_value = num
    if num > max_value :
        max_value = num

print(min_value, max_value)

# 3052 나머지
fools = {}  # 빈 딕셔너리 fools 생성. 나머지와 해당 나머지의 개수 저장됨.
for _ in range(10):  # 10번 반복하는 반복문. 입력값에서 10개의 숫자 받음.
    num = int(input())  # 정수를 입력받음.
    fool = num % 42  # 입력값%42 계산 -> fool 변수에 저장.
    if fool in fools:  # 현재 나머지가 이미 fools 딕셔너리에 있다면,
        fools[fool] += 1  # 해당 나머지의 개수를 1 증가시킴.
    else:  # 그렇지 않으면,
        fools[fool] = 1  # 새로운 나머지를 딕셔너리에 추가, 개수를 1로 초기화.

count = 0  # 서로 다른 나머지의 개수를 세기 위한 변수 count를 초기화합니다.
for value in fools.values():  # 딕셔너리의 값들을 반복하면서,
    if value > 0:  # 값이 0보다 크면 (나머지가 하나 이상 나온 경우)
        count += 1  # count 변수를 1 증가시킵니다.

print(count)  # 최종적으로 서로 다른 나머지의 개수를 출력합니다.




# 문자열 - str 2675, 1152
# 2675 문자열 반복
# 1152 단어의 개수

# 집합과 맵 - dictionary 10815, 14425
# 10815 숫자카드
# 14425 문자열 집합

# #dictionary
# answer = []
# for d in data : 
#     if d not in answer : 
#         answer.append(d)
# print(len(answer))






    
# #------------------------
n = input()
n = int(n)

db = map(int, input().split)
print(dict(list(zip((db, list(rang(n)))))))

m = int(input())

query = list(map(int, input().split()))
print(query)

for q in query:
    if q in db:
        print(1, end=' ')
    else: 
        print(0, end='dbdbdb')

# db = dict()
# for _ in range(n):
#     db[int(input)]=1

# n = int(input())

# query = dict()
# for _ i in range(m) :
#     query[int(input())]=1