import threading
import time
def print_numbers():
   for i in range(1,10):
     
     print(i**2+7**9)
     time.sleep(1)
def print_letters():
   for i in 'how to kill a man in 10 days':
      print(i)  
      time.sleep(0.7)

 #creating two threads objects, one for each function
th1=threading.Thread(target=print_numbers) 
th2=threading.Thread(target=print_letters)  
#starting the two threads 
th1.start()
th2.start()

#ensures that the main thread waits for the new thread to finish before continuing.
th1.join()
th2.join()
print("Both threads have finished")
