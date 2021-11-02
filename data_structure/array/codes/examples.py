import array
from typing import Any
from array_rotation import rotatedArray, getArray


# search for value in sorted & rotated array and return index
def searchSortedRotated(arr: array.array, value: Any, low: int, high: int):
    # if value not exists
    if low == high:
        return -1
    mid = low + (high-low)//2
    # return mid if searched
    if value == arr[mid]:
        return mid
    # pivot on left half
    if arr[low] > arr[mid]:
        if value < arr[mid]:
            return searchSortedRotated(arr, value, low, mid)
        return searchSortedRotated(arr, value, mid+1, high)
    # pivot on right half
    else:
        if value < arr[low] or value > arr[mid]:
            return searchSortedRotated(arr, value, mid+1, high)
        return searchSortedRotated(arr, value, low, mid)


# search for the value, returns value and the index
def search(arr: array.array):
    value = int(input("enter the value you want to search for: "))
    return value, searchSortedRotated(arr, value, 0, len(arr))


# array rotation, and binary search in sorted, rotated array
def arrayRotation_binarySearch():
    arr = rotatedArray()
    value, idx = search(arr)
    print(f'value {value} searched in {idx}\'th index of {arr}\n')
    return


# search for pairs of sum x in array
def searchPairs(arr: array.array, x: int):
    n = len(arr)
    ret = list()

    # find minimum(l), maximum(r)
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            l, r = (i+1)%n, i
    
    # loop until finds all pair
    while(l != r):
        # when smaller + bigger == x
        if arr[l] + arr[r] == x:
            ret.append((arr[l], arr[r]) if l < r else (arr[r], arr[l]))
            if l == (r-1+n)%n:
                break
            l, r = (l+1)%n, (r-1+n)%n
        # when smaller + bigger > x
        elif arr[l] + arr[r] > x:
            r = (r-1+n)%n
        # when smaller + bigger < x
        else:
            l = (l+1)%n
    
    return ret


# search for a pair of a given sum in sorted, rotated array
def search4Pairs_GivenSum():
    arr = getArray()
    x = int(input("enter sum you want to find: "))
    pairs = searchPairs(arr, x)
    print(f'pairs of sum {x} in {arr}\n - ', end='')
    for pair in pairs:
        print(f'{pair}', end= " ")
    print("\r")
    return


# search for maximum pair of i*arr[i] with only rotation of array permitted
def searchMax(arr: array.array):
    # parameters of array
    mass = sum(arr)
    n = len(arr)

    # first value of sum of i*arr[i]
    prev = int()
    for i in range(n):
        prev += i*arr[i]
    
    # variable for saving maximum
    ret = prev

    # finding out maximum sum(i*arr[i])
    for i in range(1, n):
        prev = prev + mass - arr[-i]*n
        ret = max(ret, prev)
    
    return ret


# maximum sum of i*arr[i] which you can only rotate an array
def search4MaxSum_iMultarri():
    arr = getArray()
    ret = searchMax(arr)
    print(f'maximum i*arr[i] is {ret}')
    return


# the rotation count of rotated & sorted array
def rotationCount(arr: array.array):
    n = len(arr)

    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            return (i+1)%n

def main():
    # example 01
    print('exampel 01: find index of value (x) in sorted, rotated array')
    arrayRotation_binarySearch()

    # example 02
    print('example 02: search for pairs in an array which each pair\'s sum is (x)')
    search4Pairs_GivenSum()

    # example 03
    print('example 03: given an array, search for maximum sum of i*arr[i]\narray rotation is only possible way of array manipulation')
    search4MaxSum_iMultarri()


if __name__ == "__main__":
    main()