def recursiveFunc(num):
    if num == 101:
        return
    else:
        if (num%3==0) and (num%5==0):
            print("FizzBuzz")
        elif num%5==0:
            print("Buzz")
        elif num%3==0:
            print("Fizz")
        else:
            print(num)
    recursiveFunc(num+1)
    
recursiveFunc(1)
            