A, B = input().split()
A = int(A)
B = int(B)
if (A>B) : 
    print(">")
elif (A<B) :
    print("<")
else : print("==")

A, B = input().split()
A = int(A)
B = int(B)

# A = int(input())
# B = int(input())
# print(A+B)
# print(A-B)
# print(A*B)

# 두 코드는 약간 다른 동작을 합니다.

# 첫 번째 코드인 A, B = input().split()은 입력을 
# 공백을 기준으로 나눠서 두 개의 변수에 할당합니다. 
# 이후 각 변수를 정수로 변환합니다. 
# 두 번째 코드인 A = int(input())와 B = int(input())는 
# 각각 한 줄에 하나의 값이 입력된다고 가정합니다. 
# 따라서 첫 번째 줄에서는 A에, 두 번째 줄에서는 B에 
# 값을 입력받습니다. 그 후에 각 값을 정수로 변환합니다.

# 따라서 입력 방식이 조금 다르며, 두 번째 방식은 
# 한 번에 한 변수씩 값을 입력받아야 합니다.

# 첫 번째 방식은 한 줄에 여러 값이 공백을 기준으로 
# 구분되어 있을 때 유용하고, 두 번째 방식은 각 변수에 
# 하나의 값이 입력될 때 유용합니다

# N = input()
# M = input()
# N = int(N)
# M = int(M)
N, M = map(int, input().split())
print(abs(N-M))
# abs : 절댓값

A = int(input())
B = int(input())

