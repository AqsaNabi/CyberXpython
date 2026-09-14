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
#importing logging
import logging 
logging.basicConfig(filename="files.log", level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s') #asc is the creation time of the log record"

# Log messages of various severity levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')