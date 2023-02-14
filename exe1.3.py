
x = {}
def func(n):
    # print(x)
    # print(x[n])
    if n in x:
        return x[n]
    else:
        if n == 0 or n == 1:
            x[n] = n
            return n
        else:
            i = func(n-1) + func(n-2)
            x[n] = i
            return i










