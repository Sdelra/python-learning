def calc_order_cost(*args, coupon=0, score=0, express=0.0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量） ---- 如：("鼠标", 188, 2), ("键盘", 388, 1)
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    #订单的总金额=商品总金额-优惠券-积分抵扣+运费
    #计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    #扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    #扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    #添加运费
    total_cost += express
    return total_cost

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), express=9.9)
print(total)