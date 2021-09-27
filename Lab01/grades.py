import json

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class FileReader:
    def __init__(self):
        try:
            with open("grades.txt", "r") as file:
                readString = ""
                for lines in file:
                    readString += lines.strip()
            self.grades_dict = json.loads(readString)
            print("Finished loading dictionary from memory...")
        except:
            print("ERROR: Unable to read file")
            raise

    def createStudent(self, name, grade):
        self.grades_dict.update({name : grade})
        print("Created Student " + name + " with grade " + grade)

    def findStudent(self, name):
        try:
            return self.grades_dict[name]
        except KeyError:
            return -1

    def updateStudent(self, name, grade):
        if name in self.grades_dict.keys():
            self.grades_dict[name] = grade
            print("Updated Student " + name + " with grade " + grade)
        else:
            print("ERROR: Student not found!")

    def deleteStudent(self, name):
        if name in self.grades_dict.keys():
            del(self.grades_dict[name])
            print("Deleted Student " + name)
        else:
            print("ERROR: Student not found!")



if __name__ == "__main__":
    f = FileReader()
    while True:
        try:
            command = eval(input("Enter 1 to create a new student\nEnter 2 to find a student\nEnter 3 to update an existing student's grade\nEnter 4 to delete a student from record\nEnter 5 to print\nEnter 6 to exit\nENTER NUMBER: "))
        except:
            print("Invalid number entered please try again...\n")
            continue
        if command == 1:
            print("\n")
            name = input("Enter the name of the new student: ")
            grade = input("Enter " + name + "'s grade: ")
            f.createStudent(name, grade)
        if command == 2:
            print("\n")
            name = input("Enter the name of student you are trying to find: ")
            grade = f.findStudent(name)
            print(name + "'s grade is " + str(grade))
        if command == 3:
            print("\n")
            name = input("Enter name of student you are trying to update: ")
            grade = input("Enter new grade: ")
            f.updateStudent(name, grade)
        if command == 4:
            print("\n")
            name = input("Enter name of student you are trying to delete: ")
            f.deleteStudent(name)
        if command == 5:
            print("\n")
            for keys in f.grades_dict.keys():
                print("Student: " + keys + "\t Grade: " + str(f.grades_dict[keys]))
        if command == 6:
            with open("grades.txt", "w") as writer:
                json_dump = json.dumps(f.grades_dict)
                writer.write(json_dump)
            break

        print("--------------------------------------------")
