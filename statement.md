


```markdown
# Project Statement - Student Grade Management System (SGMS)

## Problem Statement
In educational institutions, teachers often use manual methods or Excel sheets to track student grades, which leads to errors, data loss, and difficulty in generating quick reports. There is a clear need for a lightweight, reliable, and easy-to-use system that can manage student records, subjects, grades, and generate performance reports efficiently.

## Scope of the Project
This is a console-based desktop application built in Python that provides complete grade management functionality for a single class/semester. It uses file-based storage (JSON) for data persistence and includes full error handling and backup features.

## Target Users
- Classroom Teachers
- Lab Instructors
- Academic Coordinators
- Tutors handling student performance records

## High-level Features
- Add/View/Delete Students (CRUD)
- Add/View Subjects
- Record and update grades with input validation
- Generate detailed performance report showing:
  - Student name, roll number, subject, marks
  - Pass/Fail status (≥40 = PASS)
  - Overall pass percentage
- Automatic saving to JSON file
- Backup creation on every save

## Three Major Functional Modules
1. **Student Management Module** → Handles student enrollment and removal
2. **Subject Management Module** → Manages course/subject details
3. **Grade Management & Reporting Module** → Records marks and generates analytics

## Non-Functional Requirements Satisfied
- **Usability**: Simple numbered menu interface
- **Reliability**: Data persistence + auto backup
- **Error Handling**: Full input validation and exception handling
- **Maintainability**: Clean, well-commented, modular code structure

**A complete, practical solution using only core Python concepts — perfect for academic use.**
