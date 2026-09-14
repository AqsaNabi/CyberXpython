try:
   x=int (input("enter the first number "))
   y=int (input("enter the second number "))
   s=x+y
   print("The summation of the two number is: ", s)
except Exception as e:
   print(e)
print("The excution is completed")   


# using raise exception  
a=int (input("enter the first number "))
b=int (input("enter the first number "))
if b==0:
   raise Exception("Number is Zero")
