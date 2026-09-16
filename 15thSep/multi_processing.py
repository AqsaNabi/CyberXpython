import multiprocessing

def sq(num):
    for n in num:
        print('square ' +str(n*n))
  
def cube(num):
    for n in num:
        print('cube  ' +str(n*n*n))


if __name__== "__main__":
    arr=[1,2,3,4,5,6]
    p1=multiprocessing.Process(target=sq, args=(arr,))
    p2=multiprocessing.Process(target=cube, args=(arr,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()


    print("Excution is done")
