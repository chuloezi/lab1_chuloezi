# Project Overview
This project provides a system for evaluating student grades and organizing academic records. It is composed of a Python application for data analysis and a Bash shell script for file management.
## Grade Evaluator (grade-evaluator.py)
The Python application is used to look through a student's grades from a CSV file, and it performs the following tasks:
### Data Validation: 
It firsts Checks that all assignment scores are between 0 and 100.
### Weight Verification: 
Secondly, it verifies that Formative assignments total are equivalent to 60% and Summative assignments total are equivalent to 40% of the grade.
### GPA Calculation: 
Thirdly, it calculates the final GPA using the formula 
GPA = (Total Grade / 100) x 5.0
### Pass/Fail Logic: 
Then it determines if a student passed by checking if they scored at least 50% in both Formative assignments and Summative assignments.
### Resubmission Help: 
If a student fails, it identifies which formative assignments with the highest weight are eligible for resubmission.
### How to run it
Open your terminal and run: "grade-evaluator.py"
## Shell Script Organizer (organizer.sh)
The Bash script is used to manage your workspace so you can process new students without losing old data. It does the following tasks:
### Archiving: 
It renames the current grades.csv by adding a unique timestamp to prevent overwriting.
### Organization: 
It moves the renamed file into an archive folder.
### Workspace Reset: 
Then it creates a brand new, empty grades.csv file so the environment is ready for the next set of grades.
### Logging: 
It records every action taken (time, date, and filenames) into a file called organizer.log.
### How to run it
Write this "bash organizer.sh" to run it
