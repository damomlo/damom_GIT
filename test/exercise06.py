"""
定义列表升序排列函数
列表中所有元素两两比较，发现更小的则交换位置
"""
def ascend_list(list_target):
    for index in range(len(list_target)-1):
        for i in range(index+1,len(list_target)):
            if list_target[index]>list_target[i]:
                list_target[index],list_target[i]=list_target[i],list_target[index]
list_01=[15,7,5,6,9,7,5,41,3]
ascend_list(list_01)
print(list_01)