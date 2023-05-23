import pandas as pd

def calculate_score(student_id):
    df = pd.read_excel('questions.xlsx', usecols=['question', 'option1', 'option2', 'option3', 'option4', 'answer'])
    choice_num = df.loc[df['question_type'] == 'choice', 'question_num'].count()
    judge_num = df.loc[df['question_type'] == 'judge', 'question_num'].count()
    try:
        with open(f'answers/answers{student_id}.txt') as f:
            answers = f.read().split()  # Split the answers string by spaces
    except FileNotFoundError:
        print(f"找不到学生{student_id}的答案文件")
        return 0
    if len(answers) != choice_num + judge_num:
        print(f"学生{student_id}的答案数量与试题数量不匹配")
        return 0
    score = 0
    for i in range(choice_num):
        if answers[i] == str(df.loc[df['question_type'] == 'choice', 'answer'].values[i]):
            score += 1
    for i in range(choice_num, choice_num + judge_num):
        if answers[i] == str(df.loc[df['question_type'] == 'judge', 'answer'].values[i-choice_num]):
            score += 1
    return score

def run_calculate(student_id):
    score = calculate_score(student_id)
    print(f'学生{student_id}的得分是: {score}分')
