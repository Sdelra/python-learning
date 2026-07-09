# Python学习日志

> 课程：黑马程序员Python+AI零基础入门到大神
> 仓库：https://github.com/Sdelra/python-learning


## 📅 2026年7月

### 7月6日（第1天）

**学习内容**：P1-P21数据存储与运算（Python简介、环境安装、变量、数据类型、字符串格式化、输入输出、四种运算符）

**今日代码**：约20行
- 交换变量[swap_variables.py](./day1/swap_variables.py)
- 算术运算符[calculate.py](./day1/calculate.py)

**遇到问题**：
- input()获取数字返回字符串类型，参与运算时要先转换为int()

**解决方案**：
- int()强制转换

**额外收获**：
- 查看数据类型除了type()，还有isinstance(数据,类型)，返回布尔值。
- 计算机底层二进制无法准确表示所有小数，则涉及浮点数运算可能损失精度。
- 用//计算结果虽取整但类型与原参与运算数值类型一致。eg:85.0//10=8.0

**明日计划**：P22-P35流程控制语句（if语句、match模式匹配、while循环、for循环、嵌套循环）

---

### 7月7日（第2天）

**学习内容**：P22-P35流程控制语句（if语句、match模式匹配、while循环、for循环、嵌套循环）

**今日代码**：约105行
- match模式匹配[game_cmd.py](./day2/game_cmd.py)
- while循环+if判断[even_sum.py](./day2/even_sum.py)
- for循环+if判断[odd_sum.py](./day2/odd_sum.py)
- for循环+嵌套循环[table99.py](./day2/table99.py)
- for循环+if条件+嵌套循环[chess_board.py](./day2/chess_board.py)
- while循环+if条件+控制循环[login.py](./day2/login.py)
- while循环+if条件+控制循环[guess_num.py](./day2/guess_num.py)

**遇到问题**：
- print自动换行，chess_board.py中黑白格子排布错乱
- 循环控制语句的缩进错误

**解决方案**：
- print添加end=" ",同一行横向打印
- break和continue缩进应在循环内部

**额外收获**：
- range(start,end,step)左包含右不包含。
- shift+回车 可以无视光标位置快速创建下一行。
- match模式匹配中case后可以直接加条件判断 eg:case "/" if num2 != 0
- 生成随机数用 import random

              random_number = random.randint(num1,num2) #左右都包含

**明日计划**：P36-P56数据容器（列表list、字符串str、元组tuple、集合set、字典dict）

---

### 7月8日（第3天）

**学习内容**：P36-P56数据容器（列表list、字符串str、元组tuple、集合set、字典dict）

**今日代码**：约220行
- 列表list+for循环[list_max_min_average.py](./day3/list_max_min_average.py)
- 列表list+if条件[square_num_list.py](./day3/square_num_list.py)
- 字符串str+if条件[judge_palindrome.py](./day3/judge_palindrome.py)
- 列表list+元组tuple+for循环[score_table.py](./day3/score_table.py)
- 字典dict+while循环+if条件+控制循环+for循环+match模式匹配[shopping_cart_system.py](./day3/shopping_cart_system.py)
- 字典dict+while循环+if条件+控制循环+for循环+match模式匹配[edu_manage_system.py](./day3/edu_manage_system.py)

**遇到问题**：
- 定义单元素元组时，类型测出来不是元组
- 对于一个key能查出多个信息的字典的定义写法不对
- edu_manage_system.py文件中第6项，已经算出了最高分，但不知道这些分是哪些学生考的，在嵌套字典中知道内部的value,不知道怎么求外部的kay

**解决方案**：
- 定义单元素元组时，需要在结尾加上逗号 eg:a=(100,)
- 采用嵌套字典来定义 eg:shopping_cart = {"apple": {"price": 5, "num": 2}}
- 1）. 准备一个空名单（比如叫max_names），用来装“考了最高分的人”。
2）. 从头到尾遍历大字典（遍历items()，一次拿出“姓名”和“他的成绩字典”）。
3）. 在遍历过程中，只看这个学生的“语文”成绩。
4）. 拿这个成绩跟刚才算出来的“最高分”做比较。如果相等，说明这个学生就是最高分得主，把他的姓名放进max_names名单里。如果不相等，就跳过，看下一个学生。不能用if找到第一个就停下来，必须把整个大字典全部遍历完，把所有成绩并列最高的学生姓名都装进那个名单里。遍历结束后，max_names名单里装的就是所有并列第一的学生姓名。

**额外收获**：
- 合并列表除了用+和extend()还可以用*解包后再组包 eg:lst=[*lst1,*lst2]
- 列表推导式：[要插入的值 for i in 列表/序列 if 条件语句]
- index(数据，起始下标，结束下标)第一次出现位置，insert(位置，内容)插入
- 交集：s3=s1.intersection(s2)或s3=s1&s2
- 并集：s3=s1.union(s2)或s3=s1|s2
- 差集：s3=s1.difference(s2)或s3=s1-s2
- 字典kay为不可变类型且不能重复（若重复则后面的值覆盖前面的值），值可变
- alt+shift同时拖动光标可以并列编辑

**明日计划**：P57-P70函数基础+进阶（函数的定义与调用、参数与返回值、变量作用域（局部vs全局）、默认参数与不定长参数的使用场景）

---

### 7月9日（第4天）

**学习内容**：P57-P70函数基础+进阶（函数的定义与调用、参数与返回值、变量作用域（局部vs全局）、默认参数与不定长参数的使用场景）

**今日代码**：约60行
- 函数定义调用+不定长参数函数+if条件+函数解释[calc_statistics.py](./day4/calc_statistics.py)
- 匿名函数[lambda_str_sort.py](./day4/lambda_str_sort.py)
- 函数递归[recursion_factorial.py](./day4/recursion_factorial.py)
- 函数定义调用+if条件+函数解释[order_calc_args.py](./day4/order_calc_args.py)

**遇到问题**：
- 有些函数的用法知道的不全，例如lambda_str_sort.py文件中sort()的使用

**解决方案**：
- ctrl+单击 查看函数较完整的使用规则

**额外收获**：
- 传参方式中，位置参数在前，关键字参数在后 eg:a = b(wan,34,city="北京”，gender="女")
- 默认参数放在没有设置默认值的参数的后面 eg:def a(name,age,gender,city="北京")
- round(数值，保留小数位数)
- 不定长参数中，位置传参用*args,合并封装为元组。关键字传参用**kwargs,合并封装为字典。
- 匿名函数 变量名=lambda 参数列表 : 函数体

**明日计划**：P71-P76类型注解+模块（函数类型注解、导入、自定义、包）

---