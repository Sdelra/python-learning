#奇数累加求和
sum = 0
num = int(input("请输入数字范围"))
for i in range(num):
    if i % 2 != 0:
        sum += i
print(sum)