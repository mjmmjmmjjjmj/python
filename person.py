from typing import Any


class Person:
    count = 0 ### 클래스 변수
    def __init__(self, name, age, address) : # 생성자 역할
        self.name = name ### 인스턴스 변수
        self.age = age 
        self.address = address
        self.weight = [65, 67, 70, 71] # 공개 속성
        self.height = 170 #private 속성
        self.__vision = 1.0 
        print("{}객체가 생성됨".format(self.name))
        Person.count += 1 ###클래스 변수를 증가 
    @classmethod ###decorator - 자바 용어는 annotation
    def printing(cls):
        print("객체수는 {}".format(cls.count))

    def __getitem__(self, indx) :
        return self.weight[indx]
    def __del__ (self) :
        print("객체 {}이 소멸됨".format(self.name))

    # def __call__(self) :
    #     return self.weight/self.height **2
    
    # def __len__(self):
    #     return len(self.weight)
    
    def __str__(self): #Person은 객체 출력 시 필요한 건 String
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    
    def show_person_vision(self) :
        print("시력은 {}".format(self.__vision))
    
    def __eq__(self, other) :
        return self.address == other.address

Person('guest', 11, 'jeju')
   
new_person = Person('hong', 20, 'busan')
other_person = Person('kim', 30, 'busan')
Person.printing() ###클래스 메소드 호출
new_person.printing()
print(f"person 객체의 나이는**{new_person.age:5}***") #5칸 띄워서 출력하는지 보려는 거임
print("왼쪽이 오른쪽의 저게 맞는지 {}".format(isinstance(new_person, Person)))
print("객체의 타입은 {}".format(type(new_person)))
print(f"현재 체중은 {new_person[2]}")
print(f"{other_person.count} 객체가 생성됨")
###Person, new_person, other_person 다 해봐도 3객체가 생성됨
###위에서 Person.count +=1로 해서 Person 객체들이 가진 Person의 값을 공유해서 그걸 다 세는 듯

# print(f"체질량은 {new_person()}") ###__call__() 함수가 호출
print(new_person == other_person)
print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight}")
#print("시력은 {}".format(new_person.__vision))
#new_person.show_person_vision()
    
print(new_person.__str__())
print(new_person)

# print(f"리스트 길이{len(new_person)}")

# my_list=[1,2,3,4,5]
# print(len(my_list))

# garbage collector