import sys
import json
import timeit
import matplotlib.pyplot as plt
import threading

threading.stack_size(33554432)

sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def main():
    with open('ex2.json') as f:
        inputs = json.load(f)
    timing_results = []

    j = 0
    for i in inputs:
        if j <= 8:
            arr = i
            elapsedTime = timeit.timeit(lambda: func1(arr, 0, len(arr) - 1), number=1)
            timing_results.append(elapsedTime)
        j = j + 1

    plt.plot(timing_results)
    plt.xlabel("Input Index")
    plt.ylabel("Execution Time (s)")
    plt.title("Timing Results for QuickSort Algorithm")
    plt.show()


if __name__ == '__main__':
    main()