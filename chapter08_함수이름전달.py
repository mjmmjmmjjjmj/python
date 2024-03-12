# # 함수의 매개변수로 함수 정달하기
# def ten_times(fund) :
#     for i in range(5):
#         func()

# def print_hello():
#     print("hello")

# ten_times(print_hello)

# def print_work():
#     print("coding")

# ten_times(print_work)

# def add(x,y):
#     return x+y

# def minus(x,y):
#     return x-y

# def apply_operation(opration, x, y): ### map() 함수 역할
#     return opration(x,y)

# result = apply_operation(add, 3, 4)
# result2 = apply_operation(minus, 3, 4)



### map(), filter() 함수 사용
def power(item):
    return item * item

def under_three(item):
    return item < 3

### 람다식
# power = lambda x: x*x
# under_three = lambda x: x < 3

lst = [1, 2, 3, 4, 5]

map_list = map(power, lst)
print(f"map() 함수 적용결과 : {list(map_list)}")

filter_list = filter(under_three, lst)
print(f"filter() 함수 적용결과 : {list(filter_list)}")

### 위에 주석처리 해놓은 게 오류뜸. 나중에 고쳐야함 

# Step1 : 함수 자체를 인수전달
# Step2 : apply_opration(add, 3, 4) x, y가 여기서 3, 4임 x, y 전달
# Step3 : map 사용
# Step4 : 람다식 사용