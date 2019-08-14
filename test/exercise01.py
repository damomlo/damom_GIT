"""
在控制台中录入一个成绩，判断等级（优秀、良好、及格、不及格）
"""
def print_grade_level(grade_input):
    """
    根据输入的成绩评判等级
    :param grade_input: int 成绩
    :return: 返回出对应的等级
    """
    if int(grade_input)>100 or int(grade_input)<0:
      return "成绩有误"
    if int(grade_input) >= 90:
      return"成绩优秀！"
    if 75 <= int(grade_input):
      return"成绩良好！"
    if 60 <= int(grade_input) :
      return"成绩合格！"
    return"成绩不及格！"
grade =int(input("请输入成绩："))
print(print_grade_level(grade))