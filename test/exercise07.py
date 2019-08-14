"""
定义my_print函数，统计该函数调用次数
在函数中统计
"""
time=0
def my_print():
    global time
    time+=1
    pass
my_print()
my_print()
my_print()
print(time)