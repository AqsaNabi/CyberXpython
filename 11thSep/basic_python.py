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
