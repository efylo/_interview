from threading import Thread


def countHT():
    """function to cound hundred thousand"""
    # global variables
    global lock, cnt
    # local variable
    cnt_i = 0
    while cnt_i < 100000:
        if lock == 0:
            enter_CS()
            cnt_i += 1
    print(f"Thread finished: cnt={cnt}, cnt_i={cnt_i}")


def enter_CS():
    """function for entering critical section"""
    # global variables
    global lock, cnt
    # lock-down
    lock = 1
    cnt = cnt + 1
    leave_CS()


def leave_CS():
    """function for leaving critical section"""
    global lock
    lock = 0


def main():
    global lock, cnt
    lock, cnt = 0, 0
    n = int(input("enter number of threads: "))
    threads = []
    for _ in range(n):
        threads.append(Thread(target=countHT, ))
    
    for i in range(n):
        threads[i].start()


if __name__ == "__main__":
    main()