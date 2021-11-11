from threading import Thread, Lock
from random import shuffle


def count(key: Lock, i: int):
    global x
    for _ in range(1000000):
        key.acquire()
        x += 1
        key.release()
    print(f"Thread {i} end: global={x}")


def main():
    # global variable cnt
    global x
    x = 0
    # key - to lock down
    key = Lock()
    n = int(input("enter number of threads: "))
    threads = []
    for i in range(n):
        threads.append(Thread(target=count, args=(key, i, )))
    
    for i in range(n):
        threads[i].start()


if __name__ == "__main__":
    main()