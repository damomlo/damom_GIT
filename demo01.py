"""
    内置可重写函数
        自定义对象 -->  str
"""
class Car:
    def __init__(self, brand="", price=0,max_speed = 0):
        self.brand = brand
        self.price = price
        self.max_speed = max_speed

    # 对人友好的 --> 随心所欲的规定字符串内容
    def __str__(self):
        return "品牌是%s,单价是%d"%(self.brand,self.price)

    # 对解释器友好 --> 根据python语法规定字符串内容
    def __repr__(self):
        return "Car('%s',%d,%d)"%(self.brand,self.price,self.max_speed)

# 应用:将对象显示出来
c01 = Car("宝马",1000000,260)
print(c01) # print(str(c01)) --> print(c01.__str__())
print(c01.__str__())

# 将括号中的字符串,作为python代码执行.
# re = eval("1 + 2")# 3
# repr(c01) -->  c01.__repr__()

# 应用:克隆(重新创建与之前对象数据相同的新对象,克隆对象与原对象互不影响)
c02 = eval(repr(c01))# eval("Car("宝马",1000000,260)")
c01.price = 50
print(c02)#1000000

# 练习:
# 定义技能类(技能名称,攻击比例,持续时间)
# 创建技能对象,直接print.
# 克隆技能对象,体会改变其中一个,不影响另外一个.

















