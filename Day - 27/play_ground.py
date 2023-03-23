# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
#
#
# print(add(3,4,5))
# #
# def calculate(n, **kwargs):
#
#     # for key,value in kwargs.items():
#     #     print(kwargs["add"])
#     n +=  kwargs["add"]
#     print(n)
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2,add=3,multiply=5)


class Car:

    def __init__(self,**kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')
        self.speed = kwargs.get('speed')


car = Car(make='nissan',model='gtr')

print(car.model)
