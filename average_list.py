kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_subject = [kor_score, math_score, eng_score]
student_score = [0,0,0,0,0]

for student in range(0,5):
    for subject in midterm_subject:
        student_score[student] += subject[student]

a, b, c, d, e = student_score
student_average = [a/3, b/3, c/3, d/3, e/3]
print(student_average)