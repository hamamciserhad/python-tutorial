"""
🧵 Python Multithreading Tutorial

This script demonstrates how to use threading by creating two classes that extend the Thread class.
Each class overrides the run() method to print a message 8 times with a 1-second delay.

Steps:
1. Import Thread and sleep
2. Define Hello and Hi classes that extend Thread
3. Start the threads using .start()
4. Use .join() to wait for them to finish
5. Print 'done' after both threads complete
"""
from threading import Thread
from time import sleep


# This thread prints "hello" every second, 8 times
class Hello(Thread):
    def run(self):
        for i in range(8):
            print("hello")
            sleep(1)

# This thread prints "hi" every second, 8 times
class Hi(Thread):
    def run(self):
        for i in range(8):
            print("hi")
            sleep(1)


# Create thread instances
t1 = Hello()
t2 = Hi()


# Start both threads
t1.start() # burda run cagirmadik ama run u kendisi cagirir
sleep(0.3)
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

# Print after threads complete
print("done") # bu sonda olmuyor bu main thred e mensup o yüzden main thread beklemeli join kullandik
