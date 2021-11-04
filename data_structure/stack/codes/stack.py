from collections import deque
from queue import LifoQueue


def mainList():
    # stack as a form of list
    stack_list = []

    # push = append
    stack_list.append('a')
    stack_list.append('b')
    stack_list.append('c')

    # print
    print(f'stack elements: {stack_list}')

    # pop
    print(f'stack pop {stack_list.pop()}')  # 'c'
    print(f'stack pop {stack_list.pop()}')  # 'b'
    print(f'stack pop {stack_list.pop()}')  # 'a'

    # empty stack
    print(f'stack elements: {stack_list}')

    return


def mainDeque():
    # stack as a form of deque of collections module
    stack_deque = deque()
    
    # push
    stack_deque.append('d')
    stack_deque.append('e')
    stack_deque.append('f')

    # print
    print(f'stack elements: {stack_deque}')

    # pop
    print(f'stack popped {stack_deque.pop()}')  # 'f'
    print(f'stack popped {stack_deque.pop()}')  # 'e'
    print(f'stack popped {stack_deque.pop()}')  # 'd'

    # empty stack
    print(f'stack elements: {stack_deque}')

    return


def mainLifoQueue():
    # stack as a form of LifoQueue of queue module
    stack_LifoQueue = LifoQueue()

    # push
    stack_LifoQueue.put_nowait('g')
    stack_LifoQueue.put_nowait('h')
    stack_LifoQueue.put_nowait('i')

    # print
    print(f'stack elements: {stack_LifoQueue}')

    # pop
    print(f'stack popped {stack_LifoQueue.get_nowait()}')   # 'i'
    print(f'stack popped {stack_LifoQueue.get_nowait()}')   # 'h'
    print(f'stack popped {stack_LifoQueue.get_nowait()}')   # 'g'

    # empty stack
    print(f'stack elements: {stack_LifoQueue}')

    return


def main():
    mainList()
    mainDeque()
    mainLifoQueue()


if __name__ == "__main__":
    main()