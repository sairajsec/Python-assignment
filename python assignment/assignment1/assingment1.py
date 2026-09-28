# Assignment 1: Create a Dictionary, Tuple and List of students
# Perform Add, Delete and Update operations

# Creating a list
students_list = ["Ananya", "Arjun", "Kavya", "Ishaan", "Meera"]
print("Students list: ", students_list)

students_list.append("Vihaan")
print(students_list)

students_list.remove("Ananya")
print(students_list)

students_list = ["Ananya", "Arjun", "Kavya", "Ishaan", "Meera"]
students_list.pop(1)
print(students_list)

del students_list[3]
print(students_list)

students_list[2] = "Saanvi"
print(students_list)


# Creating a tuple
students_tuple = ("Ananya", "Arjun", "Kavya", "Ishaan", "Meera")
print("Students tuple: ", students_tuple)

y = list(students_tuple)
y.append("Vihaan")
y.append("Advik")
y.append("Myra")

students_tuple = tuple(y)
print(students_tuple)

y = ("Reyansh",)
students_tuple += y
print(students_tuple)

y = list(students_tuple)
y.remove("Ananya")
y.remove("Meera")

students_tuple = tuple(y)
print(students_tuple)


# Creating a dictionary
students_dict = {
    1: "Ananya",
    2: "Arjun",
    3: "Kavya",
    4: "Ishaan",
    5: "Meera"
}

print("Students dictionary: ", students_dict)

students_dict[6] = "Vihaan"
print("After adding Vihaan: ", students_dict)

del students_dict[3]
print("After deleting Kavya: ", students_dict)

students_dict[2] = "Saanvi"
print("After updating name: ", students_dict)