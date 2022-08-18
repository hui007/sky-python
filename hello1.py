# 模块注释。Copyright 2020 sky。

"""文档注释-单行，可以被pydoc工具从源代码中提取这些信息，生成html文件"""
"""文档注释-多行，第一行后如果还有注释内容，应该加一个空行

剩余的多行文档注释。注释结束行应该单独占据一行。
"""

# import模块。模块就是一个文件，是保存代码的最小单元。模块提供一种命名空间，同一个模块不允许有相同的变量名，但不同模块可以。
import module1
from module1 import m1

# import包。适用于模块名冲突的情况。如果模块名相同，则可以考虑划分到不同包。
import com.sky.pkg1.hello1 as mhello

# \表示续行符，但是要避免使用。在括号内换行，隐式使用了换行符，所以有时为了避免使用换行符，用括号把表达式括起来。
print("\n命名规范：\n 包名：全部小写，不推荐使用下划线。\n 模块名：全部小写，可以使用下划线隔开。"
      "\n 类名：驼峰法。\n 异常名：类的一种。结尾推荐以Error结尾。\n 变量名：小写字母，可以使用下划线隔开。"
      "\n 函数和方法名：同变量名。\n 常量名：全部大写，用下划线隔开。\n")

print('**演示变量-start**')
string = "hello world"
string = 1
print("动态变量类型。python是动态类型语言。不检查变量类型，可以改变变量类型。str改为整数：", string)
print("来自模块module1:str=" + module1.string)
print("来自模块module1:m1=" + m1)
print("来自不同包的同名模块hello1：str=" + mhello.string)
print('**演示变量-end**')

# 语句可以加分号，也不要不加分号，推荐不加分号。比如可以写成不推荐形式 name1 = "Tom";name2 = "Tony";
print('\n**演示赋值和条件语句-start**')
name1 = "Tom"
name2 = "Tony"
a = b = c = 10  # 链式赋值
# 语句不是靠花括号，而是靠缩进来组织
if a > 10:
    print("\nif a bigger than 10")
else:
    print("演示if语句。 hello ", a)
print('**演示赋值和条件语句-end**\n')

# TODO IDE支持的todo注释，非官方提供的。以下演示数据类型，后续可以移到单独的模块里
# Python里所有的数据类型都是类，每一个变量都是类的实例

# 整型。Python3不再区分整数和长整数
i1 = 28
i2 = 0b11100
i3 = 0B11100
i4 = 0o34
i5 = 0O34
i6 = 0x1c
i7 = 0X1c
print(
    "演示整型。\ni1=",
    i1,
    "0b11100=",
    i2,
    "0B11100=",
    i3,
    "0o34=",
    i4,
    "0O34=",
    i5,
    "0x1c=",
    i6,
    "0X1c=",
    i7)

# 浮点数。类型为float，只支持双精度的，且与本机相关
f1 = 1.1
f2 = 3.36e2
f3 = 3.36e-2
print("演示浮点型。\nf1=", f1, "3.36e2=", f2, "3.36e-2=", f3)

# bool类型。bool是int的子类，它只有两个值True和False。任何数据类型都可以通过bool()函数转换为bool值。
b1 = True
b2 = False
print("演示bool型。\nTrue=", b1, "False=", b2,)

# 类型转换。隐式类型转换、显式类型转换。
print('\n**类型转换-start**')
print("1+True=", 1 + True, "1+2.0=", 1 + 2.0, "type(1+2.0)=", type(1 + 2.0))
print(
    "int(False)=",
    int(False),
    "int(19.6)=",
    int(19.6), "16进制转换为int。int('AB',16)=", int('AB', 16),
    "float(5)=",
    float(5))
print(
    "bool(0)=",
    bool(0),
    "bool(1)=",
    bool(1),
    "bool('')=",
    bool(''),
    "bool('  ')=",
    bool('  '),
    "bool([])=",
    bool(
        []),
    "bool(())=",
    bool(()))
print('str(3.24)=', str(3.24), 'str(True)=',
      str(True), 'str([1,2,3])=', str([1, 2, 3]))
print('**类型转换-end**\n')
# 普通字符串和原始字符串。原始字符串是在字符串前面加r，直接按照字面意思来使用，没有转义字符
str1 = "Hello str1"
str2 = 'Heloo str2'
str3 = "\u0048 str3"
str4 = "Hello\n 换行"
str5 = "Hello\t 水平制表符"
str6 = 'Hello\'转义1'
str7 = 'Hello\\转义2'
str8 = 'Hello \u0064 转义3'
print(
    "演示字符串1。\nHello str1=",
    str1,
    "Heloo str2=",
    str2,
    r"\u0048 str3=",
    str3,
    r"Hello\n 换行=",
    str4)
print(
    "演示字符串2。\n",
    r"Hello\t 水平制表符=",
    str5,
    r"Hello\'转义1=",
    str6,
    r"Hello\\转义2=",
    str7,
    r"Hello\u005c转义3=",
    str8)

# 长字符串。可输出排版字符，如果包含特殊字符，也需要转义
str9 = '''Hello\tworld
长字符串
'''
print("演示长字符串。\n长字符串str9=", str9)

# 字符串格式化
name = 'Mary'
age = 18
money = 1234.5678
print('**字符串格式化-start**')
print("{0}的年龄是{1}".format(name, age))
print("{1}的年龄是{0}".format(age, name))
print("{n}的年龄是{a}".format(a=age, n=name))
print("{0}的年龄是{1:d}".format(name, age + 1))
print("{0}的年龄是{1:5d}".format(name, age + 5))
print("{0}今天收入是{1:f}".format(name, money))
print("{0}今天收入是{1:.2f}".format(name, money))
print("{0}今天收入是{1:10.2f}".format(name, money))  # 小数+整数合起来10位
print("{0}今天收入是{1:g}".format(name, money))  # 整数或浮点数
print("{0}今天收入是{1:G}".format(name, money))  # 整数或浮点数
print("{0}今天收入是{1:e}".format(name, money))  # 科学计数法
print("{0}今天收入是{1:E}".format(name, money))  # 科学计数法
print("十进制数{0:d}的八进制为{0:o}，十六进制为{0:x}或{0:X}".format(age))
print('**字符串格式化-end**')

# 字符串查找。rfind所以匹配的子字符串的最右串的开始位置
string = 'this is a string search example'
print('\n**字符串查找-start**')
print("find i：{0}".format(string.find('i')))
print("rfind i：{0}".format(string.rfind('i')))
print("find i。start index=4：{0}".format(string.find('i', 4)))
print('**字符串查找-end**')
