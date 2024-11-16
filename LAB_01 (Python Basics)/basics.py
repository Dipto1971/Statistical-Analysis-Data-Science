# Creating a variable and printing it
num_1 = 20
num_2 = 30
if num_1 > num_2:
  print("num_1 is greater than num_2")
elif num_1 < num_2:
  print("num_1 is less than num_2")
else:
  print("num_1 is equal to num_2")

# Creating a list of students with their grades
student_list = [
    {
        "name": "Mahir",
        "Grade": 2.5
    },
    {
        "name": "Faisal",
        "Grade": 3.9
    },
    {
        "name": "Israt",
        "Grade": 4
    }
]

for i in range(0, len(student_list), 1):
  print(student_list[i])

student_list.append({
    "name": "Supti",
    "Grade": 4.00
})

print (student_list)

for std in student_list:
  print(std)

student_dict = {
    "student1": 2.5,
    "student2": 4.0,
    "student3": 3.75
}

for key,value in student_dict.items():
  print(key, value)
  
  