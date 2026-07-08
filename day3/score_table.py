#成绩表
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "通天", 66, 59, 72)
)
#计算每个学生总分，各科平均分，然后一并输出
#方法一（可读性略差）
# for i in students:
#     total = sum(i[2:5])
#     average = total/3
#     print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t {average:.1f}")
#方法二（可读性较好）
for id,name, chinese, math, english in students:
    total = chinese + math + english
    average = total/3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {average:.1f}")

#统计各科成绩最低分，最高分，平均分，并输出
chiese = []
math = []
english = []
for j in students:
    chiese.append(j[2])
    math.append(j[3])
    english.append(j[4])
print(f"语文最高{max(chiese)},最低{min(chiese)},平均分{sum(chiese)/len(chiese)}\n\
数学最高{max(math)},最低{min(math)},平均分{sum(math)/len(math)}\n\
英语最高{max(english)},最低{min(english)},平均分{sum(english)/len(english)}")
