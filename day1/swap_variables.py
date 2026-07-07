# 交换变量

# 定义初值
a = 100
b = 200
c = 300

# 第一种方法(通用)
t = c
c = a
a = b
b = t
print(f"a={a},b={b},c={c}")

# 第二种方法(python特有)
# c,a,b = a,b,c
# print(f"a={a},b={b},c={c}")
