class Restaurant :
    """레스토랑 클래스"""

    def __init__(self, rname, rtype) :
        """name이랑 type 초기화"""
        self.restaurant_name = rname
        self.cuisine_type = rtype
    
    def describe_restaurant(self):
        print(f"그 식당 이름은 {self.restaurant_name}이야")

    def open_restaurant(self):
       print(f"그 식당은 {self.cuisine_type}식당이야")

my_rest = Restaurant("python restaurant", "KoreanFood") 

class IceCreamStand(Restaurant) :
    def __init__(self, rname, flavors):
        super().__init__(rname)
        self.flavors = flavors

    def show_flavors(self) :
        print("무슨 맛이냐면{}".format(self.flavors))
        print(f"무슨 맛이냐면 {self.flavors}")

new_rest = Restaurant("bobaboba", "iceCream", "초코맛")
ice_cream = IceCreamStand("초코맛")
ice_cream.show_flavors()

print(f"레스토랑 이름과 타입은 {my_rest.restaurant_name}, {my_rest.cuisine_type}")
new_rest.describe_restaurant()
print(f"이번에 여는 레스토랑은{new_rest.restaurant_name}")
print(f"맛은 {Restaurant.self.flavors}")

#class IceCreamStand(Restaurant): 
#     def __init__(self, rname, rtype, flavors):
#         super().__init__(rname, rtype)
#         self.flavors = flavors
    
#     def show_flavors(self) :
#         print("맛이 {}".format(self.flavors))
#         print(f"맛이 {self.flavors}")

