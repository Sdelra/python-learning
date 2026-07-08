#教务管理系统
students_info = {}
print("欢迎来到教务管理系统！")
while True:
    menu = """
    =========== 教务管理系统 ===========
    #         1.添加学生信息           #
    #         2.修改学生信息           #
    #         3.删除学生信息           #
    #         4.查询学生信息           #
    #         5.列出所有学生           #
    #         6.统计班级成绩           #
    #         7.退出系统              #
    ==================================
    """
    print(menu)
    choice = input("请输入查询的序号：")
    match choice:
        case "1":
            name = input("请输入名字：")
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
            if name in students_info:
                print("已有该学生姓名，录入失败")
            else:
                students_info[name] = {"语文":chinese,"数学":math,"英语":english}
                print("信息录入成功")
        case "2":
            name = input("请输入需要修改的学生姓名：")
            if name not in students_info:
                print("输入错误，未有该学生姓名")
            else:
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))
                students_info[name] = {"语文": chinese, "数学": math, "英语": english}
                print("信息修改成功")
        case "3":
            name = input("请输入需要删除的学生姓名:")
            if name not in students_info:
                print("输入错误，未有该学生姓名")
            else:
                del students_info[name]
        case "4":
            name = input("请输入需要查询的学生姓名:")
            if name not in students_info:
                print("输入错误，未有该学生姓名")
            else:
                print(f'{name} 语文：{students_info[name]["语文"]}\
                数学：{students_info[name]["数学"]}\
                英语：{students_info[name]["英语"]}')
        case "5":
            for i in students_info.keys():
                print(f'{i} 语文：{students_info[i]["语文"]}\
                数学：{students_info[i]["数学"]}\
                英语：{students_info[i]["英语"]}')
        case "6":
            if len(students_info) == 0:
                print("暂无学生数据，无法统计！")
            else:
                chinese_score = []
                math_score = []
                english_score = []
                for stu_name, score_dict in students_info.items():
                    chinese_score.append((score_dict["语文"], stu_name))
                    math_score.append((score_dict["数学"], stu_name))
                    english_score.append((score_dict["英语"], stu_name))

                chinese_max_score, chinese_max_name = max(chinese_score, key=lambda x: x[0])
                chinese_min_score, chinese_min_name = min(chinese_score, key=lambda x: x[0])
                chinese_avg = sum([item[0] for item in chinese_score]) / len(chinese_score)

                math_max_score, math_max_name = max(math_score, key=lambda x: x[0])
                math_min_score, math_min_name = min(math_score, key=lambda x: x[0])
                math_avg = sum([item[0] for item in math_score]) / len(math_score)

                english_max_score, english_max_name = max(english_score, key=lambda x: x[0])
                english_min_score, english_min_name = min(english_score, key=lambda x: x[0])
                english_avg = sum([item[0] for item in english_score]) / len(english_score)

                print("========班级成绩统计结果========")
                print(
                    f"语文：最高分 {chinese_max_score}({chinese_max_name})，\
                    最低分 {chinese_min_score}({chinese_min_name})，\
                    平均分 {chinese_avg:.2f}")
                print(
                    f"数学：最高分 {math_max_score}({math_max_name})，\
                    最低分 {math_min_score}({math_min_name})，\
                    平均分 {math_avg:.2f}")
                print(
                    f"英语：最高分 {english_max_score}({english_max_name})，\
                    最低分 {english_min_score}({english_min_name})，\
                    平均分 {english_avg:.2f}")
        case "7":
            print("再见喽")
            break
        case _ :
            print("请正确输入序号1-7")

