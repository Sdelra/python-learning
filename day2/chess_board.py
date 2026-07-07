#国际象棋棋盘

# 第一种方法(先排列再排行)
# line = int(input("请输入棋盘行列数"))
# for i in range(1,line+1):
#     for j in range(1,line+1):
#         if (i+j) % 2 == 0:
#             print("▬",end=" ")
#         else:
#             print("▭",end=" ")
#     print()

# 第二种方法(先排行再排列)
line = int(input("请输入棋盘行列数"))
for i in range(1,line+1):
    if i % 2 == 0:
        print("▭",end=" ")
        for j in range(2,line+1):
            if j % 2 == 0:
                print("▬",end=" ")
            else:
                print("▭",end=" ")
    else:
        print("▬",end=" ")
        for j in range(2,line+1):
            if j % 2 == 0:
                print("▭",end=" ")
            else:
                print("▬",end=" ")
    print()