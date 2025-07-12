import multiprocessing
import time
def sqr_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")
def cube_num():
    for i in range(5):
        time.sleep(1)
        print(f"Cube:{i*i*i}")

#create 2 processes
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=sqr_num)
    p2 = multiprocessing.Process(target=cube_num)

    t = time.time()

    #start process
    p1.start()
    p2.start()

    # wait process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)