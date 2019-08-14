"""
在控制台获取一个月份、年份；
打印当月的天数。
"""
def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def calculate_day(year,month):
    if month<1 or month>12:
        return 0
    if month in (1,3,5,7,8,10,12):
        return 31
    if month==2:
        return 29 if leap_year(year) else 28
    return 30
year=int(input("请输入年份："))
month=int(input("请输入月份："))
print(calculate_day(year,month))