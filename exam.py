import tkinter as tk
from tkinter import messagebox
import calculate

def exam_window(paper_id, student_id):
    window = tk.Toplevel()
    window.title('考试界面')
    show_paper(paper_id, window)
    window.student_answers = tk.StringVar()  # Create a variable to hold student's answers
    tk.Entry(window, textvariable=window.student_answers).place(x=20, y=220)  # Add an entry for answers
    tk.Button(window, text='完成答题', command=lambda: submit_paper(paper_id, student_id, window)).place(x=150, y=250)

def show_paper(paper_id, window):
    with open(f'papers/paper{paper_id}.txt') as f:
        paper = f.read()
    text = tk.Text(window, height=15, width=30)
    text.insert(tk.END, paper)
    text.place(x=20, y=20)
    tk.Label(window, text='请在下方填写答案:').place(x=20, y=200)

def submit_paper(paper_id, student_id, window):
    student_answers = window.student_answers.get()  # Get student's answers
    with open(f'answers/answers{student_id}.txt', 'w') as f:
        f.write(student_answers)
    score = calculate.calculate_score(student_id)
    messagebox.showinfo('分数', f'您的得分是:{score}分')  # Show score before destroying the window
    window.destroy()
