#파이썬에서 주석 : #
for value in range(6) :
    print(value)
numbers = list(range(1, 10, 2))
print(numbers)
number_set = {}

squares = []
for value in range(1, 11):
    #square = value ** 2
    squares.append(value ** 2)
print(squares)
#print(value) 

squares = [value ** 2 for value in range(1,11)]# list comprehension
print (squares)
print(squares[-3:])#slicing squares[0:3] = 0,1,2

a = [1, 2, 3, 4]
b = [3, 4]
#c = a - b #에서
c1=[x for x in a if x not in b]
c2=list(set(a)-set(b))
print(c1)
print(c2)


a = [10, 20, 30, 40, 50]
#b = a # b = a ### shallow copy 
b = a[0:3] ###deep copy
a[0] = 100
print(b)
# my_list {::-1} :: -> 2칸씩


a = [[1, 2, 3], [4, 5, 6]]
b = a[:] #shallow copy (list 자체를 copy하지 않으면 shallow)
print(b) #[[1, 2, 3], [4, 5, 6]]
a[0][0] = 100
print (b)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players [:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
#friend_foods = my_foods[:] #deep copy
friend_foods = my_foods #shallow copy
my_foods.append('cannoli')
#friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


dimensions = (10, 20, 30, 40, 50)
#dimensions[0] = 30
print(dimensions)
for dimension in dimensions :
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print (dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)