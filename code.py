import json
import os
from datetime import datetime
DATA_FILE = "grades_data.json"
def load_data():
    """Load data from JSON file. Creates file if not exists."""
    if not os.path.exists(DATA_FILE):
        return {
            "students": {},      # roll_no -> name
            "subjects": {},      # sub_code -> subject_name
            "grades": {},        # "roll_sub" -> marks
            "metadata": {"created": str(datetime.now()), "app": "SGMS v1.0"}
        }
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        print("Corrupted data file. Starting fresh.")
        return {"students": {}, "subjects": {}, "grades": {}, "metadata": {}}

def save_data(data):
    """Save data with error handling and backup."""
    try:
        # Create backup
        if os.path.exists(DATA_FILE):
            os.replace(DATA_FILE, DATA_FILE + ".backup")
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Failed to save data: {e}")

class StudentManager:
    @staticmethod
    def add_student(data):
        roll = input("Enter Roll Number: ").strip().upper()
        if roll in data["students"]:
            print("Student already exists!")
            return
        name = input("Enter Student Name: ").strip().title()
        data["students"][roll] = name
        print(f"Student {name} ({roll}) added successfully!")

    @staticmethod
    def view_students(data):
        if not data["students"]:
            print("No students found.")
            return
        print("\n--- All Students ---")
        print(f"{'Roll No':<10} {'Name':<20}")
        print("-" * 30)
        for roll, name in data["students"].items():
            print(f"{roll:<10} {name:<20}")

    @staticmethod
    def delete_student(data):
        roll = input("Enter Roll Number to delete: ").strip().upper()
        if roll not in data["students"]:
            print("Student not found!")
            return
        del data["students"][roll]
        # Clean up grades
        data["grades"] = {k: v for k, v in data["grades"].items() if not k.startswith(roll + "_")}
        print("Student and related grades deleted.")


class SubjectManager:
    @staticmethod
    def add_subject(data):
        code = input("Enter Subject Code (e.g., CSE1001): ").strip().upper()
        if code in data["subjects"]:
            print("Subject already exists!")
            return
        name = input("Enter Subject Name: ").strip().title()
        data["subjects"][code] = name
        print(f"Subject {name} ({code}) added!")

    @staticmethod
    def view_subjects(data):
        if not data["subjects"]:
            print("No subjects found.")
            return
        print("\n--- All Subjects ---")
        print(f"{'Code':<12} {'Subject Name':<25}")
        print("-" * 40)
        for code, name in data["subjects"].items():
            print(f"{code:<12} {name:<25}")


class GradeManager:
    @staticmethod
    def record_grade(data):
        if not data["students"]:
            print("Add students first!")
            return
        if not data["subjects"]:
            print("Add subjects first!")
            return

        StudentManager.view_students(data)
        roll = input("\nEnter Student Roll No: ").strip().upper()
        if roll not in data["students"]:
            print("Invalid Roll Number!")
            return

        SubjectManager.view_subjects(data)
        sub = input("Enter Subject Code: ").strip().upper()
        if sub not in data["subjects"]:
            print("Invalid Subject Code!")
            return

        try:
            marks = float(input("Enter Marks (0-100): "))
            if not 0 <= marks <= 100:
                raise ValueError
            key = f"{roll}_{sub}"
            data["grades"][key] = marks
            print(f"Grade recorded: {data['students'][roll]} -> {data['subjects'][sub]} = {marks}")
        except:
            print("Invalid marks! Must be 0-100.")

    @staticmethod
    def generate_report(data):
        if not data["grades"]:
            print("No grades recorded yet.")
            return

        print("\n" + "="*70)
        print(" " * 20 + "STUDENT GRADE REPORT")
        print("="*70)
        print(f"{'Roll':<8} {'Name':<18} {'Subject':<12} {'Marks':<6} {'Status':<8}")
        print("-" * 70)

        total = 0
        passed = 0
        for key, marks in data["grades"].items():
            roll, sub = key.split("_", 1)
            name = data["students"].get(roll, "Unknown")
            subj = data["subjects"].get(sub, "Unknown")
            status = "PASS" if marks >= 40 else "FAIL"
            if marks >= 40:
                passed += 1
            total += 1
            print(f"{roll:<8} {name:<18} {sub:<12} {marks:<6} {status:<8}")

        print("-" * 70)
        print(f"Total Students with Grades: {total} | Pass Rate: {passed/total*100:.1f}%")
        print(f"Report Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*70)


def main():
    data = load_data()
    print("Welcome to Student Grade Management System (SGMS)")

    while True:
        print("\n" + "="*50)
        print(" MAIN MENU")
        print("="*50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Add Subject")
        print("5. View All Subjects")
        print("6. Record Grade")
        print("7. Generate Full Report")
        print("8. Save & Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            StudentManager.add_student(data)
        elif choice == "2":
            StudentManager.view_students(data)
        elif choice == "3":
            StudentManager.delete_student(data)
        elif choice == "4":
            SubjectManager.add_subject(data)
        elif choice == "5":
            SubjectManager.view_subjects(data)
        elif choice == "6":
            GradeManager.record_grade(data)
        elif choice == "7":
            GradeManager.generate_report(data)
        elif choice == "8":
            save_data(data)
            print("Thank you for using SGMS. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
