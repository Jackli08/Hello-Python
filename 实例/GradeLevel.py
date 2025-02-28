score = eval(input('成绩：'))
if score >= 60:
    grade = "D"
    if score >= 70:
        grade = 'C'
        if score >= 80:
            grade = 'B'
            if score >= 90:
                grade = 'A'
print("输入成绩属于级别{}".format(grade))