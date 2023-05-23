import pandas as pd
import os

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 生成文件的保存路径
file_path = os.path.join(current_dir, 'questions.xlsx')


# 生成示例题目的 Excel 文件
def generate_example_excel():
    # 示例题目数据
    example_questions = [
        {
            'question': '在Python中，用于获取用户输入的函数是：',
            'option1': 'input()',
            'option2': 'print()',
            'option3': 'scanf()',
            'option4': 'getline()',
            'answer': 'input()',
            'question_type': 'choice',
            'question_num': 1
        },
        {
            'question': '在Python中，以下哪个关键字用于定义函数：',
            'option1': 'def',
            'option2': 'function',
            'option3': 'define',
            'option4': 'func',
            'answer': 'def',
            'question_type': 'choice',
            'question_num': 2
        },
        {
            'question': '在Python中，以下哪个符号用于表示“不等于”：',
            'option1': '==',
            'option2': '!=',
            'option3': '<>',
            'option4': '><',
            'answer': '!=',
            'question_type': 'choice',
            'question_num': 3
        },
        {
            'question': '下面哪个函数可以将字符串转换为整数：',
            'option1': 'int()',
            'option2': 'str()',
            'option3': 'float()',
            'option4': 'eval()',
            'answer': 'int()',
            'question_type': 'choice',
            'question_num': 4
        },
        {
            'question': '在Python中，用于计算一个数的绝对值的函数是：',
            'option1': 'abs()',
            'option2': 'fabs()',
            'option3': 'absolute()',
            'option4': 'value()',
            'answer': 'abs()',
            'question_type': 'choice',
            'question_num': 5
        },
        {
            'question': '下列选项中，哪个是合法的变量名？',
            'option1': '2var',
            'option2': '_var',
            'option3': 'var!',
            'option4': 'var-name',
            'answer': '_var',
            'question_type': 'choice',
            'question_num': 6
        },
        {
            'question': '在Python中，以下哪个关键字用于退出循环？',
            'option1': 'exit',
            'option2': 'break',
            'option3': 'quit',
            'option4': 'continue',
            'answer': 'break',
            'question_type': 'choice',
            'question_num': 7
        },
        {
            'question': '在Python中，用于获取字符串长度的函数是：',
            'option1': 'len()',
            'option2': 'length()',
            'option3': 'size()',
            'option4': 'count()',
            'answer': 'len()',
            'question_type': 'choice',
            'question_num': 8
        },
        {
            'question': '下面哪个操作符用于将两个字符串连接起来？',
            'option1': '+',
            'option2': '*',
            'option3': '&',
            'option4': '%',
            'answer': '+',
            'question_type': 'choice',
            'question_num': 9
        },
        {
            'question': '在Python中，以下哪个数据结构是有序且可变的？',
            'option1': 'tuple',
            'option2': 'set',
            'option3': 'dictionary',
            'option4': 'list',
            'answer': 'list',
            'question_type': 'choice',
            'question_num': 10
        },
        {
            'question': '在Python中，以下哪个方法可以删除列表中的元素？',
            'option1': 'remove()',
            'option2': 'delete()',
            'option3': 'erase()',
            'option4': 'discard()',
            'answer': 'remove()',
            'question_type': 'choice',
            'question_num': 11
        },
        {
            'question': '在Python中，用于生成随机数的模块是：',
            'option1': 'random',
            'option2': 'math',
            'option3': 'statistics',
            'option4': 'numpy',
            'answer': 'random',
            'question_type': 'choice',
            'question_num': 12
        },
        {
            'question': '在Python中，以下哪个关键字用于定义函数：',
            'option1': 'def',
            'option2': 'function',
            'option3': 'define',
            'option4': 'func',
            'answer': 'def',
            'question_type': 'choice',
            'question_num': 13
        },
        {
            'question': '在Python中，以下哪个方法用于对列表进行排序？',
            'option1': 'sort()',
            'option2': 'sorted()',
            'option3': 'order()',
            'option4': 'arrange()',
            'answer': 'sort()',
            'question_type': 'choice',
            'question_num': 14
        },
        {
            'question': '下面哪个操作符用于判断两个值是否相等？',
            'option1': '==',
            'option2': '=',
            'option3': '!=',
            'option4': '<>',
            'answer': '==',
            'question_type': 'choice',
            'question_num': 15
        },
        {
            'question': '在Python中，以下哪个函数用于计算列表中元素的和？',
            'option1': 'sum()',
            'option2': 'total()',
            'option3': 'add()',
            'option4': 'accumulate()',
            'answer': 'sum()',
            'question_type': 'choice',
            'question_num': 16
        },
        {
            'question': '在Python中，以下哪个函数用于返回指定范围内的整数列表？',
            'option1': 'range()',
            'option2': 'list()',
            'option3': 'sequence()',
            'option4': 'integer()',
            'answer': 'range()',
            'question_type': 'choice',
            'question_num': 17
        },
        {
            'question': '在Python中，以下哪个函数用于向列表末尾添加元素：',
            'option1': 'append()',
            'option2': 'insert()',
            'option3': 'extend()',
            'option4': 'update()',
            'answer': 'append()',
            'question_type': 'choice',
            'question_num': 18
        },
        {
            'question': '在Python中，以下哪个函数用于计算一个数的平方根：',
            'option1': 'pow()',
            'option2': 'root()',
            'option3': 'square()',
            'option4': 'sqrt()',
            'answer': 'def',
            'question_type': 'choice',
            'question_num': 19
        },
        {
            'question': '在Python中，以下哪个符号用于表示逻辑与操作：',
            'option1': '&&',
            'option2': '||',
            'option3': '&',
            'option4': '|',
            'answer': '&',
            'question_type': 'choice',
            'question_num': 20
        },
        {
            'question': '在Python中，以下哪个方法用于删除字典中指定的键值对：',
            'option1': 'remove()',
            'option2': 'delete()',
            'option3': 'discard()',
            'option4': 'pop()',
            'answer': 'pop()',
            'question_type': 'choice',
            'question_num': 21
        },
        {
            'question': '在Python中，以下哪个库常用于绘制数据图表：',
            'option1': 'matplotlib',
            'option2': 'numpy',
            'option3': 'scipy',
            'option4': 'sympy',
            'answer': 'matplotlib',
            'question_type': 'choice',
            'question_num': 22
        },
        {
            'question': '在Python中，以下哪个关键字用于引入外部模块或库：',
            'option1': 'include',
            'option2': 'require',
            'option3': 'import',
            'option4': 'use',
            'answer': 'include',
            'question_type': 'choice',
            'question_num': 23
        },
        {
            'question': '在Python中，以下哪个方法用于从列表中获取最大值：',
            'option1': 'max()',
            'option2': 'maximum()',
            'option3': 'largest()',
            'option4': 'get_max()',
            'answer': 'max()',
            'question_type': 'choice',
            'question_num': 24
        },
        {
            'question': '在Python中，以下哪个函数用于将列表反转：',
            'option1': 'reverse()',
            'option2': 'invert()',
            'option3': 'flip()',
            'option4': 'turn()',
            'answer': 'reverse()',
            'question_type': 'choice',
            'question_num': 25
        },
        {
            'question': 'Python是一种解释型语言。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 26
        },
        {
            'question': '列表是Python中唯一的有序数据结构。',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 27
        },
        {
            'question': '在Python中，函数可以返回多个值。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 28
        },
        {
            'question': 'Python中的字典是无序的数据结构。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 29
        },
        {
            'question': '在Python中，for循环只能用于遍历列表。',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 30
        },
        {
            'question': 'Python中的元组是可变的数据结构。',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 31
        },
        {
            'question': '在Python中，可以使用单引号或双引号表示字符串。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 32
        },
        {
            'question': 'Python中的集合是有序的数据结构。',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 33
        },
        {
            'question': 'Python中的while循环可以根据条件重复执行代码块。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 34
        },
        {
            'question': 'Python中的布尔数据类型只有两个取值：True和False。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 35
        },
        {
            'question': 'Python中的切片操作可以用于列表、字符串和元组。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 36
        },
        {
            'question': '在Python中，变量的数据类型在声明时就确定了，不能更改。',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 37
        },
        {
            'question': 'Python中的字典使用花括号{}来表示。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 38
        },
        {
            'question': 'Python中的函数可以作为参数传递给其他函数。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 39
        },
        {
            'question': 'Python中的while循环条件可以是任意表达式。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 40
        },
        {
            'question': 'Python中的列表可以存储任何类型的数据。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 41
        },
        {
            'question': 'Python中的字典可以存储键值对数据。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 42
        },
        {
            'question': '在Python中，使用continue关键字可以跳过当前循环中的剩余语句。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 43
        },
        {
            'question': '在Python中，使用replace函数可以替换字符串中的某个部分',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 44
        },
        {
            'question': 'Python支持复数类型。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 45
        },
        {
            'question': 'Python的索引从1开始。 ',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 46
        },
        {
            'question': '在Python中，可以使用负数作为索引来访问序列的元素。 ',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 47
        },
        {
            'question': 'Python中的字符串是可变的。 ',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 48
        },
        {
            'question': 'NumPy中的ndarray对象只能存储数字。',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 49
        },
        {
            'question': '在Python中，无论是列表还是元组，都可以通过索引修改其元素。',
            'answer': 'False',
            'question_type': 'judge',
            'question_num': 50
        },
        {
            'question': '在Python中，“/”运算符得到结果一定是浮点数（float）。',
            'answer': 'True',
            'question_type': 'judge',
            'question_num': 51
        },
    ]

    # 将题目数据转换为 DataFrame
    df = pd.DataFrame(example_questions)

    # 重新排列列的顺序
    columns_order = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'question_type', 'question_num']
    df = df[columns_order]

    # 保存 DataFrame 到 Excel 文件
    # df.to_excel('questions.xlsx', index=False)
    # 保存 DataFrame 到 Excel 文件
    df.to_excel(file_path, index=False)

# 运行示例题目的 Excel 生成
if __name__ == '__main__':
    generate_example_excel()
