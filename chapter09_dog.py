class Dog:
    """개 클래스"""

    def __init__(self, name, age) :
        """ name과 age 속성 초기화"""
        self.name = name  # 속성 > 자바의 클래스 field
        self.age = age
        self.price = 100

    def sit(self) :
        """앉기"""
        print(f"{self.name} is 앉기")

my_dog = Dog('Willie', 6) # 생성자 호출 > 인ㅇ스턴스 생성 > __init__() 함수가 자동 호출
# __init__ : 특별의미 부여함. 
# self : 생성된 객체 자기자신0
my_dog.sit()
print(f"개이름은{my_dog.name} + {my_dog.price}")
your_dog = Dog('Lucy', 3)
your_dog.sit()
print(f"너의 개는 {your_dog.name}")



# 1. 클래스 이름 : 대문자
# 2. document string : 한 줄/ 한 칸씩 떼주기


