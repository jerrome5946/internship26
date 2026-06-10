# a={'aby','aron','ananthapandmanapan'}
# fruit=input("Enter a fruit name: ")
# if 'fruit'  in a:  
#   print("fruit is not in the set")
# else:
#   print("fruit is in the set")
# logged=True
# if not logged:
#     print("Please log in to continue.")
# else:
#     print("Welcome back!")
# marks = 85
# attendance = 80

# if marks > 80 and attendance > 75:
#         print("Eligible for scholarship!")
# else:
#         print("Not eligible for scholarship.")
# text="hello world"
# search="h"
# if search in text:
#     print(f"'{search}' is found in the text.")\
# else:
#     print(f"'{search}' is not found in the text.")
# import random

# words = ["apple", "house", "table", "python"]
# word = random.choice(words)

# stages = [
# """
#  -----
#  |   |
#      |
#      |
#      |
#      |
# =========
# """,
# """
#  -----
#  |   |
#  O   |
#      |
#      |
#      |
# =========
# """,
# """
#  -----
#  |   |
#  O   |
#  |   |
#      |
#      |
# =========
# """,
# """
#  -----
#  |   |
#  O   |
# /|   |
#      |
#      |
# =========
# """,
# """
#  -----
#  |   |
#  O   |
# /|\\  |
#      |
#      |
# =========
# """,
# """
#  -----
#  |   |
#  O   |
# /|\\  |
# /    |
#      |
# =========
# """,
# """
#  -----
#  |   |
#  O   |
# /|\\  |
# / \\  |
#      |
# =========
# """
# ]

# guessed = []
# wrong = 0

# while wrong < 6:
#     # Display word
#     display = ""
#     for letter in word:
#         if letter in guessed:
#             display += letter + " "
#         else:
#             display += "_ "

#     print("\nWord:", display)

#     # Check win
#     if "_" not in display:
#         print("You Win!")
#         break

#     guess = input("Enter a letter: ").lower()

#     if guess in guessed:
#         print("Already guessed!")
#         continue

#     guessed.append(guess)

#     if guess in word:
#         print("Correct!")
#     else:
#         wrong += 1
#         print(stages[wrong])
#         print("Wrong guess! Attempts left:", 6 - wrong)

# if wrong == 6:
#     print(stages[6])
#     print("Game Over!")
#     print("The word was:", word)
# list1={'key':'value'}
# list2={'key':'value'}
# print(list1 is not list2)
# print(list1 ==list2)
# n=int(input("enter the no."))
# # a=int(input("enter the no."))
# # b=int(input("enter the no."))
# if(n>=1 and n<=5):
#     print("child")
# elif(n>=6 and n<=18):
#     print("teenager")
# elif(n>=19 and n<=59):
#     print("adult")
# else:
#      print("senior")    
    
# n=int(input("enter the no."))
# digit=len(str(n))
# if(digit==2):
#     print("is 2 digit")
# elif(digit==3):
#     print("is 3 digit")
# elif(digit==4):
#     print("is 4 digit") 
# else:
#     print("higher order")       
# n=int(input('enter no.'))   
# discount=0  
# if(n>=500):
#     discount=.20 
# elif(n>=200):
#     discount=.10       
# else:
#     discount=1
# applied=n*discount    
# total_amount=n-applied
# print(total_amount)       
# if(1<=n<=100):
#     print("inside")
# else:
#     print("outside")   
    