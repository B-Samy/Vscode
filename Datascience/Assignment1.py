# Assignment no 1 




# employee = {
#     101:{'Name': 'Satya' , 'Age':27 , 'department':'Hr' , 'salary' : 50000},
# }

# print(employee)



# Q.2 Menu system 

# employee = []

# def add_Employee(empId , name ,department):
#     if empId in employee:
#         print("Account existed")
#     else:
#         employee.append((empId,name,department))

#         print(end="\n")


# print(end="\n")


# def display_Employee(empId):

#     if empId in employee:
#         print(f"The empId of {name} is {empId}")
#         print(f"The name of employee is {name}")
#         print(f"The department of employee {name} is {department}")

#     else:
#         print("Employee does'nt seem to be exist")



# print(end="\n")



# def Searching(empId , name):
#     if empId or name in employee:
#         print(f"The Id of employee you looking for is {empId}")
#         print(f"The name of employee you looking for is {name}")
#     else:
#         print(f"can't find the employee {name} you looking for ")


# print(end="\n")

# while True:

#     print("Menu System")
#     print("1 -> Add Employee")
#     print("2 -> Display Employee")
#     print("3 -> Search Employee")
#     print("4 -> Exit")

#     print(end="\n")

#     choice= int(input('Enter your choice : '))
#     if choice == 1:
#         empId = int(input("Enter the empId : "))
#         name = input("Enter the employee Name : ")
#         department = input("Enter the employee department : ")
#         print("Employee added successfully")
#         add_Employee(empId,name,department)

#     elif choice == 2:
#         empId = int(input("Enter the empId to display : "))
#         display_Employee(empId)

#     elif choice == 3:
#         empId = int(input("Enter the empId to finding employee : "))
#         Searching(empId)
#     elif choice == 4:
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice")
#         break


# Q.3 Employee Adding  functionality 


# empl = {}

# def add_emp(empid , name ,age , department, salary):
#     if empid in empl:
#         print("Enter new Id / Already existed ")
#     else:
#         empl[empid] = {'Name':name , 'Age':age,'Department':department,'Salary':salary}
#         print("Employee added sucessfully")



# empid = int(input("Enter the EmployeeId : "))
# name = input("Enter the Name : ")
# age = int(input("Enter the Age : "))
# department = input("Enter the department : ")
# salary = int(input("Enter the salary : "))


# add_emp(empid,name , age , department , salary)

# print(end="\n")

# def displayNow(empid):
#     if empid in empl:
#         print(f"The Id of the employee is {empid}")
#         print(f"The name of the employee is {name}")
#         print(f"The age of the employee is {age}")
#         print(f"The department of the employee is {department}")
#         print(f"The salary of the employee is {salary}")

    
# displayNow(empid)



# Q.4     VIEW ALL EMPLOYEES 


# def view_employee(empid):
#     if empid in empl:
#         print(f"The empid is {empid}")
#         print(f"The name is {name}")
#         print(f"The age is {age}")
#         print(f"The department is {department}")
#         print(f"The salary is {salary}")
#     else:
#         print("No employees available ")


# Q.5 SEARCH THE EMPLOYEE 


# def search_user(empid):
#     if empid in empl:
#         print(f"The name of the employee is {name}")
#         print(f"The age of the employee is {age}")
#         print(f"The department of the employee is {department}")
#         print(f"The salary of the employee is {salary}")
#     else:
#         print("Emplyoee not found ")


# empid = int(input("Search the employee by id "))
# search_user(empid)


# Q.6 EXIT PROGRAM 



# while True:
#     user_choice = input("Enter the choice ")

#     if user_choice.lower() == 'exit':
#         break
#     print("Thank you")