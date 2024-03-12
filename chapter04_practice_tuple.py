
###8-9 일련의 짧은 문자메시지를 포함하는 리스트를 만드세요.
    ### 이 리스트를 show_message()함수에 전달해 각 메시지를 출력하세요
### 8-10 위(8-9)의 프로그램으로 시작함. send_message 함수를 수정해서 출력한 
    ###메시지를 sent_message 리스트로 이동하세요. 함수를 호출 후 두 리스트를 
    ###모두 출력해 메시지가 정확히 이동했는지 확인하세요
### 8-11 위(8-10)의 프로그램으로 시작. send_message()함수를 호출할 때 메시지
    ###리스트 사본을 전달하세요 함수 호출 후 두 리스트를 모두 출력해 
    ###리스트 원본 그대로인지 확인

#8-9

#def show_message(send_messages, sent_messages):
#    """빈 리스트일 때까지 출력"""

def send_messages(unsent_messages, sent_messages) :
    """남은 거 없을 때까지 메시지 출력
    출력 끝나면 sent_messages로 이동"""
    while unsent_messages:
         current_message = unsent_messages.pop()
         print(f"sending message : {current_message}.")
         sent_messages.append(current_message)
 
unsent_ones = ['going', 'home', 'for goods']
sent_messages = []
print(unsent_ones)

send_messages(unsent_ones, sent_messages)

def show_sent_messages(sent_messages) :
    print ("\nThe following messages have been sent,")
    for sent_message in sent_messages:
        print(sent_message)
    unsent_ones = ['going', 'home', 'for goods']
    sent_messages = []

print("\nThe following messages have been printed : ")
for sent_message in sent_messages :
    print(sent_message)

# def show_sent_messages(sent_messages):
#         print("\nThe following messages have been sent,")
#         for sent_message in sent_messages:
#             print(sent_message)
#         unsent_ones = ['going', 'home', 'for goods']
#         sent_messages = []

#         send_messages(unsent_ones, sent_messages)
#         show_sent_messages(sent_messages)
        
# print("\nThe following messages have been printed : ")
# for sent_message in sent_messages :
#     print(sent_message)
    


def build_profile(first, last, **user_info) : 
    """사용자 dictionary"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                             location='princeton', 
                             field = 'physics')
print(user_profile)


    