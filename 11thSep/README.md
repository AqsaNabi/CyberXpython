**Virtual Environment**
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.
It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.
It also have many features like:
Has its own Python interpreter
Has its own set of installed packages
Is isolated from other virtual environments
Can have different versions of the same package
Using virtual environments is important because:
It prevents package version conflicts between projects
Makes projects more portable and reproducible
Keeps your system Python installation clean
Allows testing with different Python versions
**Creating a Virtual Environment**
Python has the built-in venv module for creating virtual environments.
I used  **python -m venv first_venv** command to generate v-env withing my 11\9\26 folder, by chaning the path to that particular directory. After creating a venv, it install these files Include/ → contains C/C++ header files that some Python packages may need.
Lib/ → contains the Python packages installed inside your virtual environment.
Scripts/ → contains executables such as python, pip, and the activation scripts.
pyvenv.cfg → configuration file telling Python that this folder is a virtual environment and which base Python installation it uses.
.gitignore → tells Git which files/folders it should not upload to GitHub.
**Acticate the V.env** 
 i used **first_venv\Scripts\activate** but due to authorization error i first used Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser and Get-ExecutionPolicy -Scope CurrentUser
 we can create files within this venv and run after activating venv
 To deactivate we use **deactivate** 
 **PIP**
 A package contains all the files you need for a module. A module is usually a single .py file. Modules are Python code libraries you can include in your project.
We use pip to install a pacckage also to unistall the packages also can use to check all installed packages in our systems using **pip list**
**PYTHON DATA TYPES**
Data types in Python define the type of value stored in a variable and determine the operations that can be performed on that data. Since Python treats everything as an object, each value is associated with a specific data type. Helps the interpreter understand how to store and process different kinds of data efficiently.
Enables correct operations by ensuring only valid actions are performed on compatible data types. 
**Numeric**
Numeric data types are used to store numeric values. It can be an integer, floating number or even a complex number. Python supports three main numeric types:  
**Integers:** value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals).
**Float:** value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point.
**Complex:** It is represented by a complex class. It stores numbers with real and imaginary parts. For example: 2+3j                                        
To check types i used type() function.
Sequence Data Types
A sequence is an ordered collection of items, which can be of similar or different data types. Elements in a sequence can be accessed using indexing.
***Sequence Data Types***
A sequence is an ordered collection of items, which can be of similar or different data types. Elements in a sequence can be accessed using indexing.
**String**
Strings are used to store text data. A string is represented using the str class and can be created using single, double or triple quotes. We can also use index to access characte within the string                                      
**Lists** are ordered and mutable collections used to store multiple items in a single variable. Elements in a list can be of different data types and are accessed using indexing.
**Tuple**
Tuples are ordered and immutable collections used to store multiple items in a single variable. Once created, tuple elements cannot be modified and are accessed using indexing. 
**Boolean Data Type**
Boolean data type represents one of two values: True or False. It is mainly used in conditions and comparisons and is represented by the bool class.
**Set Data Type**
Sets are unordered and mutable collections used to store unique elements. Since sets are unordered, elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.
**Dictionary Data Type**
Dictionaries are used to store data in key:value pairs. Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.
**Loops** are used to execute a block of code repeatedly until a condition is met or all items in a sequence are processed. The main types are For loops (iterating over sequences) and While loops (executing code based on a condition)
**For Loop**
For loops is used to iterate over a sequence such as a list, tuple, string or range. It executes a block of code once for each item in the sequence.
A for loop can also iterate through sequence elements using their index values with the help of range() and len().
**While Loop**
While loop repeatedly executes a block of code as long as the given condition remains true. When the condition becomes false, the line immediately after the loop in the program is executed.
**Nested Loops**
A nested loop is a loop inside another loop. The inner loop executes completely for every iteration of the outer loop.
**List Comprehension**
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
syntax newlist = [expression for item in iterable if condition == True]  
Mutable and Immutable describe whether an object can be changed after it has been created. A mutable object can be modified without creating a completely new object—for example, a list can have items added, removed, or changed, and a dictionary can have its values updated. An immutable object cannot be modified once it is created; if you appear to change it, Python actually creates or uses a new object and makes the variable point to that new object. Integers, floats, strings, and tuples are immutable. We have both because they serve different purposes: mutable objects are useful when we need data to change during a program, while immutable objects provide stability and prevent their contents from being accidentally changed. For example, a list of students may need new students added, so a list is mutable, whereas a student's name or age can be treated as an immutable value. '
