# checking that, although arr_global, still value not updated inside it, as it is a different process other than main
# had it been different thread in main, it wouldve been updated
import multiprocessing
import time
import sys
import random
sys.__stdout__
sys.__stdout__.fileno()

start_time= time.time()

arr_global=[]

def calc_cube(arr):
    for i in arr:
        print(i*i*i)
        arr_global.append(i*i*i)
    print("arr_global inside process p2: ",arr_global)
    print(sys.__stdout__)
    print(sys.__stdout__.fileno())

if __name__=="__main__":
    random.seed(1)
    arr= [random.randint(1,10) for i in range(10)]

    p2= multiprocessing.Process(target= calc_cube, args=(arr,))
    p2.start()
    p2.join()

    print("arr_global, outside process p2, i.e inside main process: ", arr_global)
    
    end_time= time.time()
    print(end_time-start_time)
