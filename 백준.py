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
T = int(input())
1<=T<=1000
for _ in range (T) : 
    R, S = input().split()
    R = int (R)
    1<=R<=8
    P = ""
    for char in S:
        P += char * R
    print(P)

# 1152 단어의 개수
sentence = input().strip()
 # 문자열 입력 및 양쪽 공백 제거
words = sentence.split()
# 공백을 기준으로 문자열을 분리하여 단어의 리스트를 얻음
print(len(words))
# 분리된 단어의 개수를 출력

# 집합과 맵, dictionary - dictionary 10815, 14425 7785
# 10815 숫자카드

N = int(input())
1<=N<=500000
cards = list(map(int, input().split()))
# 상근이가 가지고 있는 숫자 카드의 개수 N과 숫자 카드들을 입력 받음

M = int(input())
check_numbers = list(map(int, input().split()))
# 입력으로 주어진 M개의 수의 개수 M과 M개의 수를 입력 받음

cards_set = set(cards)
# 상근이가 가지고 있는 숫자 카드를 set으로 변환하여 중복을 제거함

for num in check_numbers :
    if num in cards_set :
        print(1, end=" ")
    else :
        print(0, end=" ")
# 각 수가 숫자 카드 리스트에 있는지 확인하여 결과를 출력
        
# 14425 문자열 집합
N, M = map(int.input().split())
S = set()
for _ in range(N) :
    S.add(input())

count = 0
for _ in range (M):
    if input() in S:
        count += 1

print(count)

# 백준 버전 : 
# sys.stdin.readline().strip()는 파이썬의 표준 라이브러리인 
# sys 모듈을 사용하여 표준 입력에서 한 줄을 읽어오고 개행 문자를 제거하는 방법
# 표준 입력에서 입력을 받는 데 있어서 더욱 효율적으로 처리
# input() 함수는 파이썬의 내장 함수로, 보다 유연한 사용법을 제공하지만 
# 입력이 많은 경우에는 처리 속도가 느려질 수 있기 때문
import sys

N, M = map(int, sys.stdin.readline().strip().split())
S = set()
for _ in range(N):
    S.add(sys.stdin.readline().strip())

count = 0
for _ in range(M):
    if sys.stdin.readline().strip() in S:
        count += 1

print(count)
 
# 7785
n = int(input())
logs = []
for _ in range (n) :
    name, action = input().split()
    logs.append((name, action))

current_employees = set()
for name, action in logs : 
    if action == "enter":
        current_employees.add(name)
    else :
        current_employees.remove(name)

for employee in sorted(current_employees, reverse=True):
    print(employee)



# 정렬 - 2750, 2587, 25305
# 2750 수 정렬하기
n = int(input())
numbers = []

for _ in range(n) : 
    num = int(input())
    numbers.append(num)

numbers.sort() # 모든 수를 입력한 후에 오름차순으로 정렬
# 모든 수를 입력한 후에 내림차순으로 정렬
# numbers.sort(reverse=True)
    
for num in numbers: # 정렬된 수들을 한 줄에 하나씩 출력
    print(num)
        
# 2587 대표값2
# n = int(input())
numbers = []

for _ in range(5) :
    num = int(input())
    numbers.append(num)

numbers.sort()
# median_index = len(numbers) // 2
# median = numbers[median_index]

# print(median)

print(int(sum(numbers)/5))
print(numbers[2])



# 25305 커트라인
# 1<=n<=1000
# 1<=k<=n
# 0<=x<=10000
# n, k = input().split()
# n = int(n)
# k = int(k)
# scores_input = input().split()

# scores = []
# for score in scores_input:
#     scores.append(int(score))

# score.sort(reverse = True)

# cut_line = scores[k-1]
# print(cut_line)

n, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse=True)
print(scores[k-1])


# 10988 팰린드롬

# 1157 단어공부
# 1316 그룹 단어 체커

# 2738 행렬 덧셈


# 2566 최댓값
# 10798 세로읽기

# 수학
# 2745 진법변환
# 5086 배수와 약수
# 1978 소수찾기
# 2869 달팽이
# 1934 최소공배수

# 기타
# 24264 알고리즘 수행시간
# 2798 블랙잭
# 1018 체스판 색칠



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