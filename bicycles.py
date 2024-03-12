bicycles = ['trek','cannondale','redline','spcialized']
print(bicycles)
print(bicycles[-3].title())
print(bicycles[-1].title())
message = f"bicycle was a {bicycles[0].title()}.!!!!"
print(message)
motorcycles=['honda','ducati','yamaha','suzuki','ducati']
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
#motorcycles.remove('ducati')
#motorcycles[0]='ducati'
print(motorcycles)
#motorcycles[-1]='kia'
motorcycles.append('GM')
print(motorcycles)
motorcycles.insert(1,'Samcheonri')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles.pop()
print(motorcycles)
popped_motor=motorcycles.pop()
print(motorcycles)
print(f'the last owned motor was a {popped_motor.title()}')