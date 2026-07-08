# 购物车管理系统
shopping_cart = {}

menu = """
=============== 购物车管理系统 ===============
#        1. 添加商品至购物车                 #
#        2. 更新购物车商品信息               #
#        3. 移除购物车指定商品               #
#        4. 查看当前购物车清单               #
#        5. 退出管理系统                    #
===========================================
"""

print("欢迎进入购物车管理系统")
while True:
    print(menu)
    choice = input("请输入序号进行操作：")
    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品单价："))
            goods_num = int(input("请输入采购数量："))
            if goods_name in shopping_cart:
                print("警告：该商品已存在于购物车，请勿重复添加")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品信息录入成功")
        case "2":  # 修改购物车
            goods_name = input("请输入需要修改的商品名称：")
            if goods_name not in shopping_cart:
                print("错误：未查询到该商品，更新失败")
            else:
                new_price = float(input("请输入更新后的商品单价："))
                new_num = int(input("请输入更新后的采购数量："))
                shopping_cart[goods_name]={"price": new_price, "num": new_num}
                print("商品数据更新完成")
        case "3":  # 删除购物车
            goods_name = input("请输入待移除的商品名称：")
            if goods_name not in shopping_cart:
                print("错误：目标商品不存在，移除操作无效")
            else:
                del shopping_cart[goods_name]
                print("指定商品已成功移出购物车")
        case "4":  # 查询购物车
            print("----------当前购物车商品清单----------")
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name}，商品单价：{goods_info['price']}，采购数量：{goods_info['num']}")
            print("--------------------------------------")
        case "5":  # 退出购物车
            print("系统即将退出，感谢使用！")
            break
        case _:  # 匹配其他所有情况
            print("输入无效,请选择1-5范围内的功能编号")