dict_goods_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
order_list = []
def show_goods():
    for key, value in dict_goods_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
def buy():
    show_goods()
    while True:
        cid=get_int_info("商品编号")
        if cid in dict_goods_info:
            break
        print("该商品不存在")
    count = get_int_info("购买数量")
    order_list.append({"cid": cid, "count": count})
    print("添加到购物车。")


def get_int_info(str_target):
    while True:
        try:
            result = int(input("请输入%s："%str_target))
            return result
        except:
            print("%s输入有误，请输入整数"%str_target)


def account(total_money):
    while True:
        money = float(input("总价%d元，请输入金额：" % total_money))
        if money >= total_money:
            print("购买成功，找回：%d元。" % (money - total_money))
            order_list.clear()
            break
        print("金额不足.")
def settlement():
    total_money = 0
    for item in order_list:
        goods = dict_goods_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (goods ["name"], goods ["price"], item["count"]))
        total_money += goods ["price"] * item["count"]
        account(total_money)
def shopping():
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buy()
        elif item == "2":
            settlement()
        else:break
shopping()
