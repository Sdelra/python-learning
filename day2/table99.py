#九九乘法表
for i in range(10):
    for j in range(i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()