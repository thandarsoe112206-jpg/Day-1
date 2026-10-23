student = {
    "name": "Su Su",
    "age": 20,
    "score": 88,
    "passed": True
}
print(student["name"])
print(student["score"])

student = [
    {"name": "Aung Aung", "score": 85},
    {"name": "Su Su", "score": 92},
    {"name": "Mg Mg", "score": 35}
]

for student in student:
    print(student["name"], student["score"])