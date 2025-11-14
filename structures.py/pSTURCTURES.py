#list
employees = ["Alice", "Bob", "Charlie", "David"]
#tuple
coordinates = (10.0, 20.0)
#dictionary 
student = {"name": "John", "age": 21, "courses": ["Math", "CompSci"]}
#set        
unique_numbers = {1, 2, 3, 4, 5}
# --- IGNORE ---
for i in range(5):
    #dictionary
    person = {"id": i, "name": f"Person_{i}"}   
    name: str = person["name"]
    print(name) 
    
#Dictionary to store student data
students = {}


def add_student():
    """
    Add a new student with their name and three subject marks.
    Validates that marks are between 0-100.
    """
    while True:
        try:
            student_name = input("\nEnter student name: ").strip()
            
            # Check if student already exists
            if student_name in students:
                print(f"Error: {student_name} already exists. Please enter a different name.\n")
                continue
            
            if not student_name:
                print("Error: Student name cannot be empty. Please try again.\n")
                continue
            
            # Get three subject marks
            marks = []
            subjects = ["Maths", "English", "Science"]
            
            for subject in subjects:
                while True:
                    try:
                        mark = float(input(f"Enter {subject} marks (0-100): "))
                        
                        # Validate mark range
                        if mark < 0 or mark > 100:
                            print("Error: Marks must be between 0 and 100. Please try again.")
                            continue
                        
                        marks.append(mark)
                        break
                    
                    except ValueError:
                        print("Error: Please enter a valid number.\n")
            
            # Store student data
            students[student_name] = {
                "marks": marks,
                "average": calculate_average(marks),
                "grade": find_grade(calculate_average(marks))
            }
            
            print(f"\n✓ {student_name} added successfully!")
            break
        
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            break


def calculate_average(marks):
    """
    Calculate the average of three subject marks.
    
    Args:
        marks (list): List of three subject marks
    
    Returns:
        float: Average of the marks (rounded to 2 decimal places)
    """
    if len(marks) == 0:
        return 0
    return round(sum(marks) / len(marks), 2)


def find_grade(average):
    """
    Determine the grade based on average marks.
    
    Grade criteria:
    70 and above → A
    60–69 → B
    50–59 → C
    40–49 → D
    Below 40 → F
    
    Args:
        average (float): Average marks of the student
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def display_results():
    """
    Display all students' names, averages, and grades in a formatted table.
    """
    if not students:
        print("\n" + "="*60)
        print("No students recorded yet.")
        print("="*60)
        return
    
    print("\n" + "="*60)
    print("STUDENT GRADE REPORT")
    print("="*60)
    print(f"{'Student Name':<20} {'Average':<12} {'Grade':<8}")
    print("-"*60)
    
    for name, data in students.items():
        print(f"{name:<20} {data['average']:<12.2f} {data['grade']:<8}")
    
    print("="*60)


def show_menu():
    """
    Display the main menu and get user choice.
    
    Returns:
        str: User's menu choice
    """
    print("\n" + "="*60)
    print("STUDENT GRADE PROGRAM")
    print("="*60)
    print("1. Add a new student")
    print("2. View all students and grades")
    print("3. Exit")
    print("="*60)
    
    choice = input("Enter your choice (1/2/3): ").strip()
    return choice


def main():
    """
    Main function to run the student grade program.
    Controls the program flow with a menu loop.
    """
    print("\nWelcome to the Student Grade Program!")
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_student()
        
        elif choice == "2":
            display_results()
        
        elif choice == "3":
            print("\nThank you for using the Student Grade Program!")
            print("Goodbye!\n")
            break
        
        else:
            print("Error: Invalid choice. Please enter 1, 2, or 3.\n")


# Run the program
if __name__ == "__main__":
    main()
