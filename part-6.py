for i in range(5):
    print(i)
    
scores=[70, 85, 60, 90, 45]

for score in scores:
    print("Score:",score)
    
count = 1
while count <= 5:
    print(count)
    count += 1
    
scores = [45, 70, 85, 30, 90, 55]

total = 0
pass_count = 0
fail_count = 0

for score in scores:
    total += score
    if score >= 40:
        pass_count += 1
    else:
        fail_count +=1
    
average = total / len(scores)




print("Total:", total)
print("Average:", average) 
print ("pass_count:",pass_count)
print ("fail_count:",fail_count)   

     