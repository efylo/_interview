import array


# array input
def getArray():
    return array.array('i', list(map(int, input("enter an array: ").split())))


# Euclidean algorithm of getting greatest common divisor(gcd)
def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a%b)


# rotate via juggling algorithm
def juggle(arr: array.array, d: int):
    n = len(arr)
    d = d%n     # just in case d is bigger than n
    gc_divisor = gcd(d, n)

    # juggle for gcd(d, n) times
    for i in range(gc_divisor):
        temp = arr[i]   # first value
        # each juggle goes (n//gc_divisor - 1) times
        for j in range(n//gc_divisor-1):
            prev = i + j*d
            next = prev + d
            arr[prev%n] = arr[next%n]
        # last juggle
        last = i + (n//gc_divisor-1)*d
        arr[last%n] = temp
    return


# reverse an array from start to end(not included)
def reverse(arr: array.array, start: int, end: int):
    while start < end-1:
        temp = arr[start]
        arr[start] = arr[end-1]
        arr[end-1] = temp
        start += 1
        end -= 1
    return


# rotate via reverse algorithm
def reversal(arr: array.array, d: int):
    n = len(arr)
    reverse(arr, 0, d)
    reverse(arr, d, n)
    reverse(arr, 0, n)
    return


# swap arr[A_start:A_start+l] and arr[B_start:B_start+l]
def swap(arr: array.array, A_start: int, B_start: int, l: int):
    temp = arr[A_start:A_start+l]
    arr[A_start:A_start+l] = arr[B_start:B_start+l]
    arr[B_start:B_start+l] = temp
    return


# block swap algorithm
def blockSwap(arr: array.array, start: int, end: int, d: int):
    n = end - start
    if d==n or d==0:
        return
    else:
        if d < n-d:
            l = d
            swap(arr, start, end-d, l)
            blockSwap(arr, start, end-d, d)
        elif d > n-d:
            l = n-d
            swap(arr, start, start+d, l)
            blockSwap(arr, end-d, end, 2*d-n)
        else:
            swap(arr, start, end-d, d)
            return


# rotate via 3 type codes 'j', 'r', 'b'
def rotate(arr: array.array, d: int, type_code: str):
    if type_code == 'j':
        juggle(arr, d)
    elif type_code == 'r':
        reversal(arr, d)
    elif type_code == 'b':
        blockSwap(arr, 0, len(arr), d)
    else:
        raise ValueError
    return


# returns rotated array, via given inputs
def rotatedArray():
    # define an array by standard input
    arr = getArray()
    type_code = input("enter an algorithm ['j': juggle, 'r': reversal, 'b': blockSwap]: ")
    d = int(input("enter the number you want to rotate: "))
    rotate(arr, d, type_code)

    return arr


# main function
def main():
    pass


if __name__ == "__main__":
    main()