#### 一、模块（Module）

- 模块就是一个 `.py` 文件，里面包含函数、类、变量等
- 使用模块前必须先导入，再使用

**导入方式**：

| 导入形式 | 代码样例 | 调用方式 |
|---------|---------|---------|
| `import 模块名` | `import random, os` | `模块名.功能名()` |
| `import 模块名 as 别名` | `import random as rd` | `别名.功能名()` |
| `from 模块名 import 功能名` | `from random import randint` | `功能名()` |
| `from 模块名 import 功能名 as 别名` | `from random import randint as rint` | `别名()` |
| `from 模块名 import *` | `from random import *` | `功能名()` |


#### 二、包（Package）

- 包是一个文件夹，里面可以存放多个Python模块（`.py`文件）
- 包的作用：对模块进行分类管理，避免命名冲突

**`__init__.py` 的作用**：
- 标识这是一个包，而不是普通文件夹
- 可以控制 `from 包名 import *` 时导入哪些模块（通过 `__all__` 变量）

**包的导入方式**：

| 导入形式 | 调用方式 |
|---------|---------|
| `import 包名.模块名` | `包名.模块名.功能名()` |
| `from 包名 import 模块名` | `模块名.功能名()` |
| `from 包名 import *` | `模块名.功能名()`（需配合 `__all__`） |
| `from 包名.模块名 import 功能名` | `功能名()` |


#### 三、`__name__` 与 `__all__`

**`__name__`**：
- 当模块**直接运行**时，`__name__` 的值为 `"__main__"`
- 当模块**被导入**时，`__name__` 的值为模块文件名（不含 `.py`）
- 常用写法：`if __name__ == "__main__":` 让代码只在直接运行时执行，被导入时不执行

**`__all__`**：
- 控制 `from 模块名 import *` 时导入哪些功能
- 在模块中定义 `__all__ = ['函数名1', '函数名2']`
- 注意：`__all__` 只影响 `import *`，不影响直接导入具体功能


#### 四、类型注解（Type Annotation）

**写法**：

```python
# 变量注解
name: str = "张三"
age: int = 18

# 函数参数和返回值注解
def calc(scores: list[int]) -> float:
    return sum(scores) / len(scores)

# 联合类型（Python 3.10+）
def get_info(flag: str | int) -> None:
    pass