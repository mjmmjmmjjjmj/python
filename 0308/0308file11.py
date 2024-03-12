import os

from pathlib import Path

path = Path ('./a/a.txt')
print(path)

dir_path = Path( './a')
print(dir_path)

file_path = Path('./a/a.txt')
print(file_path)

print(os.path.isdir(dir_path))
print(os.path.isdir(file_path))

# for d in os.listdir():
#     print(d, os.path.isdir(d))
#     if '.txt' in d:
#         print('Found!')

no_file = Path ('./a/b.txt')
print(os.path.exists(no_file))
print(no_file.exists())

print(os.path.split(Path('./a/b.txt')))
# ['.', 'aaa', 'b.txt']
print(Path('aaa', 'b.txt'))


# top=Path('.')
# for root, dirs, files in top.walk (top_down=False) :
#     for name in files:
#         (root/name).unlink()
#     for name in dirs:
#         (root/name).rmdir()


path = Path('./0308/a/a.txt')

with open(path, 'a') as file:
    file.write('a\n')
    file.write('aa\n')
    file.write('aaa\n')
    file.write('aaaa\n')

# if path.exists():
#     with open(path) as file:
#         for line in file:
#             print(line)
# try : 
#     with open(path) as file:
#         for line in file:
#             print(line)
# except Exception as e:
#     pass
#     print (e)


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



