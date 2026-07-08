#列表最值与平均数
lst = []
for i in range(10):
    num = int(input("请输入十个数字"))
    lst.append(num)
lst.sort()
print(f"最小值是{lst[0]}")  #min(lst)
print(f"最大值是{lst[-1]}") #max(lst)
average = sum(lst)/len(lst)
print(f"平均值为{average}")
