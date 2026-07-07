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