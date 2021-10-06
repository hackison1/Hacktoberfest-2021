import threading
import time
import random

semaphore = threading.Semaphore(0)

def consumer():
    print("Consumer is waiting")
    semaphore.acquire()
    print("Consumer notify: consumed item number %s" %item)

def producer():
    global item
    time.sleep(10)
    item = random.randint(0, 1000)
    print("Producer notify : produced item number %s" % item)

    semaphore.release()

for i in range(5):
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
