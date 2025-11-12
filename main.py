# # # print("Hellow world")

# # 7

# # # age = 25
# # # name = "Emmanuel"
# # # print(f"My name is {name} and I am {age} years old.")
# # # #Data Types in Python
# # # # Integer  
# # # weight = 70
# # # #String
# # # my_name = "Emmanuel"
# # # # a string is just a combination of characters
# # # # Float
# # # height = 5.9
# # # # Boolean
# # # print
# # # is_student = True_adult = age >= 18

# # # #User Input
# # # user_name = input("Enter your name: ")
# # # height = float(input("Enter your height in meters: "))
# # # print(f"Hello, {user_name}! You are {height} meters tall.") 

# # # print(height,user_name)

# # # #User input
# # # BMI = weight / (height ** 2)
# # # print(f"Your BMI is: {BMI:.2f}")
# # # print("Your BMI is: {:.2f}".format(BMI))

# # # #Type Conversion
# # # age_str = str(age)
# # # num1 = input("Enter  your first number: ") 
# # # num2 = input("Enter  your second number: ")
# # # sum_result = int(num1) + int(num2)
# # # print(f"The sum of {num1} and {num2} is {sum_result}.")

# # # # Student Marks

# # # # Get student name
# # # student_name = input("Enter student name: ")

# # # # Input marks for five subjects with subject names
# # # print(f"\nEnter marks for {student_name}:")
# # # math = float(input("Enter marks for Mathematics: "))
# # # english = float(input("Enter marks for English: "))
# # # science = float(input("Enter marks for Science: "))
# # # history = float(input("Enter marks for History: "))
# # # geography = float(input("Enter marks for Geography: "))

# # # # Create a list of tuples (subject_name, marks)
# # # subjects = [
# # #     ("Mathematics", math),
# # #     ("English", english),
# # #     ("Science", science),
# # #     ("History", history),
# # #     ("Geography", geography)
# # # ]

# # # # Sort subjects by marks in descending order (highest to lowest)
# # # ranked_subjects = sorted(subjects, key=lambda x: x[1], reverse=True)

# # # # Calculate total and average
# # # total_marks = math + english + science + history + geography
# # # average_marks = total_marks / 5

# # # # Print results
# # # print(f"\n{'='*50}")
# # # print(f"STUDENT MARKS REPORT - {student_name}")
# # # print(f"{'='*50}")

# # # print(f"\nSUBJECTS RANKED (Highest to Lowest):")
# # # print(f"{'-'*50}")
# # # for i, (subject, marks) in enumerate(ranked_subjects, 1):
# # #     print(f"{i}. {subject:<20} : {marks:.2f}")

# # # print(f"\n{'-'*50}")
# # # print(f"Total Marks     : {total_marks:.2f}")
# # # print(f"Average Marks   : {average_marks:.2f}")
# # # print(f"{'='*50}")

# # # #Product of two numbers

# # # num1 = int(input("Enter first number: "))
# # # num2 = int(input("Enter second number: "))    
# # # product = num1 * num2
# # # print(f"The product of {num1} and {num2} is {product}.") 
       
# # # #input three names in a single call to input()
# # # names = input("Enter three names separated by commas: ").split(",")
# # # name1, name2, name3 = [name.strip() for name in names]      
# # # print(f"Name 1: {name1}")
# # # print(f"Name 2: {name2}")       
# # # print(f"Name 3: {name3}")

# # # #Enter first name and last name in a single call to input()
# # # full_name = input("Enter your first and last name separated by a space: ").split(" ")           

# # # #Input age
# # # age = int(input("Enter your age: "))
# # # next_age = age + 1  
# # # print(f"Next year, you will be {next_age} years old.")

# # #store name,age favourite programming language,print them using variables
# # # name = input("Enter your name: ")
# # # age = int(input("Enter your age: "))
# # # fav_language = input("Enter your favourite programming language: ") 
# # # print(f"Name: {name}, Age: {age}, Favourite Programming Language: {fav_language}")  

# # # #Input year of birth, currectyear and print age
# # # year_of_birth = input("Kindly input your year of birth; ")
# # # current_year = input("Kindly input the current year; ")

# # # age = int(current_year)-int (year_of_birth)

# # print("Your current age is {age}years old")

# # #input weight in kg and convert to grams
# # weight_kg = float(input("Enter your weight in kilograms: "))        
# # weight_grams = weight_kg * 1000
# # print(f"Your weight in grams is: {weight_grams} grams.")


# # #logical operators
# # age1 = int(input("Enter age of first person: "))
# # age2 = int(input("Enter age of second person: "))       
# # is_older = age1 > age2
# # print(f"Is the first person older than the second? {is_older}")


















# # conditional statements

# #if else
# score = int(input("Enter a number: "))
# if score >= 80:
#     print("Grade A.")
# elif score >= 60:
#     print("Grade B.")
# elif score >= 50:
#     print("Grade C.")
# elif score >= 40:
#     print("Grade D.")    
# elif score >= 0:
#     print("Grade F.")   
# else:
#     print("Invalid score, enter number between 0 and 100.")
    
    #while loop complexities
    
i = 1
while i <= 5:
    print(f"Iteration {i}")
    i += 1
    
for y in 'python':
    print(y)    

    
    



