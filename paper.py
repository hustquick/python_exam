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

def generate_paper(exam_window):
    # 读取Excel表格
    df = read_excel()
    # 获取选择题和判断题
    choice_questions = df.loc[df['question_type'] == 'choice']
    judge_questions = df.loc[df['question_type'] == 'judge']

    # 随机抽取题目
    choice_questions = choice_questions.sample(frac=1).reset_index(drop=True)
    judge_questions = judge_questions.sample(frac=1).reset_index(drop=True)

    # 创建题目标签和选项复选框的变量
    question_label = tk.Label(exam_window, text='')
    choice_var = tk.IntVar()
    choice_var.set(-1)  # 初始值为-1，表示未选择

    # 当前题目索引
    current_question = 0

    # 存储学生答案的列表
    student_answers = []

    def show_question():
        nonlocal current_question
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

        question_label.config(text=question)
        question_label.pack()

        for widget in exam_window.winfo_children():
            if isinstance(widget, tk.Radiobutton) or isinstance(widget, tk.Checkbutton):
                widget.pack_forget()

        if question_type == 'choice':
            for i, option in enumerate(options):
                choice_radio = tk.Radiobutton(exam_window, text=option, variable=choice_var, value=i + 1)
                choice_radio.pack()
        elif question_type == 'judge':
            judge_radio1 = tk.Radiobutton(exam_window, text=options[0], variable=choice_var, value=1)
            judge_radio1.pack()
            judge_radio2 = tk.Radiobutton(exam_window, text=options[1], variable=choice_var, value=2)
            judge_radio2.pack()

    def submit_answer():
        nonlocal current_question
        answer = choice_var.get()
        if answer == -1:
            messagebox.showerror('错误', '请选择一个选项')
        else:
            # 存储学生的答案
            student_answers.append(answer)  # Add the answer to the list
            print(f'学生答案: {answer}')

            current_question += 1
            if current_question < len(choice_questions) + len(judge_questions):
                show_question()
            else:
                messagebox.showinfo('提示', '试卷已完成')
                return student_answers  # Return the list of answers when the exam is done

    show_question()

    submit_button = tk.Button(exam_window, text='提交答案', command=submit_answer)
    submit_button.pack()
