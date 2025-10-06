
import time

def func1():
    a = 2
    b = 2
    c = a+b
    return c

def func2():
    a = 2
    b = 2
    c = a+b
    return c

def func3():
    a = 2
    b = 2
    c = a+b
    return c



test = func1()+func2()+func3()



def test_func():
    print("Function is executing...")
    test1 = test - 1
    print(test1)
    return test1

# Store functions in a list
function_list = [func1, func2, func3]

# Loop through the list and call each function


def decision():
    if test > 0:
        print(test)
        test_func()
        time.sleep(5)
        for func in function_list:
            func()
    else:
        print("no")

decision()