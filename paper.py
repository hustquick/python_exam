import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox


# 定义问题生成器，用于产生问题的初始数据
def linear_equation_generator():
    return {'a': random.randint(1, 10), 'b': random.randint(1, 10)}


# 暂时只添加了一个问题，你可以按照格式添加更多
programming_questions = [
    {
        'question': '求解线性方程组',
        'data_generator': linear_equation_generator
    },
    # 添加更多题目
]


# 读取Excel表格
def read_excel():
    excel_path = 'questions.xlsx'  # 根据实际情况修改路径
    df = pd.read_excel(excel_path)

    for pq in programming_questions:
        new_df = pd.DataFrame([{
            'question_type': 'programming',
            'question': pq['question'],
            'data_generator': pq['data_generator']
        }])

        df = pd.concat([df, new_df], ignore_index=True)
    return df


# 生成试卷
def generate_paper(exam_window):
    df = read_excel()
    choice_questions = df.loc[df['question_type'] == 'choice']
    judge_questions = df.loc[df['question_type'] == 'judge']
    programming_questions = df.loc[df['question_type'] == 'programming']

    choice_questions = choice_questions.sample(n=10).reset_index(drop=True)
    judge_questions = judge_questions.sample(n=10).reset_index(drop=True)
    programming_questions = programming_questions.sample(n=4).reset_index(drop=True)

    question_label = tk.Label(exam_window, text='')
    choice_var = tk.IntVar()

    student_answers = {}
    current_question = 0

    def show_question():
        nonlocal current_question
        choice_var.set(-1)
        if current_question < len(choice_questions):
            question_type = 'choice'
            question = choice_questions.iloc[current_question]['question']
            options = [choice_questions.iloc[current_question]['option1'],
                       choice_questions.iloc[current_question]['option2'],
                       choice_questions.iloc[current_question]['option3'],
                       choice_questions.iloc[current_question]['option4']]
        elif current_question < len(choice_questions) + len(judge_questions):
            question_type = 'judge'
            question_index = current_question - len(choice_questions)
            question = judge_questions.iloc[question_index]['question']
            options = ['正确', '错误']
        else:
            question_type = 'programming'
            question_index = current_question - len(choice_questions) - len(judge_questions)
            question = programming_questions.iloc[question_index]['question']
            data = programming_questions.iloc[question_index]['data_generator']()
            options = ['数据：{}'.format(data)]

        question_label.config(text=f'{current_question + 1}. {question}')
        question_label.pack()

        for widget in exam_window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.pack_forget()

        for i, option in enumerate(options):
            choice_radio = tk.Radiobutton(exam_window, text=option, variable=choice_var, value=i + 1)
            choice_radio.pack()

    def previous_question():
        nonlocal current_question
        if current_question > 0:
            current_question -= 1
            show_question()

    def next_question():
        nonlocal current_question
        if current_question < len(choice_questions) + len(judge_questions) + len(programming_questions) - 1:
            current_question += 1
            show_question()

    show_question()

    previous_button = tk.Button(exam_window, text='上一题', command=previous_question)
    previous_button.pack(side='left', padx=20)
    next_button = tk.Button(exam_window, text='下一题', command=next_question)
    next_button.pack(side='right', padx=20)
