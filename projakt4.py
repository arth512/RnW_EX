marks = [78,45,92,35,67,88,21,54,100,63,49,85,76,33,57,90,41,69,58,98]

total = len(marks)

print("Total Students:", total)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", round(sum(marks)/total, 2))

passed = len([m for m in marks if m >= 40])
failed = len([m for m in marks if m < 40])

print("Passed:", passed)
print("Failed:", failed)

print("Scored 100:", marks.count(100))
print("Pass Percentage:", round((passed/total)*100, 2), "%")

sorted_marks = sorted(marks)
print("\nSorted Marks (Asc):", sorted_marks)
print("Sorted Marks (Desc):", sorted_marks[::-1])

print("Second Lowest:", sorted_marks[1])
print("Second Highest:", sorted_marks[-2])

print("All Passed:", all(m >= 40 for m in marks))
print("Any Failed:", any(m < 40 for m in marks))

search = int(input("\nEnter mark to search: "))

if search in marks:
    print(search, "FOUND")
else:
    print(search, "NOT FOUND")

A = len([m for m in marks if m >= 90])
B = len([m for m in marks if 80 <= m <= 89])
C = len([m for m in marks if 70 <= m <= 79])
D = len([m for m in marks if 60 <= m <= 69])
E = len([m for m in marks if 40 <= m <= 59])
F = len([m for m in marks if m < 40])

print("\nGRADE DISTRIBUTION")
print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)
print("E:", E)
print("F:", F)