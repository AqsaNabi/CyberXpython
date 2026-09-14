<h2>Exception Handling</h2>
ven if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal. Most exceptions are not handled by programs, however, and result in error messages.
The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).
In my example i have used try and exception to handle exception if the input entered is not int thus cannot be summed with the other number <br>
<h3>Raise an exception</h3>
As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword. in my example i have used it to check wether a number is zero if yes display the error message 
<h3>Common built-in exceptions</h3>

Python has many built-in exception classes.

Some important ones:<br>

Exception	Typical cause
ZeroDivisionError	Division by zero
ValueError	Invalid value
TypeError	Wrong type/operation
IndexError	Invalid list/tuple index
KeyError	Missing dictionary key
NameError	Variable doesn't exist
FileNotFoundError	File doesn't exist
ImportError	Import problem
ModuleNotFoundError	Module cannot be found
AttributeError	Object doesn't have attribute