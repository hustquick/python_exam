import tkinter as tk
from tkinter import messagebox
import login
import paper

exam_window = None

def start_exam():
    global exam_window
    student_id = student_id_entry.get()
    if not student_id:
        messagebox.showerror('错误', '请输入学号!')
    elif exam_window is not None:
        messagebox.showinfo('提示', '试卷窗口已经打开，请完成当前试卷!')
    else:
        exam_window = tk.Toplevel(main_window)
        exam_window.title('试卷')
        generate_paper(exam_window)  # 将exam_window作为参数传递给generate_paper()函数


def generate_paper(exam_window):
    paper_content = paper.generate_paper(exam_window)
    paper_label = tk.Label(exam_window, text=paper_content)
    paper_label.pack()

if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title('Python考试系统')

    # 添加组件
    welcome_label = tk.Label(main_window, text='欢迎使用Python考试系统', font=('Arial', 16))
    welcome_label.pack(pady=20)

    student_id_label = tk.Label(main_window, text='请输入学号:', font=('Arial', 14))
    student_id_label.pack()

    student_id_entry = tk.Entry(main_window, font=('Arial', 14))
    student_id_entry.pack(pady=10)

    start_exam_button = tk.Button(main_window, text='开始答题', font=('Arial', 14), command=start_exam)
    start_exam_button.pack(pady=20)

    main_window.mainloop()
