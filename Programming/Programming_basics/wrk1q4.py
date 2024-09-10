students = int(input("enter the number of students in the class: "))
books  = int(input("enter the number of books to divide among the class: "))
print("there will be", books // students, "books per student with", books % students, "remainder.")