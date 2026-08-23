import numpy as np

print("PERCENTAGE CALCULATOR USING NUMPY")
show_arr = np.array(["English", "Hindi", "Maths", "Science", "Computer Science"])
print(f"Subjects: {show_arr}")
sub1 = int(input("English: "))
sub2 = int(input("Hindi: "))
sub3 = int(input("Maths: "))
sub4 = int(input("Science: "))
sub5 = int(input("Computer Science: "))

marks_arr = np.array([sub1,sub2,sub3,sub4,sub5])
print(f"Marks: {marks_arr}")

form = np.mean(marks_arr)
print("Total Marks: ", np.sum(marks_arr))
print(f"percentage: {form}%")
