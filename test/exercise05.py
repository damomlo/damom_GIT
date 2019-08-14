"""
定义矩阵转置函数
定义方阵转置函数
"""
def matrix_transpose(list_target01,list_target02):
    for r in range(length_list01):
        list_target02.append([])
        for i in range(length_list_rectangle):
            list_target02[r].append(list_target01[i][r])
    return list_target02
list_transpose_rectangle=[]
list_rectangle=[]
length_list_rectangle=int(input("请输入二维列表的长度："))
length_list01=int(input("请输入二维列表中一维列表的长度："))
for length in range(length_list_rectangle):
    list01 = []
    for i in range(length_list01):
        num=input("请输入数字:")
        list01.append(num)
    list_rectangle.append(list01)
print(matrix_transpose(list_rectangle,list_transpose_rectangle))
