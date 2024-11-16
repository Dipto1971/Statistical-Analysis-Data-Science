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
  
# Creating a Student Data Set dictionary  
student_data_set = {
    "name": ["student1", "student2", "student3"],
    "id" : ["2022-1", "2022-2", "2022-3"],
    "CGPA" : [3.55, 4.0, 3.9]
}

print(student_data_set["name"])

for key,value in student_data_set.items():
  print(key, ":")
  for val in value:
    print(val)

# Creating a Employee Data Set dictionary & performing operations
employee_data_set = {
    "Name" : ["Emp1", "Emp2", "Emp3"],
    "Salary": [20000, 40000, 60000],
    "Dept": ["HR", "IT", "HR"]
}
print(employee_data_set)
# add a new column named City
employee_data_set["City"] = ["Dhaka", "Khulna", "Barishal"]

print(employee_data_set)

# Delete "IT" from Dept
for i in range(0, 2, 1):
  if employee_data_set["Dept"][i] == "IT":
     del employee_data_set["Dept"][i]

print(employee_data_set)
# Update Emp1 Salary to 100000
for i in range(0, len(employee_data_set["Name"]), 1):
  if employee_data_set["Name"][i] == "Emp1":
    employee_data_set["Salary"][i] = 100000

print(employee_data_set)    