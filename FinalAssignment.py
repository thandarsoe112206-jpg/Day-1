   
students = [
    {
        "name": "Aung Aung",
        "age": 20,
        "study_hours": 4,
        "score": 85
    },
    {
    "name": "Su Su",
    "age": 21,
    "study_hours": 3,
    "score":92
},
{
    "name": "Mg Mg",
    "age": 22,
    "study_hours": 2,
    "score" :35
},
{
    "name": "Hla Hla",
    "age": 23,
    "study_hours": 4,
    "score":70
},
{
    "name": "Khin Khin",
    "age": 24,
    "study_hours": 3,
    "score":55
}
]
grade_categories = ("A", "B", "C", "D", "F")

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    elif score >= 30:
        return "D"
    else:
        return "F"

def calculate_average(students):
    total = 0

    for student in students:
        total += student["score"]

    return total / len(students)

def count_passing_students(students):
    count = 0

    for student in students:
        if student["score"] >= 40:
            count += 1

    return count

passing = count_passing_students(students)
print("Passing Students:", passing)

average = calculate_average(students)
print("average score:", average)

for student in students:
    score = student["score"]

    if score < 0 or score > 100:
        print(student["name"], "Invalid score!")
        continue

    grade = get_grade(score)
    
    print(student["name"], "Score:", score, "Grade:", grade)

print("\n===== STUDENT PERFORMANCE REPORT =====")
print("Total Students:", len(students))
print("Average Score:", round(average, 2))
print("Passing Students:", passing)
print("Failing Students:", len(students) - passing)

