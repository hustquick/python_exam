import tkinter as tk
from tkinter import messagebox

# 登陆窗口
def login_window():
    window = tk.Tk()
    window.title('学生登陆')
    window.geometry('200x100')
    # 学号label和输入框
    tk.Label(window, text='学号:').place(x=30, y=20)
    var_student_id = tk.StringVar()
    entry_student_id = tk.Entry(window, textvariable=var_student_id)
    entry_student_id.place(x=70, y=20)
    # 开始答题按钮
    tk.Button(window, text='开始答题', command=lambda: start_exam(var_student_id.get(), window)).place(x=35, y=50)
    window.mainloop()

def start_exam(student_id, window):
    if not student_id:
        messagebox.showerror('错误', '请输入学号!')
    else:
        # Generate exam paper for this student and start exam
        # TODO: Call function to generate exam paper
        print(f"Starting exam for student: {student_id}")

if __name__ == '__main__':
    # 运行login窗口
    login_window()
