import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        # File handling technique to read and parse structured data
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Processes grades, validates data, and determines academic standing.
    """
    print("\n--- Processing Grades ---")

    # Variables to track totals
    formative_weight_total = 0
    summative_weight_total = 0
    formative_weighted_score = 0
    summative_weighted_score = 0
    failed_formative_assignments = []
    
    # TODO: a) Check if all scores are percentage based (0-100) 
    for item in data:
        if not (0 <= item["score"] <= 100):
            # Fixed syntax: using single quotes inside double quotes
            print(f"Error: Score for '{item['assignment']}' is out of range (0-100).")
        
        # Accumulate weights and calculate category scores 
        if item["group"] == "Formative":
            formative_weight_total += item["weight"]
            formative_weighted_score += (item["score"] * (item["weight"] / 100))
            if item["score"] < 50:
                failed_formative_assignments.append(item)
        elif item["group"] == "Summative":
            summative_weight_total += item["weight"]
            summative_weighted_score += (item["score"] * (item["weight"] / 100))

    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60) 
    if formative_weight_total != 60 or summative_weight_total != 40:
        print(f"Error: Total weights are incorrect. Formative: {formative_weight_total}%, Summative: {summative_weight_total}%")
        return # Stop if weights are invalid 

    # TODO: c) Calculate the Final Grade and GPA 
    final_grade = formative_weighted_score + summative_weighted_score
    gpa = (final_grade / 100) * 5.0 

    print(f"Final Grade: {final_grade:.2f}%")
    print(f"GPA: {gpa:.2f} out of 5.0")

    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    is_passed = (formative_weighted_score >= 30) and (summative_weighted_score >= 20)

    # TODO: e) Check for failed formative assignments (< 50%) 
    # and determine which one(s) have the highest weight for resubmission 
    resubmission_list = []
    if not is_passed and failed_formative_assignments:
        highest_weight = 0
        for item in failed_formative_assignments:
            if item["weight"] > highest_weight:
                highest_weight = item["weight"]

        for item in failed_formative_assignments:
            if item["weight"] == highest_weight:
                resubmission_list.append(item["assignment"])

    # TODO: f) Print the final decision (PASSED/FAILED) and resubmission options 
    if is_passed:
        print("Status: PASSED")
    else:
        print("Status: FAILED")
        if resubmission_list:
            print("Resubmission Options (Failed Formative Assignments with Highest Weight):")
            for assignment in resubmission_list:
                print(f"- {assignment}")
        else:
            print("No formative assignments failed, but overall category scores did not meet the 50% threshold.")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
