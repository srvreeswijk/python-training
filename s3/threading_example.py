import threading
import time

def my_thread(name):
    for i in range(10):
        time.sleep(1)
        print(name + " " + str(i))

t1 = threading.Thread(target=my_thread, args=["thread1"])
t2 = threading.Thread(target=my_thread, args=["thread2"])

t1.start()
t2.start()

t1.join()
t2.join()


