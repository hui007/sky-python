# 引用其他模块。模块就是一个文件，是保存代码的最小单元。模块提供一种命名空间，同一个模块不允许有相同的变量名，但不同模块可以。
import module1
from module1 import m1

# 引用其他包。如果模块名相同，则可以考虑划分到不同包。
import com.sky.pkg1.hello as mHello

str = "hello world"
print(str)

# 语句可以加分号，也不要不加分号，推荐不加分号。比如可以写成不推荐形式 name1 = "Tom";name2 = "Tony";
name1 = "Tom"
name2 = "Tony"

a = b = c = 10  # 链式赋值

# 语句不是靠花括号，而是靠缩进来组织
if a > 10:
    print("a bigger than 10")
else:
    print("hello ", a)

print("来自模块module1:str=" + module1.str)
print("来自模块module1:m1=" + m1)
print("来自不同包的同名模块：str="+mHello.str)
