def greet_user(username):
    """인사말"""
    print(f"hello, {username.title}")
    username = 'kim'

input_name = 'jesse'
greet_user(input_name) # 함수호출
input_name = 'kim' ### 값을 변경시킨 게 아니라 변수를 다시 설정하는 거임
print(input_name)
#help(greet_user)
#print(greet_user.__doc__)

def describe_pet(pet_name, animal_type="dog"): 
    ###animal_type="dog"디폴트 parameter
    ###(특정한 값을 입력하지 않을 때 쓰고자 하는 거. 
    ###구문 앞쪽이 아니라 마지막 뒤쪽에 써야 함)
    """반려동물 표시"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

###describe_pet() 이렇게 적으면 positional argument 정확해야 한다고 에러남
describe_pet('hamster', 'harry')
### 순서대로 안 적게 됐을 때는 이름 다 붙여줘야 함.
describe_pet(pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


def get_formatted_name(first_name, last_name, middle_name='') :
        """실제 이름을 깔끔한 형식으로 반환"""
        if middle_name: #빈 스트링이명 false로 간주
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {last_name}"
        return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
#오타 잘 확인하기 -랑 =랑 특히 주의



