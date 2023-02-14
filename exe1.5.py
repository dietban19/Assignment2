import time
import matplotlib.pyplot as plt



def func(n,data={}):
    if n in data:
        return data[n]
    else:
        if n == 0 or n == 1:
            data[n] = n
            return n
        else:
            i = func(n-1) + func(n-2)
            data[n] = i
            return i

def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)



def timing_function(func, n):
    startTime = time.time()
    result = func(n)
    endTime = time.time()
    return endTime - startTime


def main():
    nlist = list(range(0, 36))

    modifiedCodeTime = [timing_function(func, n) for n in nlist]
    originalCodeTime = [timing_function(func1, n) for n in nlist]

    plt.plot(nlist, modifiedCodeTime, label='Modified Code (memoized)', color = "red")
    plt.plot(nlist, originalCodeTime, label='Original Code (non-memoized)', color = "blue")
    plt.legend()
    plt.xlabel('n')
    plt.ylabel('time (seconds)')
    plt.show()

if __name__ == '__main__':
    main()