import numpy as np

# Student names
students = np.array([
    "Rahul",
    "Priya",
    "Amit",
    "Sneha",
    "Karan"
])

# Subject names
subjects = np.array([
    "Python",
    "SQL",
    "Mathematics",
    "Statistics"
])

# Student marks
marks = np.array([
    [85, 78, 90, 88],
    [92, 89, 95, 91],
    [45, 55, 60, 50],
    [76, 82, 79, 85],
    [30, 40, 35, 45]
])

print("STUDENT MARKS ANALYSIS")
print("----------------------")

print("Students:", students)
print("Subjects:", subjects)

print("\nMarks:")
print(marks)

print("\nDataset Shape:", marks.shape)

# Total marks of each student
total_marks = np.sum(marks, axis=1)

# Average marks of each student
average_marks = np.mean(marks, axis=1)

print("\nSTUDENT PERFORMANCE")

for i in range(len(students)):
    print(
        students[i],
        "Total:", total_marks[i],
        "Average:", average_marks[i]
    )


# Average marks in each subject
subject_average = np.mean(marks, axis=0)

print("\nSUBJECT-WISE AVERAGE")

for i in range(len(subjects)):
    print(subjects[i], ":", subject_average[i])

# Highest marks in each subject
subject_highest = np.max(marks, axis=0)

print("\nHIGHEST MARKS")

for i in range(len(subjects)):
    print(subjects[i], ":", subject_highest[i])


# Lowest marks in each subject
subject_lowest = np.min(marks, axis=0)

print("\nLOWEST MARKS")

for i in range(len(subjects)):
    print(subjects[i], ":", subject_lowest[i])


# Strongest subject
strongest_index = np.argmax(subject_average)

# Weakest subject
weakest_index = np.argmin(subject_average)

print("\nSUBJECT PERFORMANCE")

print("Strongest Subject:", subjects[strongest_index])
print("Weakest Subject:", subjects[weakest_index])




# Find topper
topper_index = np.argmax(total_marks)

# Find lowest performer
lowest_index = np.argmin(total_marks)

print("\nSTUDENT RANK ANALYSIS")
print("---------------------")

print("\nTOPPER")
print("Name:", students[topper_index])
print("Total:", total_marks[topper_index])
print("Average:", average_marks[topper_index])

print("\nLOWEST PERFORMER")
print("Name:", students[lowest_index])
print("Total:", total_marks[lowest_index])
print("Average:", average_marks[lowest_index])



# Check whether each student has any failed subject
failed_students = np.any(marks < 40, axis=1)

print(failed_students)

# Get names of failed students
print("Failed Students:", students[failed_students])
passed_students = ~failed_students

print("Passed Students:", students[passed_students])
print("\nPASS/FAIL REPORT")
print("----------------")

for i in range(len(students)):

    if failed_students[i]:
        status = "FAIL"
    else:
        status = "PASS"

    print(students[i], ":", status)


topper_index = np.argmax(total_marks)

print("\ntopper\n")
print(students[topper_index])

ranking_indices = np.argsort(total_marks)[::-1]

print("\nSTUDENT RANKING")

for rank, index in enumerate(ranking_indices, start=1):
    print(
        rank,
        students[index],
        "Total:", total_marks[index],
        "Average:", average_marks[index]
    )



print("\n========== STUDENT PERFORMANCE REPORT ==========")

# Overall class statistics
class_average = np.mean(average_marks)
highest_total = np.max(total_marks)
lowest_total = np.min(total_marks)
total_passed=np.sum(passed_students)
total_failed=np.sum(failed_students)
print("\nCLASS SUMMARY")
print("Total Students:", len(students))
print("Class Average:", round(class_average, 2))
print("Passed Students:", total_passed)
print("Failed Students:", total_failed)

# Topper details
print("\nTOPPER")
print("Name:", students[topper_index])
print("Total Marks:", total_marks[topper_index])
print("Average Marks:", average_marks[topper_index])

# Subject performance
print("\nSUBJECT PERFORMANCE")

for i in range(len(subjects)):
    print(
        subjects[i],
        "| Average:", subject_average[i],
        "| Highest:", subject_highest[i],
        "| Lowest:", subject_lowest[i]
    )

# Final student ranking
print("\nSTUDENT RANKING")

for rank, index in enumerate(ranking_indices, start=1):
    status = "FAIL" if failed_students[index] else "PASS"

    print(
        rank,
        students[index],
        "| Total:", total_marks[index],
        "| Average:", average_marks[index],
        "| Status:", status
    )

print("\n================================================")