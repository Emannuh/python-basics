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