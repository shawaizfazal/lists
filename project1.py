
empty_list = []
print("empty list:", empty_list)
marks = [56, 23, 15, 22, 33]
print("studnt marks:", marks)
sample_marks = [10, 20, 30] * 2
print("repeated sample marks:", sample_marks)
print("number of marks:", len(marks))
print("first mark:", marks[0])
print("last mark:", marks[-1])
first_three_marks = marks[0:3]
print("first three marks:", first_three_marks)
reversed_marks = marks[::-1]
print("reversed Marks:", reversed)
def match_marks(mark_list):
    count = 0
    matched_marks = []
    for mark in mark_list:
        mark_text = str(mark)
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
    print("marks with first and last digit same:", matched_marks)
    return count
same_digit_count = match_marks([40, 50, 60, 70, 80])
print("number of matching marks:", same_digit_count)
total = 0
for mark in marks:
    total += mark

average = total / len(marks)
print("sum of marks:", total)
print("average marks:", average)

marks.sort()
print("smallest mark is:", marks[0])
print("largest mark is:", marks[-1])

# PART 10: Print the final student marks summary
print("")
print("===== student mark anylizer =====")
print("sorted marks:", marks)
print("total marks:", total)
print("average marks:", average)
print("lowest mark:", marks[0])
print("highest mark:", marks[-1])
print("=======================================")