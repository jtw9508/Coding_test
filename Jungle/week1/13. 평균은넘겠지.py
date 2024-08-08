case_nums = int(input())
for i in range(case_nums):
    scores = list(map(int, input().split()))
    total_student = scores[0]
    total_score = 0
    over_mean_student = 0
    for score in scores[1:]:
        total_score += score
    mean_score = total_score/total_student
    for score in scores[1:]:
        if score > mean_score:
            over_mean_student += 1
    over_mean_rate = round(over_mean_student/total_student*100,3)
    print(f'{over_mean_rate:.3f}%')


