n=int(input("enter the no of input :"))
even_count=0
odd_count=0
for i in range(n):
    num=int(input("enter the input :"))
    if num%2==0:
      even_count+=1
    else:
      odd_count+=1
      
      
print("thw even",even_count)
print("thw dd",odd_count)
      
n=int(input("enter tthe number::"))

for i in range(1, n + 1 ):
      for j in range(1, i + 1):
          print(j, end='')

  
      print()
    import math

1. Get the coordinates for the first point
import math
print("Enter coordinates for Point 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

# 2. Get the coordinates for the second point
print("\nEnter coordinates for Point 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# 3. Calculate the distance using the formula
# In Python, ** 2 means "squared"
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 4. Print the final result, rounded to 2 decimal places
print(f"\nThe distance between ",distance)
Get the number of rows from the user
n = int(input("Enter the number of rows (N <= 26): "))

# Check if the input is within the valid range
if 1<= n <= 26:
    for i in range(1, n + 1):           # Outer loop for the number of rows
        for j in range(i):              # Inner loop for printing characters
            # 65 is the ASCII value for 'A'
            # Adding 'j' moves it to 'B', 'C', etc.
            print(chr(65 + j), end=' ') 
        print()                         # Move to the next line after each row
else:
    print("Invalid input! Please enter a number between 1 and 26.")

def dictative(input_str):
    dict={}
    for i in input_str:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict
input_str=input("enter the string :")
result=dictative(input_str)
print (result)
def separate_numbers():
    positive_list = []
    negative_list = []
    original_list = []
    
    # Ask the user how many numbers they want to input
    n = int(input("Enter the number of integers (n): "))
    
    # Read n integers from the user
    for i in range(n):
        num = int(input(f"Enter integer {i+1}: "))
        original_list.append(num)
        
        # Separate the logic
        # Note: 0 is generally considered neither positive nor negative, 
        # but in programming contexts it's often grouped with positives.
        if num >= 0: 
            positive_list.append(num)
        else:
            negative_list.append(num)
            
    print("\nResults:")
    print("Original List:", original_list)
    print("Positive Numbers:", positive_list)
    print("Negative Numbers:", negative_list)

# To run the program, you would call:
separate_numbers()
def birthday_lookup():
    # Create the initial dictionary of names (keys) and birthdays (values)
    birthdays = {
        'Albert Einstein': 'March 14, 1879',
        'Ada Lovelace': 'December 10, 1815',
        'Alan Turing': 'June 23, 1912',
        'Grace Hopper': 'December 9, 1906'
    }
    
    print("Welcome to the Birthday Dictionary!")
    print(f"We know the birthdays of: {', '.join(birthdays.keys())}")
    
    # Ask the user for a name
    name_to_find = input("\nEnter a name to find their birthday: ")
    
    # Check if the name exists in the dictionary and display the result
    if name_to_find in birthdays:
        print(f"\n{name_to_find}'s birthday is {birthdays[name_to_find]}.")
    else:
        print(f"\nSorry, we don't have birthday information for '{name_to_find}'.")

# To run the program, you would call:
birthday_lookup()
Birthdays={'A':'03/14/1879','B':'03/14/1879','C':'03/14/1879','D':'06/14/18669',} 
print("Who's birthday do you want to look up?'"A) 
In_name = input() 
print(Birthdays[In_name]) 

import turtle

Create a turtle screen and object


Loop 5 times to draw the 5 points of the star
for i in range(5):
    turtle.forward(100) # Move forward 100 units
    turtle.right(144) 
    turtle.speed(1)# Turn right by 144 degrees

Keep the window open until clicked
screen.exitonclick()
data = "Python rules!"

# a. Obtain a list of the words
words_list = data.split()

# b. Convert to uppercase
upper_string = data.upper()

# c. Locate the position of "rules"
position = data.find("rules")

# d. Replace exclamation with question mark
replaced_string = data.replace("!", "?")
print(data,words_list,position,replaced_string)
def count_four_letter_words(filename):
    try:
        inputfilee=open(filename, 'r') 
        content =inputfilee.read()
        words = content.split()
            
        count = 0
        for word in words:
                # Strip basic punctuation to accurately count letters
                clean_word = word.strip(".,!?") 
                if len(clean_word) == 4:
                    count += 1
                    
        print(f"Number of 4-letter words: {count}")
    except FileNotFoundError:
        print("File not found.")

count_four_letter_words("content.txt")
numbers_list = [-5, 12, -3, 8, 0, -1, 4]

# filter() takes the lambda function (condition) and the list
positive_numbers = list(filter(lambda x: x > 0, numbers_list))

print("Positive numbers:", positive_numbers)        
class MyClass: 
    def __init__(self, name): 
        self.name = name 
     
    def __del__(self): 
        print(f"Destroying instance of {self.name}") 
 
# Example usage 
obj1 = MyClass("Object 1") 
obj2 = MyClass("Object 2") 
 
del obj1 
del obj2 
class DistanceConverter: 

    def __init__(self): 
        self.distance_km = 0 
     
    def  get_distance(self): 
        self.distance_km = float(input("Enter the distance in kilometers: ")) 
     
    def print_distance(self): 
        distance_meter = self.distance_km * 1000 
        print("Distance in meters:", distance_meter) 
        
c=DistanceConverter()
c.get_distance()
c.print_distance()

print("prime ")
for n in range(2,1000):
 i=2
 while i<=n/2:
  if n%i==0:
   break
 i=i+1
 else:
  print(n,end="" )
  print() 
x1=int(input("enter x1 : ")) 
x2=int(input("enter x2 : ")) 
y1=int(input("enter y1 : ")) 
y2=int(input("enter y2 : ")) 
result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5) 
print(round(result))
   
def t_even(first,last):
  for i  in range(first,last):
   if i%2==0:
    print(f"{i}iseven")
    print()
   else:
    print(f"{i}isodd")
     
  return
# t_even(1,25)              
class DistanceTracker:
    def __init__(self):
        self.distance_km = 0.0

    def get_distance(self):
        # Accept distance in kilometres from the user
        self.distance_km = float(input("Enter distance in kilometres: "))

    def print_distance(self):
        # Convert to meters and print
        distance_meters = self.distance_km * 1000
        print(f"The distance is {distance_meters} meters.")
# DistanceTracker().get_distance()
# DistanceTracker().print_distance()
# 1. Create an instance of the class
tracker = DistanceTracker()

# 2. Call the method to get user input
tracker.get_distance()

# 3. Call the method to convert and print the result
tracker.print_distance()
import turtle
import time

t = turtle.Turtle()
t.fillcolor("blue")

# Start filling the shape
t.begin_fill()

# Side 1
t.forward(100)
t.left(72)
time.sleep(2) # 2 second delay

# Side 2
t.forward(100)
t.left(72)
time.sleep(2)

# Side 3
t.forward(100)
t.left(72)
time.sleep(2)

# Side 4
t.forward(100)
t.left(72)
time.sleep(2)

# Side 5
t.forward(100)
t.left(72)

# Complete the fill
t.end_fill()

turtle.done()