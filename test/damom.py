dict_goods_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
list_order = []
list_singel_goods = []
def shopping():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()
def settlement():
    total_money = get_total_money()
    accounting(total_money)
def accounting(total_money):
    while True:
        money = float(input("总价%d元，请输入金额：" % total_money))
        if money >= total_money:
            print("购买成功，找回：%d元。" % (money - total_money))
            list_order.clear()
            break
        else:
            print("金额不足.")
def get_total_money():
    total_money = 0
    for item in list_order:
        shang_pin = dict_goods_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
        total_money += shang_pin["price"] * item["count"]
    return total_money
def buying():
    showing_goods()
    creat_single_order()
    list_order.append(list_singel_goods)
    print("添加到购物车。")
def creat_single_order():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_goods_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    list_singel_goods.append({"cid": cid, "count": count})
def showing_goods():
    for key, value in dict_goods_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
shopping()
