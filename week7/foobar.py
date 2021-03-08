import time

# def foo():
#     return 42

for foo in range(5):
    print(foo)
bar = 1
bar *= 0.2
time.sleep(60)
print(bar)

"""
Fixed:
foobar.py:6: redefinition of unused 'foo' from line 3
foobar.py:11: undefined name 'baz'
"""