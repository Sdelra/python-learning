#平均数组成列表

#方法一
# list = []
# for i in range(1,21):
#     list.append(i**2)
# print(list)

#方法二(列表推导式1)
# list = [i**2 for i in range(1,21)]
# print(list)

#求偶数的平方数组成的列表(列表推导式2)
list = [i**2 for i in range(1,21) if i % 2 == 0]
print(list)