a=20 
b=2.90
c=15+7j
print(a,b,c)
print(type(a), type(b), type(c))
s="It's End of the World"
print(type(s))
print(s)
print(s[1],s[-1])
x=[17,8,9,"Joy", "despair"]
print(x,x[-3])
tuple=(8,24,4464,11233,"You")
print(tuple, tuple[1:-1], type(tuple))
bool=True
print(bool, type(bool))
#creating a set and printing it
set={'a','b','c','d','a'}
print(set)
for i in set:
    print(i)
 #dictionary   
d = {'name': 'abc', 'roll_no': 15, 'branch': {'CSE','Civil'}}
print(d['name'])    
print(d.get('branch'))    
for i in tuple:
    print(i)
for i in x: #x is the list here
    print(i)   
 #while loop    
p = 0
while (p < 3):
    p = p + 1
    print(s)
#Nested loop
for i in range(1, 5):
    for j in range(i):
        print('*', end=' ')
    print()
# creating a new list using already defined list 'x'       
new_list=[]
for i in x:
    new_list.append(i)
print(new_list)    
#list corephension
new_list2=[i for i in x if 1==True]
print(new_list2)
#function example to print each elementt within the list
def List_elements(l):
    print("The list have following elements: ")
    for i in l:
        print(i)
    return    
#Using Default Arguments
List_elements(new_list)
def sum(y,x=10):
    print("The ssum is: ", x+y)
sum(23)
#passes function as a paarameter to another function
def fun(func, arg):
    return func(arg)
  
def square(x):
    return x ** 2
  
res = fun(square, 5)
print(res)    
#Using *args*
def mul(*argg):
    l=[]
    for arg in argg:
        l.append(arg)
    m=1
    for i in l:
            m=m*i
    return m
print(mul(2,4,5))        
#using *kwargs
def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k}: {val}")

fun(name="aqsa", E_roll=2, branch="CSE")
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    
    def val(self):
        print(f"Name - {self.name} and Age - {self.age}.")

p1 = Person("NAAM", 23)
p1.val()
        
      