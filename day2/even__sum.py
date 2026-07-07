#偶数累加求和
sum = 0
i = 1
num = int(input("请输入数字范围"))
while i<=num:
    if i%2 == 0:
        sum += i
    i += 1
print(sum)