# Educational Management System
A console-based application for managing users, units, enrollments, and scores
in an educational setting. Users can log in as admin, teacher, or student, with
role-based features.
## Table of Contents
* Quick Start
* User Roles
* System Overview
## Quick Start
To run the Educational Management System, simply execute the main.py file:
python main.py
## User Roles
### Admin
* Search users
* Manage users and units
### Teacher
* Manage teaching units
* Access student enrollment and score data
### Student
* View, enroll, and drop units
* Check and generate scores
## System Overview
Code is organized into user type classes (Admin, Teacher, Student) and a Unit
class. main.py contains the main menu and role-based functions. Test data is
generated with `generate_test_data()`.\
Data is stored in text files:
* data/user.txt (User information)
* data/unit.txt (Unit information)