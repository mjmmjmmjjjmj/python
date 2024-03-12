# with open('0308name.txt')as file:
#     for line in file : 
#         print(line.rstrip())

# # def add(a, b) :
# #     return a+b

# # print(add(1, 2))
# # print('A', 'B', 'C', sep=', ')
# # # print('B', end='\n')


import csv # grade.csf 불러옴

with open('0308grade.csv') as file:
    reader = csv.reader(file)
    header = next(reader)    
    for line in reader:
        print(line)
    print(header)


n = range(5)
print(n)
r = iter(n)
print(next(r))
print(next(r))


for i in range(5):
    print(i)