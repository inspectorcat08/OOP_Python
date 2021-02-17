# # первый вариант
#
# def makeAdder(x):
#     def func(y):
#         return x + y
#     return func
#
# add5 = makeAdder(5)
# add10 = makeAdder(10)
#
# print(add5(2))
# print(add10(2))
#
# # второй вариант
#
# a = lambda x1: x1 + 2
# b = lambda y1: y1 + 2
#
# print(a(5))
# print(b(10))
#

def my_decorator(func):
    def wrapper():
        print("i am run first")
        func()
        print('i am run third')
    return wrapper

@my_decorator
def some_func():
    print('here i am, second!!')

some_func()

