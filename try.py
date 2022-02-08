from __future__ import print_function


try:
    total = 1 / 0

except Exception:
    total = 0

print(total) 
pass


bb = int(input('input no.'))
print(bb)



def my_decorator(func):
    def wrapper():
        print("hello")
        func()
        print("world")
    return wrapper

@my_decorator
def myfunc():
    print("result")
myfunc()