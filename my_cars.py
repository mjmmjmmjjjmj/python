#from module_name import *
###잘 사용하지 않음

import car as c #파일을 import하는 경우
#import numpy as np

my_mustang = c.Car("ford", "mustang", 2023)
print(my_mustang.get_descriptive_name())
my_leaf = c.ElectricCar("nissan", "leaf", 2023)
print(my_leaf.get_descriptive_name())