def test():
    return (10, 20)

a, b = test(); #tuple 값을 return
print(f"a = {a}, b = {b}")
lst = ['a', 'b', 'c', 'd']
for i, value in enumerate(lst): 
    # enumerate() 험수가 tuple을 리턴함
    # enumerate는 return값이 tuple임 근데 tuple이 뭐임
    # print(f"i = {i}, value = {value}")

    # def get_formatted_name(first_name, last_name):
    #     """실제이름반환"""
    #     full_name = f"{first_name}{last_name}"
    #     return full_name.title()
    
    # while true:
    #     print("\n print your name")
    #     f_name = input("first name: ")
    #     l_name = input("last name:")
    #     formatted_name = get_formatted_name(f_name, l_name)
    #     print(f"\n hello {formatted_name}!")

    def print_models(unprinted_designs, completed_models):
        #리스트가 parameter면 
        """빈 리스트일 때까지 출력"""
        while unprinted_designs: #빈리스트이면 false
            current_design = unprinted_designs.pop() # 한개씩 삭제됨
            print(f"printing : {current_design}")
            completed_models.append(current_design)
    
    def show_completed_models(completed_models):
        print("\nThe following models have been printed.")
        for completed_model in completed_models:
            print(completed_model)
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)

    def modify_string(s): ##스트링 값을 전달받음
        ###immutable 변수는 튜플, 숫자, 스트링, 불리언 
        s = s + "world" ## 변수 s는 원래 변수가 가리키는 주소와 다름
        print(s)

    st = "hello "
    modify_string(st)
    print(st) # 출력결과는 hello -> 변경안됐음