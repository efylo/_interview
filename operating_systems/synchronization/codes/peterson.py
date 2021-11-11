from threading import Thread


"""
Sometimes threads go too slow - I don't know why it happens.
Debugging on them, there is no error in counting global variables
and process isn't on infinite loop either. 
"""
def countHT(i: int, flag: list):
    """function to count Hundred Thousand"""
    # global variables
    global turn, cnt
    # local variable to count hundred thousand
    cnt_i = 0
    # loop until hundred thousand
    while cnt_i < 100000:
        # hands up - i'th thread want to use critical section
        flag[i] = True
        # turn over to other process
        j = (i+1)%2
        turn = j
        # continuously check if j's turn is over
        while flag[j] and turn == j:
            continue
        # Critical Section
        cnt = cnt + 1
        flag[i] = False
        # Remainder Section
        cnt_i += 1
    print(f"Thread {i} finished with cnt = {cnt}, cnt_i = {cnt_i}")


def main():
    global turn, cnt
    turn = 0
    cnt = 0
    # threads more than 2 causes an error
    n = 2
    flag = [False] * n
    threads = []
    for i in range(n):
        threads.append(Thread(target=countHT, args=(i, flag, )))

    for i in range(n):
        threads[i].start()


if __name__ == "__main__":
    main()