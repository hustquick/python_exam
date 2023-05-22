import pandas as pd

# 计算学生的得分
def calculate_score(student_id):
    df = pd.read_excel('questions.xlsx', usecols=['question', 'option1', 'option2', 'option3', 'option4', 'answer'])
    choice_num = df.loc[df['question_type'] == 'choice', 'question_num'].count()
    judge_num = df.loc[df['question_type'] == 'judge', 'question_num'].count()
    try:
        with open(f'answers/answers{student_id}.txt') as f:
            answers = f.read()
    except FileNotFoundError:
        print(f"找不到学生{student_id}的答案文件")
        return 0
    answer_list = answers.split()
    if len(answer_list) != choice_num + judge_num:
        print(f"学生{student_id}的答案数量与试题数量不匹配")
        return 0
    score = 0
    for i in range(choice_num):
        if answer_list[i] == str(df.loc[df['question_type'] == 'choice', 'answer'].values[i]):
            score += 1
    for i in range(choice_num, choice_num + judge_num):
        if answer_list[i] == str(df.loc[df['question_type'] == 'judge', 'answer'].values[i-choice_num]):
            score += 1
    return score

# 运行分数计算
def run_calculate(student_id):
    score = calculate_score(student_id)
    print(f'学生{student_id}的得分是: {score}分')
