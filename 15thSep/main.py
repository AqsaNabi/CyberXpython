#7
l=[]
n=999999999
c=0
def prime(num):
    for i in range(2,num-1):
        if(num%i==0):
            return
        else:
            l.append(num/i)
def l_length():
    m=0
    for c in l:   
        m=m+1
    return m
c=l_length()        
for i in range(0,n):
    if c<10001:
      prime(i)
    else:
      print(l[i])
     