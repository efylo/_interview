import array

def main():
    arri = array.array('i', [1, 2, 3])
    print(f'arri: {arri}')
    print('arri creation\n')
    arri.append(2)
    print(f'arri: {arri}')
    print('arri append 2\n')
    idx = arri.index(2)
    print(f'arri: {arri}')
    print('first index of value(2): {idx}\n')
    arri.remove(2)
    print(f'arri: {arri}')
    print(f'first value(2) removed\n')
    arri.insert(2, 5)
    print(f'arri: {arri}')
    print(f'insert value(5) to index(2)\n')
    arri.reverse()
    print(f'arri: {arri}')
    print(f'array reversed\n')

    # checks

    # 1. is an integer bigger than 4 bytes(2**31+1) appendable? 
    #    - no, raises an error(overflow)
    #    - this ensures int type array can represent -2**31 <= x < 2**31
    try:
        arri.append(2**31)
    except OverflowError:
        print(f'2**31 not appendable to arri')
    
    try:
        arri.append(-2**31-1)
    except OverflowError:
        print(f'-2**31-1 not appendable to arri\n')

    # 2. if type_code is unsigned int, is a negative integer appendable? 
    #    - no, raises an error(overflow)

    arrI = array.array('I', [3, 2, 1, 0])
    print(f'arrI: {arrI}')

    try:
        arrI.append(-1)
    except OverflowError:
        print(f'negative value not appendable to arrI')
    
    try:
        arrI.append(2**32)
    except OverflowError:
        print(f'2**32 not appendable to arrI\n')

    # 3. if you create an array of float type with init vale of integers, 
    #    - it automatically switches int to float

    arrf = array.array('f', [1, 2, 3])
    print(f'arrf: {arrf}\n')

    # 4. what is unicode character?
    #    - 'char', and it can represent Korean
    arru = array.array('u', ['a', 'b', 'c', '한', '글', ])
    print(f'arru: {arru}\n')

    # 5. what refers signed char 'b' (-128 ~ 127)?
    arrb = array.array('b', [1, 2, 3, -1, -2, -3])
    print(f'arrb: {arrb}\n')

    return

if __name__ == "__main__":
    main()