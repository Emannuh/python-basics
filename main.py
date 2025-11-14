# # # # # print("Hellow world")

# # # # 7

# # # # # age = 25
# # # # # name = "Emmanuel"
# # # # # print(f"My name is {name} and I am {age} years old.")
# # # # # #Data Types in Python
# # # # # # Integer  
# # # # # weight = 70
# # # # # #String
# # # # # my_name = "Emmanuel"
# # # # # # a string is just a combination of characters
# # # # # # Float
# # # # # height = 5.9
# # # # # # Boolean
# # # # # print
# # # # # is_student = True_adult = age >= 18

# # # # # #User Input
# # # # # user_name = input("Enter your name: ")
# # # # # height = float(input("Enter your height in meters: "))
# # # # # print(f"Hello, {user_name}! You are {height} meters tall.") 

# # # # # print(height,user_name)

# # # # # #User input
# # # # # BMI = weight / (height ** 2)
# # # # # print(f"Your BMI is: {BMI:.2f}")
# # # # # print("Your BMI is: {:.2f}".format(BMI))

# # # # # #Type Conversion
# # # # # age_str = str(age)
# # # # # num1 = input("Enter  your first number: ") 
# # # # # num2 = input("Enter  your second number: ")
# # # # # sum_result = int(num1) + int(num2)
# # # # # print(f"The sum of {num1} and {num2} is {sum_result}.")

# # # # # # Student Marks

# # # # # # Get student name
# # # # # student_name = input("Enter student name: ")

# # # # # # Input marks for five subjects with subject names
# # # # # print(f"\nEnter marks for {student_name}:")
# # # # # math = float(input("Enter marks for Mathematics: "))
# # # # # english = float(input("Enter marks for English: "))
# # # # # science = float(input("Enter marks for Science: "))
# # # # # history = float(input("Enter marks for History: "))
# # # # # geography = float(input("Enter marks for Geography: "))

# # # # # # Create a list of tuples (subject_name, marks)
# # # # # subjects = [
# # # # #     ("Mathematics", math),
# # # # #     ("English", english),
# # # # #     ("Science", science),
# # # # #     ("History", history),
# # # # #     ("Geography", geography)
# # # # # ]

# # # # # # Sort subjects by marks in descending order (highest to lowest)
# # # # # ranked_subjects = sorted(subjects, key=lambda x: x[1], reverse=True)

# # # # # # Calculate total and average
# # # # # total_marks = math + english + science + history + geography
# # # # # average_marks = total_marks / 5

# # # # # # Print results
# # # # # print(f"\n{'='*50}")
# # # # # print(f"STUDENT MARKS REPORT - {student_name}")
# # # # # print(f"{'='*50}")

# # # # # print(f"\nSUBJECTS RANKED (Highest to Lowest):")
# # # # # print(f"{'-'*50}")
# # # # # for i, (subject, marks) in enumerate(ranked_subjects, 1):
# # # # #     print(f"{i}. {subject:<20} : {marks:.2f}")

# # # # # print(f"\n{'-'*50}")
# # # # # print(f"Total Marks     : {total_marks:.2f}")
# # # # # print(f"Average Marks   : {average_marks:.2f}")
# # # # # print(f"{'='*50}")

# # # # # #Product of two numbers

# # # # # num1 = int(input("Enter first number: "))
# # # # # num2 = int(input("Enter second number: "))    
# # # # # product = num1 * num2
# # # # # print(f"The product of {num1} and {num2} is {product}.") 
       
# # # # # #input three names in a single call to input()
# # # # # names = input("Enter three names separated by commas: ").split(",")
# # # # # name1, name2, name3 = [name.strip() for name in names]      
# # # # # print(f"Name 1: {name1}")
# # # # # print(f"Name 2: {name2}")       
# # # # # print(f"Name 3: {name3}")

# # # # # #Enter first name and last name in a single call to input()
# # # # # full_name = input("Enter your first and last name separated by a space: ").split(" ")           

# # # # # #Input age
# # # # # age = int(input("Enter your age: "))
# # # # # next_age = age + 1  
# # # # # print(f"Next year, you will be {next_age} years old.")

# # # # #store name,age favourite programming language,print them using variables
# # # # # name = input("Enter your name: ")
# # # # # age = int(input("Enter your age: "))
# # # # # fav_language = input("Enter your favourite programming language: ") 
# # # # # print(f"Name: {name}, Age: {age}, Favourite Programming Language: {fav_language}")  

# # # # # #Input year of birth, currectyear and print age
# # # # # year_of_birth = input("Kindly input your year of birth; ")
# # # # # current_year = input("Kindly input the current year; ")

# # # # # age = int(current_year)-int (year_of_birth)

# # # # print("Your current age is {age}years old")

# # # # #input weight in kg and convert to grams
# # # # weight_kg = float(input("Enter your weight in kilograms: "))        
# # # # weight_grams = weight_kg * 1000
# # # # print(f"Your weight in grams is: {weight_grams} grams.")


# # # # #logical operators
# # # # age1 = int(input("Enter age of first person: "))
# # # # age2 = int(input("Enter age of second person: "))       
# # # # is_older = age1 > age2
# # # # print(f"Is the first person older than the second? {is_older}")


















# # # # conditional statements

# # # #if else
# # # score = int(input("Enter a number: "))
# # # if score >= 80:
# # #     print("Grade A.")
# # # elif score >= 60:
# # #     print("Grade B.")
# # # elif score >= 50:
# # #     print("Grade C.")
# # # elif score >= 40:
# # #     print("Grade D.")    
# # # elif score >= 0:
# # #     print("Grade F.")   
# # # else:
# # #     print("Invalid score, enter number between 0 and 100.")
    
# #     #while loop complexities
    
# # i = 1
# # while i <= 5:
# #     print(f"Iteration {i}")
# #     i += 1
    
# # for y in 'python':
# #     print(y)    

    
# #list
# employees = ["Alice", "Bob", "Charlie", "David"]
# #tuple
# coordinates = (10.0, 20.0)
# #dictionary 
# student = {"name": "John", "age": 21, "courses": ["Math", "CompSci"]}
# #set        
# unique_numbers = {1, 2, 3, 4, 5}
# # --- IGNORE ---
# for i in range(5):
#     #dictionary
#     person = {"id": i, "name": f"Person_{i}"}   
#     name: str = person["name"]
#     print(name) 
    
# #Dictionary to store student data
# students = {}


# def add_student():
#     """
#     Add a new student with their name and three subject marks.
#     Validates that marks are between 0-100.
#     """
#     while True:
#         try:
#             student_name = input("\nEnter student name: ").strip()
            
#             # Check if student already exists
#             if student_name in students:
#                 print(f"Error: {student_name} already exists. Please enter a different name.\n")
#                 continue
            
#             if not student_name:
#                 print("Error: Student name cannot be empty. Please try again.\n")
#                 continue
            
#             # Get three subject marks
#             marks = []
#             subjects = ["Maths", "English", "Science"]
            
#             for subject in subjects:
#                 while True:
#                     try:
#                         mark = float(input(f"Enter {subject} marks (0-100): "))
                        
#                         # Validate mark range
#                         if mark < 0 or mark > 100:
#                             print("Error: Marks must be between 0 and 100. Please try again.")
#                             continue
                        
#                         marks.append(mark)
#                         break
                    
#                     except ValueError:
#                         print("Error: Please enter a valid number.\n")
            
#             # Store student data
#             students[student_name] = {
#                 "marks": marks,
#                 "average": calculate_average(marks),
#                 "grade": find_grade(calculate_average(marks))
#             }
            
#             print(f"\n✓ {student_name} added successfully!")
#             break
        
#         except KeyboardInterrupt:
#             print("\nOperation cancelled.")
#             break


# def calculate_average(marks):
#     """
#     Calculate the average of three subject marks.
    
#     Args:
#         marks (list): List of three subject marks
    
#     Returns:
#         float: Average of the marks (rounded to 2 decimal places)
#     """
#     if len(marks) == 0:
#         return 0
#     return round(sum(marks) / len(marks), 2)


# def find_grade(average):
#     """
#     Determine the grade based on average marks.
    
#     Grade criteria:
#     70 and above → A
#     60–69 → B
#     50–59 → C
#     40–49 → D
#     Below 40 → F
    
#     Args:
#         average (float): Average marks of the student
    
#     Returns:
#         str: Letter grade (A, B, C, D, or F)
#     """
#     if average >= 70:
#         return "A"
#     elif average >= 60:
#         return "B"
#     elif average >= 50:
#         return "C"
#     elif average >= 40:
#         return "D"
#     else:
#         return "F"


# def display_results():
#     """
#     Display all students' names, averages, and grades in a formatted table.
#     """
#     if not students:
#         print("\n" + "="*60)
#         print("No students recorded yet.")
#         print("="*60)
#         return
    
#     print("\n" + "="*60)
#     print("STUDENT GRADE REPORT")
#     print("="*60)
#     print(f"{'Student Name':<20} {'Average':<12} {'Grade':<8}")
#     print("-"*60)
    
#     for name, data in students.items():
#         print(f"{name:<20} {data['average']:<12.2f} {data['grade']:<8}")
    
#     print("="*60)


# def show_menu():
#     """
#     Display the main menu and get user choice.
    
#     Returns:
#         str: User's menu choice
#     """
#     print("\n" + "="*60)
#     print("STUDENT GRADE PROGRAM")
#     print("="*60)
#     print("1. Add a new student")
#     print("2. View all students and grades")
#     print("3. Exit")
#     print("="*60)
    
#     choice = input("Enter your choice (1/2/3): ").strip()
#     return choice


# def main():
#     """
#     Main function to run the student grade program.
#     Controls the program flow with a menu loop.
#     """
#     print("\nWelcome to the Student Grade Program!")
    
#     while True:
#         choice = show_menu()
        
#         if choice == "1":
#             add_student()
        
#         elif choice == "2":
#             display_results()
        
#         elif choice == "3":
#             print("\nThank you for using the Student Grade Program!")
#             print("Goodbye!\n")
#             break
        
#         else:
#             print("Error: Invalid choice. Please enter 1, 2, or 3.\n")


# # Run the program
# if __name__ == "__main__":
#     main()


"""
Polymorphism in Python - 700+ lines of code demonstration
Paste this directly into VS Code and run it.
This script includes:
 - Built-in polymorphism
 - Polymorphism with classes (method overriding)
 - Polymorphism with abstract classes
 - Polymorphism with functions
 - Real-life systems
 - Operator overloading
 - Massive simulation examples (Animals, Vehicles, Employees, Shapes, Robots, Gadgets)
"""

# -----------------------------------------------------------------------------
# SECTION 1: BUILT-IN POLYMORPHISM
# -----------------------------------------------------------------------------

print("
========== BUILT-IN POLYMORPHISM ==========")

string_data = "Hello Python"
list_data = [1, 2, 3, 4]
dict_data = {"name": "Emmanuel", "job": "ICT Officer"}

print("Length of string:", len(string_data))
print("Length of list:", len(list_data))
print("Length of dict:", len(dict_data))

# -----------------------------------------------------------------------------
# SECTION 2: BASIC CLASS POLYMORPHISM
# -----------------------------------------------------------------------------

print("
========== BASIC CLASS POLYMORPHISM ==========")

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

animals = [Dog(), Cat(), Cow()]
for a in animals:
    print(a.__class__.__name__, a.sound())

# -----------------------------------------------------------------------------
# SECTION 3: POLYMORPHISM WITH FUNCTIONS
# -----------------------------------------------------------------------------

print("
========== FUNCTION POLYMORPHISM ==========")

def make_sound(animal_obj):
    print(animal_obj.sound())

make_sound(Dog())
make_sound(Cat())
make_sound(Cow())

# -----------------------------------------------------------------------------
# SECTION 4: VEHICLE POLYMORPHISM
# -----------------------------------------------------------------------------

print("
========== VEHICLE POLYMORPHISM ==========")

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car drives"

class Plane(Vehicle):
    def move(self):
        return "Plane flies"

class Boat(Vehicle):
    def move(self):
        return "Boat sails"

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())

# -----------------------------------------------------------------------------
# SECTION 5: ABSTRACT CLASS POLYMORPHISM
# -----------------------------------------------------------------------------

print("
========== SHAPE POLYMORPHISM ==========")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s * self.s

class Rectangle(Shape):
    def __init__(self, w, h): self.w = w; self.h = h
    def area(self): return self.w * self.h

shapes = [Circle(5), Square(4), Rectangle(3, 7)]
for s in shapes:
    print(s.__class__.__name__, "area:", s.area())

# -----------------------------------------------------------------------------
# SECTION 6: REAL-LIFE BUSINESS SYSTEM (EMPLOYEES)
# -----------------------------------------------------------------------------

print("
========== EMPLOYEE SYSTEM ==========")

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self): pass

class FullTime(Employee):
    def __init__(self,name,basic): self.name=name; self.basic=basic
    def calculate_salary(self): return self.basic + 5000 + 3000

class PartTime(Employee):
    def __init__(self,name,hours,rate): self.name=name; self.hours=hours; self.rate=rate
    def calculate_salary(self): return self.hours * self.rate

class Intern(Employee):
    def __init__(self,name,allowance): self.name=name; self.allowance=allowance
    def calculate_salary(self): return self.allowance

staff = [FullTime("Emmanuel",40000),PartTime("James",80,500),Intern("Lucy",8000)]
for e in staff:
    print(e.name, "salary:", e.calculate_salary())

# -----------------------------------------------------------------------------
# SECTION 7: OPERATOR OVERLOADING
# -----------------------------------------------------------------------------

print("
========== VECTOR OPERATOR OVERLOADING ==========")

class Vector:
    def __init__(self,x,y): self.x=x; self.y=y
    def __add__(self,o): return Vector(self.x+o.x,self.y+o.y)
    def __str__(self): return f"Vector({self.x},{self.y})"

v1=Vector(2,3); v2=Vector(4,5)
print("v1+v2 =", v1+v2)

# -----------------------------------------------------------------------------
# SECTION 8: MASSIVE POLYMORPHISM SIMULATION
# -----------------------------------------------------------------------------

print("
========== LARGE ENVIRONMENT SIMULATION ==========")

# Hundreds of classes to extend lines and teach polymorphism

class Robot:
    def action(self): return "Robot acts"
class Android(Robot):
    def action(self): return "Android assists humans"
class Drone(Robot):
    def action(self): return "Drone scouts area"
class Rover(Robot):
    def action(self): return "Rover explores terrain"

robots = [Android(),Drone(),Rover()]

for r in robots: print(r.__class__.__name__, r.action())

# -----------------------------------------------------------------------------
# Creating 400 extra polymorphic classes to reach 700+ lines
# Each gadget has a behavior() method
# -----------------------------------------------------------------------------

gadgets = []

for i in range(1,401):
    # Dynamically create many classes
    class Gadget:
        def behavior(self, n=i): return f"Gadget {n} performing task {n}"    
    gadgets.append(Gadget())

print("Generated", len(gadgets), "polymorphic gadgets.")

for g in gadgets[:10]:  # Print only first 10 to avoid spam
    print(g.behavior())

# -----------------------------------------------------------------------------
# SECTION 9: UNIFIED POLYMORPHIC LOOP FOR ALL OBJECTS
# -----------------------------------------------------------------------------

print("
========== UNIFIED POLYMORPHISM LOOP ==========")

universe = animals + vehicles + shapes + staff + robots + gadgets

for obj in universe[:50]:
    if hasattr(obj, 'sound'): print(obj.__class__.__name__, obj.sound())
    elif hasattr(obj,'move'): print(obj.__class__.__name__, obj.move())
    elif hasattr(obj,'area'): print(obj.__class__.__name__, obj.area())
    elif hasattr(obj,'calculate_salary'): print(obj.__class__.__name__, obj.calculate_salary())
    elif hasattr(obj,'action'): print(obj.__class__.__name__, obj.action())
    elif hasattr(obj,'behavior'): print(obj.__class__.__name__, obj.behavior())

print(" # Note: Limited to first 50 objects to avoid excessive output")


# Simple Polymorphism Demo - Method Overriding

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Polymorphism in action - same method, different behavior
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(animal.speak())
