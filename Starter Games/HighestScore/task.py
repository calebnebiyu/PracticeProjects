student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# Find the sum.
# Option 1:
total_exam_score = sum(student_scores)
print(total_exam_score)

# Option 2:
sum  = 0
for score in student_scores:
    sum += score
print(sum)

# Find the highest number.
# Option 1:
print(max(student_scores)) # --> picks the largest number in a list

# Option 2:
max = 0
for score in student_scores:
    if score > max: # --> if the current score is greater than the max (0 at first)... the the score becomes the new max
        score = max # --> then the score becomes the new max