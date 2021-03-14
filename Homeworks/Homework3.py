std_list = []
for i in range(5):
    name = input("student name: ")
    midterm_grade = input("student midterm grade: ")
    project_grade = input("student project grade: ")
    final_grade = input("student final grade: ")
    passing_grade = float(midterm_grade) * 0.3 + float(project_grade) * 0.3 + float(final_grade) * 0.4
    std = {"Name" : name, "Midterm grade" : midterm_grade, "Project grade" : project_grade, "Final grade" : final_grade, "Passing grade" : passing_grade}
    std_list.append(std)    

std_list.sort(key = lambda x: x.get('Passing grade'), reverse = True)

print("All students")
for i in std_list:
    print(i)

print("Best student")
print(std_list[0])
