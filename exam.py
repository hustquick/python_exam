import tkinter as tk
from tkinter import messagebox
import calculate

# 考试窗口
def exam_window(paper_id, student_id):
    window = tk.Toplevel()
    window.title('考试界面')
    # 显示试卷
    show_paper(paper_id, window)
    # 完成答题按钮
    tk.Button(window, text='完成答题', command=lambda: submit_paper(paper_id, student_id, window)).place(x=150, y=250)

# 显示试卷
def show_paper(paper_id, window):
    # 读取本地试卷
    with open(f'papers/paper{paper_id}.txt') as f:
        paper = f.read()
    # 在窗口上显示试卷内容
    text = tk.Text(window, height=15, width=30)
    text.insert(tk.END, paper)
    text.place(x=20, y=20)
    # 提示学生在下方填写答案
    tk.Label(window, text='请在下方填写答案:').place(x=20, y=200)
    window.text = text  # 保存text对象的引用

# 提交试卷
# 提交试卷
def submit_paper(paper_id, student_id, window):
    # 获取学生的答案
    student_answers = window.student_answers
    # 将学生的答案保存到本地
    with open(f'answers/answers{student_id}.txt', 'w') as f:
        for question_index, answer in student_answers.items():
            f.write(f'{question_index},{answer}\n')
    # 计算学生的得分
    score = calculate.calculate_score(paper_id, student_id)
    # 在窗口上显示分数
    score_label = tk.Label(window, text=f'您的得分是:{score}分')
    score_label.place(x=50, y=250)
    window.destroy()

# 获取学生的答案
def get_answers(window):
    # 获取填写在文本框中的答案
    text = window.text
    answers = text.get(1.0, tk.END)
    return answers
