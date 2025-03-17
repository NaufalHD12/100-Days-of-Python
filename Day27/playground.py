def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


# print(add(1, 2, 8))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    return n
    
# print(calculate(2, add=2, multiply=3))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.color)