#计算n的阶乘
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)
    
result = jc(10)
print(result)