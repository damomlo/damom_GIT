"""
定义判断列表中是否存在相同元素的函数
让列表中所有元素两两比较
"""
def comparison_element(list_target):
    for i in range(len(list_target)-1):
        for item in range(i+1,len(list_target)):
            if list_target[i]==list_target[item]:
                return True
    return False
list_input=[]
while True:
    num=input("请输入数字：")
    if not num:
        break
    list_input.append(num)
print(comparison_element(list_input))
