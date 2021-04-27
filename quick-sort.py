#!/usr/bin/python3

import sys
import time


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
    return alist


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def readFile(lines):
    arrayTemp = []
    f = open("numeros.txt").read().splitlines()
    for x in range(0, lines):
        arrayTemp.append(int(f[x]))
    return arrayTemp


start_time = time.time()
print("Number of lines:", '{0:,}'.format(int(sys.argv[1])).replace(',', '.'))
lines = int(sys.argv[1])
array = []

array = readFile(lines)
print(array)

array = quickSort(array)
print(array)

print("Runtime: %s seconds" % (time.time() - start_time))
