<h2>Exception Handling</h2>
ven if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal. Most exceptions are not handled by programs, however, and result in error messages.
The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).
In my example i have used try and exception to handle exception if the input entered is not int thus cannot be summed with the other number
The try/except block is used to handle exceptions. Code that might raise an exception is placed in the try block, and if an exception occurs, the except block is executed. Here is the syntax of try/except in a code block:


<br>
try:<br>
     Code that might raise an exception<br>
    pass <br>
except ExceptionType as e: <br>
    Code to handle the exception <br>
    pass <br>
else Block (Optional): Contains code that runs if no exceptions are raised in the try block. It is useful for code that should only run when the try block is successful.

finally Block (Optional): Contains code that always runs, regardless of whether an exception was raised or not. This is typically used for cleanup actions, such as closing files or releasing resources.

The code that could potentially fail is put inside the try block. If an issue arises, the program’s execution will enter the except block. <br>
<h3>Raise an exception</h3>
As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword. in my example i have used it to check wether a number is zero if yes display the error message. Re-raise means you catch an exception, maybe do something useful with it, and then send the same exception back to the code above you because you cannot properly handle the problem at the current level.
<h3>Common built-in exceptions</h3>

Python has many built-in exception classes.

Some important ones:<br>

Exceptio---Typical cause<br>
ZeroDivisionError---Division by zero <br>
ValueError---nvalid value<br>
TypeError---Wrong type/operation<br>
IndexError---Invalid list/tuple index<br>
KeyError---Missing dictionary key<br>
NameError---Variable doesn't exist<br>
FileNotFoundError---File doesn't exist<br>
ImportError---Import problem<br>
ModuleNotFoundError	---Module cannot be found<br>
AttributeErro---Object doesn't have attribute<br>
<h3> when to let an application crash</h3>
We should let an application crash when it reaches a serious problem that the current code cannot safely handle or recover from. If we catch the error and simply continue, the application might produce wrong results, corrupt data, or behave unpredictably
In Python, we usually let the application crash by simply not catching the exception, or by re-raising it if we already caught it for some reason.
<h3>Logging</h3>
Logging helps developers track errors, events, or any runtime information in an application or program. Logging is an important and crucial aspect of software engineering as it has the ability to record everything that goes right or wrong in a post-development application. Logging is one of the most important pillars of monitoring. Python provides a built-in module that can be used for logging

purposes. To use this module, the first thing to do is to import it.

using <h4>import logging</h4> Then, configure the logger using the basicConfig method. You need to pass parameters to it, such as the log level, the format of the message, and the output file to save the log
<br>
logs will be written to a file named at 'name' paramter of the basic_Config function. The log message format includes the timestamp, logger name, log level, and the actual message.

Python logging has different log levels that indicate the severity of an event or message. These log levels allow you to categorize and filter messages based on their importance. Here’s a breakdown of the common log levels in Python:
<br>
Log Levels
DEBUG: Detailed information, typically of interest only when diagnosing problems. Used for debugging purposes during development.

INFO: Confirmation that things are working as expected. This is the level you would use for normal operations and informational messages.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., "disk space low"). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform some function. An error indicates a significant issue that needs attention.

CRITICAL: A very serious error, indicating that the program itself may be unable to continue running. Critical errors often represent severe problems that require immediate action.

The logging module allows you to control which messages are recorded by setting the logging level. Only messages that are equal to or more severe than the set level will be logged. The default level is WARNING, meaning only WARNING, ERROR, and CRITICAL messages are logged unless you change the logging configuration.

In the code example above, we set the logging level to DEBUG, which means all log messages (DEBUG, INFO, WARNING, ERROR, and CRITICAL) will be recorded in the app.log file.