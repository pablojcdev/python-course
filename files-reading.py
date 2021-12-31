employee_file = open("files-employees.txt", "r")
# r = read
# w = write
# a = append (can't change, can add information)
# r+ = read and write

#print(employee_file.readable())
#print(employee_file.read())

#print(employee_file.readline())

#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readline())

#print(employee_file.readlines())

#print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

