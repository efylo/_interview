from threading import Thread


class Semaphore_:
    """simple semaphore class"""
    def __init__(self, value) -> None:
        self.s = value
        pass

    def P(self, i: int):
        while self.s == 0:
            print(f'An instance is running - from id {i}')
            pass
        self.s -= 1
    
    def V(self, ):
        self.s += 1


def f(s: Semaphore_, i: int):
    """thread to run"""
    # ask for semaphore acquire
    s.P(i)
    # do some functionality - if costly, then it is blocked from other thread sometimes
    x = [1, 2, 3, 4]
    for i in range(100):
        for j in range(100):
            x[(100*i+j)%4] += 1 if j%2 == 0 else -1
    # increase s
    s.V()
    

def main():
    sema = Semaphore_(1)
    threads = []
    for i in range(10000):
        threads.append(Thread(target=f, args=(sema, i, )))
    
    for i in range(10000):
        threads[i].start()


if __name__ == "__main__":
    main()