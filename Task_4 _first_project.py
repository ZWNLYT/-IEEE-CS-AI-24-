
import random

class Student:
    def __init__(self, name, age, grade):
        self.id = random.randint(1000, 9999)  
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        new_student = Student(name, age, grade)
        self.students.append(new_student)
        return f"Student {name} added successfully with ID {new_student.id}"

    def view_students(self):
        if not self.students:
            return "No students in the database"
        return "\n".join([str(student) for student in self.students])

    def search_student(self, name_or_id):
        for student in self.students:
            if student.name == name_or_id or str(student.id) == name_or_id:
                return str(student)
        return "Student not found"

    def update_student(self, student_id, name=None, age=None, grade=None):
        for student in self.students:
            if student.id == int(student_id):
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
                return f"Student {student_id} updated successfully"
        return "Student not found"

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == int(student_id):
                self.students.remove(student)
                return f"Student {student_id} deleted successfully"
        return "Student not found"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for student in self.students:
                f.write(f"{student.id},{student.name},{student.age},{student.grade}\n")
        return f"Student database saved to {filename} successfully"

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    student_id, name, age, grade = line.strip().split(",")
                    self.students.append(Student(name, int(age), grade))
            return f"Student database loaded from {filename} successfully"
        except FileNotFoundError:
            return f"File {filename} not found"

def main():
    db = StudentDatabase()

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            print(db.add_student(name, age, grade))

        elif choice == "2":
            print(db.view_students())

        elif choice == "3":
            name_or_id = input("Enter student name or ID: ")
            print(db.search_student(name_or_id))

        elif choice == "4":
            student_id = input("Enter student ID: ")
            name = input("Enter new student name (optional): ")
            age = int(input("Enter new student age (optional): "))
            grade = input("Enter new student grade (optional): ")
            print(db.update_student(student_id, name, age, grade))

        elif choice == "5":
            student_id = input("Enter student ID: ")
            print(db.delete_student(student_id))

        elif choice == "6":
            filename = input("Enter filename: ")
            print(db.save_to_file(filename))

        elif choice == "7":
            filename = input("Enter filename: ")
            print(db.load_from_file(filename))

        elif choice == "8":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
