import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox

# 读取Excel表格
def read_excel():
    # excel文件的路径
    excel_path = 'questions.xlsx'  # 可以根据实际情况修改路径
    # 读取表格
    df = pd.read_excel(excel_path)
    # 返回读取到的表格数据
    return df

# 生成试卷
# 生成试卷
def generate_paper(exam_window):
    # 读取Excel表格
    df = read_excel()
    # 获取选择题和判断题
    choice_questions = df.loc[df['question_type'] == 'choice']
    judge_questions = df.loc[df['question_type'] == 'judge']

    # 随机抽取题目
    choice_questions = choice_questions.sample(n=10).reset_index(drop=True)
    judge_questions = judge_questions.sample(n=10).reset_index(drop=True)

    # 创建题目标签和选项复选框的变量
    question_label = tk.Label(exam_window, text='')
    choice_var = tk.IntVar()

    # 初始化学生答案字典
    student_answers = {}

    # 当前题目索引
    current_question = 0

    # 显示题目和选项的函数
    def show_question():
        nonlocal current_question
        choice_var.set(-1)  # 确保默认没有选中的选项
        # 获取当前题目的数据
        if current_question < len(choice_questions):
            question_type = 'choice'
            question = choice_questions.iloc[current_question]['question']
            options = [choice_questions.iloc[current_question]['option1'],
                       choice_questions.iloc[current_question]['option2'],
                       choice_questions.iloc[current_question]['option3'],
                       choice_questions.iloc[current_question]['option4']]
        else:
            question_type = 'judge'
            question_index = current_question - len(choice_questions)
            question = judge_questions.iloc[question_index]['question']
            options = ['正确', '错误']

        # 更新题目标签和选项复选框
        question_label.config(text=f'{current_question + 1}. {question}')
        question_label.pack()

        # 清空选项复选框
        for widget in exam_window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.pack_forget()

        # 创建选项复选框
        if question_type == 'choice':
            for i, option in enumerate(options):
                choice_radio = tk.Radiobutton(exam_window, text=option, variable=choice_var, value=i + 1)
                choice_radio.pack()
        elif question_type == 'judge':
            judge_radio1 = tk.Radiobutton(exam_window, text=options[0], variable=choice_var, value=1)
            judge_radio1.pack()
            judge_radio2 = tk.Radiobutton(exam_window, text=options[1], variable=choice_var, value=2)
            judge_radio2.pack()

    # 上一题的函数
    def previous_question():
        nonlocal current_question
        if current_question > 0:
            current_question -= 1
            show_question()

    # 下一题的函数
    def next_question():
        nonlocal current_question
        if current_question < len(choice_questions) + len(judge_questions) - 1:
            current_question += 1
            show_question()

    # 显示第一题
    show_question()

    # 创建提交按钮
    previous_button = tk.Button(exam_window, text='上一题', command=previous_question)
    previous_button.pack(side='left', padx=20)
    next_button = tk.Button(exam_window, text='下一题', command=next_question)
    next_button.pack(side='right', padx=20)

