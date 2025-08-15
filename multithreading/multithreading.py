from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello from thread")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi from thread")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.5)  # Sleep to ensure t1 starts before t2
t2.start()

t1.join()
t2.join()  

print("Bye: both threads finished")


