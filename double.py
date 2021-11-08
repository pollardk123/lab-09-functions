def double(n):
        # n is a PARAMETER that is used within the function DEFINITION.
        # n a PARAMETER is a placeholder for input data.
        return n * 2;

userstring = input("Number please...")
usernum = int(userstring)

print(double(usernum))
       #usernum is passed as an argument to the double() function CALL.
      # an argument is a placeholder for a real value that gets PASSED into a function call.
      # line 18 order : 1. usernum is evaluated ; 2.double() is evaluated; 3. consol.log() is evaluated.
