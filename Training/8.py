# gil = global interpretor lock
# one thread per process
'''
import time
from threading import Thread
def greet():
    start = time.time()
    name = input("Enter your name")
    print("Hello " + name)
    print("Time taken for greet is "+ str(time.time() - start))

def complex():
    start = time.time()
    [n**2 for n in range(2000000)]
    print("Time taken for complex is "+ str(time.time()-start))

complex()
greet()

start = time.time()
t1 = Thread(target=complex)
t2 = Thread(target=greet)

t1.start()
t2.start()

t1.join()
t2.join()
print("Time take is" + str(time.time() - start))
'''
#thread pool
'''
from concurrent.futures import ThreadPoolExecutor
import time

def greet():
    start = time.time()
    name = input("Enter your name")
    print("Hello " + name)
    print("Time taken for greet is "+ str(time.time() - start))

def complex():
    start = time.time()
    [n**2 for n in range(2000000)]
    print("Time taken for complex is "+ str(time.time()-start))

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex)
    pool.submit(greet)
'''
#arguments and kwargs
'''
def fun(*args):
    for n in args:
        print(n)

fun(1,2,3,4,5)

def func(**kwargs):
    for k,v in kwargs.items():
        print ("%s %s" %(k, v)) 
func(a=1,b=2,c=4)
'''
#processor
'''
import time
from multiprocessing import Process
def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
'''
#pool executor for process\
'''
import time
from concurrent.futures import ProcessPoolExecutor
def complex():
    start = time.time()
    [n**2 for n in range(2000000)]
    print("Time taken for complex is "+ str(time.time()-start))

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=1) as pool:
        pool.submit(complex)
'''
#lock
'''
import threading 
deposit = 100
lock = threading.Lock()
def add_profit(): 
    global deposit
    for i in range(100000):
        #lock.acquire()
        deposit = deposit + 10
        #lock.release()

def pay_bill(): 
    global deposit
    for i in range(100000):
        #lock.acquire()
        deposit = deposit - 10
        #lock.release()

thread1 = threading.Thread(target = add_profit, args = ())
thread2 = threading.Thread(target = pay_bill, args = ())
thread1.start() 
thread2.start()
thread1.join()
thread2.join()
print(deposit)
'''
#async and await
'''
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
'''