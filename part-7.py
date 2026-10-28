from itertools import count


def greet():
    print('Hello from UCSpyay')
    
greet()

def greet_student(name):
    print(f"Hello, {name}!")
    
    
greet_student("Aung Aung")
greet_student("Su Su")

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


scores = [45, 70, 85]
result = calculate_average(scores)
print("Average:", result)


def calculate_total(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)

print("Total:", calculate_total(scores))
 
def calculate_average(scores):
    if len(scores) == 0:
        return 0
        return sum(scores) / len(scores)
    print("average:", calculate_average(scores))

def classify_grade(score):
    if score < 0 or score > 90:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    
    else:
        return "D"
    
print(classify_grade(88))
print(classify_grade(60))
print(classify_grade(45)) 
print(classify_grade(20))

def count_passed(scores):
      count = 0
      for score in scores:
       if score >= 40:
        count += 1
       return count
       scores = [45, 70, 85, 30, 90, 55]
       
      print("count_passed:", count_passed(scores))

