
@profile
def my_func():
    a = [1] * (10**6)
    b = [2] * (2 * 10 ** 7)

    del b
    return a

if __name__ == '__main__':
    my_func()


"""
output:
Filename: memory.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     2   19.250 MiB   19.250 MiB           1   @profile
     3                                         def my_func():
     4   26.727 MiB    7.477 MiB           1       a = [1] * (10**6)
     5  179.352 MiB  152.625 MiB           1       b = [2] * (2 * 10 ** 7)
     6                                         
     7   26.914 MiB -152.438 MiB           1       del b
     8   26.914 MiB    0.000 MiB           1       return a
"""