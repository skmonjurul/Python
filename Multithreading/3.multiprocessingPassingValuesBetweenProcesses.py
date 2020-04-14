import multiprocessing
import time

def cal_cube(arr, queue):
    # time.sleep(1)
    for i in arr:
        # print(i)
        queue.put(i*i)

if __name__=="__main__":
    arr_global=[1,2,3,4]
    queue= multiprocessing.Queue()
    p1= multiprocessing.Process(target= cal_cube, args= (arr_global, queue))

    p1.start()
    p1.join()

    while queue.empty() is False:
        print(queue.get())