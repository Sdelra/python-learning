# 登录验证
i = 1
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if i == 5:
        print("输入错误五次，停止操作")
        break
    if username ==" " and password == " ":
        print("用户名和密码不能为空，请重新输入")
        i += 1
        continue
    if username == "admin" and password == "666888":
        print("登陆成功")
        break
    elif username == "zhangsan" and password == "123456":
        print("登陆成功")
        break
    elif username == "taoge" and password == "888666":
        print("登陆成功")
        break
    else:
        print("登陆失败,请重新输入")
        i += 1
