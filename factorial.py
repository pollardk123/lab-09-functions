def factorial(n):
       # An INTERATIVE example of the factorial function.
    total = 1
    for i in range(0,n):
         # i < n ensures that I will never reach n...
        total = total * (n-i);
        # and therefore will never multiply by 0
        print("Current i is:" + str(i))
        print("Current value of total is:" + str(total))
    return total


userstring = input("Number please...")
usernum = int(userstring)

print(str(usernum)+ " i is"  + str(factorial(usernum)))
