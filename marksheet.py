# Marksheet Generator

def generate_marksheet():
    print("========== Marksheet Generator ==========")
    
    # Input student details
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    class_name = input("Enter Class: ")
    
    # Input marks for subjects
    print("\nEnter marks for the subjects (out of 100):")
    subjects = ['Mathematics', 'Science', 'English', 'Social Studies', 'Computer']
    marks = {}
    total_marks = 0

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    total_marks += mark
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
    
    # Calculate percentage
    percentage = (total_marks / (len(subjects) * 100)) * 100
    
    # Determine grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    
    # Display marksheet
    print("\n========== Marksheet ==========")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_no}")
    print(f"Class: {class_name}\n")
    print("Subjects and Marks:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    print("\n========== Results ==========")
    print(f"Total Marks: {total_marks}/{len(subjects) * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("================================")

# Run the marksheet generator
generate_marksheet()
