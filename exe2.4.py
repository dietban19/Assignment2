import sys
import json
import timeit
import matplotlib.pyplot as plt


sys.setrecursionlimit(200000)

#A modified version of a quicksort algorithm provided by ChatGPT
#in which it dosen't select the pivot by the first element but by the median
#Source: https://openai.com/blog/chatgpt/
def median_of_three(array, start, end):
    mid = (start + end) // 2
    if array[start] > array[mid]:
        array[start], array[mid] = array[mid], array[start]
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if array[mid] > array[end]:
        array[mid], array[end] = array[end], array[mid]
    return mid

def quick_sort(array, start, end):
    if start < end:
        pivot_index = median_of_three(array, start, end)
        pivot = array[pivot_index]
        array[pivot_index], array[start] = array[start], array[pivot_index]

        low = start + 1
        high = end
        while low <= high:
            while low <= high and array[high] >= pivot:
                high = high - 1
            while low <= high and array[low] <= pivot:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]

        array[start], array[high] = array[high], array[start]

        quick_sort(array, start, high - 1)
        quick_sort(array, high + 1, end)

def main():

    with open('ex2.json') as f:
        inputs = json.load(f)
    timing_results = []

    for i in inputs:
        arr = i
        elapsedTime = timeit.timeit(lambda: quick_sort(arr,0,len(arr)-1), number = 1)
        timing_results.append(elapsedTime)


    plt.plot(timing_results)
    plt.xlabel("Input Index")
    plt.ylabel("Execution Time (s)")
    plt.title("Timing Results for QuickSort Algorithm")
    plt.show()

if __name__ == '__main__':
    main()