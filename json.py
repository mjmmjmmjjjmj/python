
# import json 
# #import pickle
# # 아니 진심 뭐라고 하는 거임 적어도 똑같은 에러가 떠야 하는데 저기서는 신택스 여기서는 타입 에러 나고 있잖음
# # print(type(json.dumps(['foo', {'bar' : ('baz', None, 1.0, 2)}])))
# # print(type(json.loads(['foo', {'bar' : ('baz', None, 1.0, 2)}])))

# data = json()
# type(data) # json

# data = json.parse ("{'name':'kim', 'age': 22}")
# type(data) #jason
# print(data.name) #1
# print(data.age) #2

# # import json
# # print(type(json.dumps({'4': 5, '6': 7})))
# json.dumps("{'name':'kim, 'age':22}")
# json.loads("{'name':'kim, 'age':22}")


import json 

def to_json(data_str):
    return json.loads(data)

data = '{"name", : "Kim", "age" : "23}'
# member = {"name": "Lee", "age" : "24"}
data.json = to_json(data_str)

# with open('member2.json' , 'w') as w_file:
#     json.dumpe(data, w_file)

with open('member2.json' , 'r') as r_file:
    d = json.load(r_file)
    print(d, type(d))

d2 = json.dumps(member)
print(d2, type(d2))

d3 = json.loads(d2)
print(d3, type(d3), d3["name"])

import pickle 

data = [1, 2, 3, 4, 5]
with open('dump_member.pk', 'wb') as w_file:
    pickle.dump([1, 2, 3, 4, 5], w_file)

# with open('dump_member.pk', 'rb') as r_file:
#     pickle.load('dump_member.pk')

with open('dump_member.pk', 'rb') as r_file:
    d5 = pickle.load('dump_member.pk')
    print(d5)

# 시바 진짜 따라갈 시간도 안 줘 코드도 안 올려줘 뭘 보고 어떻게 하라는 거임
# 오류가 나면 맞는 코드 보고 왜 틀렸는질 알아야 할텐데 걍 혼자 신남