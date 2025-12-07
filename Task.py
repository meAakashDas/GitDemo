# 1. Take 3 numbers and print the largest numbernum1=int(input('enter the first number'))

# num2=int(input('enter the second number'))
# num3=int(input('enter the third number'))
# if num1>num2 and num1>num3 :
#   print('first number is greater')
# elif num2>num1 and num2>num3 :
#   print('second number is greater')
# else :
#   print('third number is the greatest')

# -----------------------------------------------------------------------------------------------

#2. Take a month number (1–12) and print the month name

# number=int(input('enter the number'))
# if number==1 :
#   print('jan')
# elif number ==2 :
#   print('feb')
# elif number ==3 :
#   print('march')
# elif number ==4 :
#   print('april')
# elif number ==5 :
#   print('may')
# elif number ==6 :
#   print('june')
# elif number ==7 :
#   print('july')
# elif number ==8 :
#   print('august')
# elif number ==9 :
#   print('sep')
# elif number ==10 :
#   print('oct')
# elif number ==11 :
#   print('nov')
# else: number ==12
# print('dec')

# -------------------------------------------------------------------------------------------------------------

# 3. Write a program to swap two variables

# num1=int(input('enter tert the first number'))
# num2=int(input('enter tert the second number'))
# num1,num2=num2,num1
# print(num1)
# print(num2)
# # -------------------------------------------------------------------------------------------------------------

# num1=int(input('enter tert the first number'))
# num2=int(input('enter tert the second number'))
# num1=num1^num2
# num2=num1^num2
# num1=num1^num2
# print(num1)
# print(num2)
# # -------------------------------------------------------------------------------------------------------------
# num1=20
# num2=25
# x=num1
# num1=num2
# num2=x
# print(num1) 
# print(num2) 

# -------------------------------------------------------------------------------------------------------------

# 4. You are developing a simple ticket booking system for a movie theatre. The ticket
# price depends on the age of the person and whether they have a membership card. If
# the person is under 12, the ticket is free. If the person is between 12 and 60: if they
# have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs 200. If the
# person is above 60, they get a senior citizen discount, and then ticket costs Rs 100.
# Write a python program using nested if-else to calculate and print the ticket price
# based on the users age and membership status

# age=int(input('enter your age'))
# if age<12 :
#   print('your ticket is free')
# elif age>=12 and age<=60 :
#   membership_card=input('do you have a membership card? yes or no')
#   if membership_card=='yes' :
#     print('your ticket costs Rs.150')
#   else:
#     print('your ticket costs Rs.200')
# else:
#   print('your ticket costs Rs.100')

#*************************************************************************************************************

# A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
# Next units: Rs 8
# If usage is > 300 units:
# First 100: Rs 5
# Next 200: Rs 8
# Remaining: Rs 10


# units = int(input("Enter electricity usage in units: "))
# total_cost = 0

# if units < 100:
#     total_cost = units * 5
# elif units <= 300:
#     # First 100 units cost Rs 5
#     # Remaining units cost Rs 8
#     total_cost = (100 * 5) + ((units - 100) * 8)
# else: # usage is > 300
#     # First 100 units cost Rs 5
#     # Next 200 units cost Rs 8
#     # Remaining units cost Rs 10
#     total_cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)

# print(f"Total cost: Rs {total_cost}")

# units = int(input("Enter electricity usage in units: "))
# total_cost = 0

# if units < 100:
#     total_cost = units * 5
# elif units <= 300:
#     # First 100 units cost Rs 5
#     # Remaining units cost Rs 8
#     total_cost = (100 * 5) + ((units - 100) * 8)
# else: # usage is > 300
#     # First 100 units cost Rs 5
#     # Next 200 units cost Rs 8
#     # Remaining units cost Rs 10
#     total_cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)

# print(f"Total cost: Rs {total_cost}")


# # To calculate desks needed, we divide students by 2.
# # If the number is odd, we need one extra desk (integer division rounds down, so we add the remainder).

# class_a = int(input("Enter number of students in Class A: "))
# class_b = int(input("Enter number of students in Class B: "))
# class_c = int(input("Enter number of students in Class C: "))

# desks_a = (class_a // 2) + (class_a % 2)
# desks_b = (class_b // 2) + (class_b % 2)
# desks_c = (class_c // 2) + (class_c % 2)

# total_desks = desks_a + desks_b + desks_c
# print(f"Total desks needed: {total_desks}")


# current_floor = 5
# target_floor = 3 # You can change this or make it an input

# if target_floor > current_floor:
#     print("Lift is going up.")
# elif target_floor < current_floor:
#     print("Lift is going down.")
# else:
#     print("Lift stays at current floor.")

#     num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 0:
#         print("The number is Positive and Even.")
#     else:
#         print("The number is Positive and Odd.")
# else:
#     print("The number is not positive.")

#     num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if num1 > num2:
#     print(f"{num1} is greater.")
# elif num2 > num1:
#     print(f"{num2} is greater.")
# else:
#     print("Both numbers are equal.")
#     if num1 > 0:
#         print("The number is positive.")
#     elif num1 < 0:
#         print("The number is negative.")
#     else:
#         print("The number is zero.")




#         num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print("Fizz Buzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)



# import random

# random_num = random.randint(0, 5)

# if random_num == 0:
#     print("Flamingos turn pink from eating shrimp.")
# elif random_num == 1:
#     print("The only food that doesn't spoil is honey.")
# elif random_num == 2:
#     print("Shrimp can only swim backwards.")
# elif random_num == 3:
#     print("A taste bud's life span is about 10 days.")
# elif random_num == 4:
#     print("It is impossible to sneeze while sleeping.")
# elif random_num == 5:
#     print("It is illegal to sing off-key in North Carolina.")



# total_amount = float(input("Enter total purchase amount: "))
# member_input = input("Is the customer a member? (yes/no): ").lower()

# is_member = (member_input == "yes")
# discount = 0

# if total_amount > 1000:
#     if is_member:
#         discount = total_amount * 0.20
#     else:
#         discount = total_amount * 0.10

# final_amount = total_amount - discount
# print(f"Final amount to pay: Rs {final_amount}")



# earth_weight = float(input("Enter your Earth weight: "))
# planet_num = int(input("Enter planet number (1-7): "))

# if planet_num == 1:
#     # Mercury
#     print(f"Your weight on Mercury is {earth_weight * 0.38}")
# elif planet_num == 2:
#     # Venus
#     print(f"Your weight on Venus is {earth_weight * 0.91}")
# elif planet_num == 3:
#     # Mars
#     print(f"Your weight on Mars is {earth_weight * 0.38}")
# elif planet_num == 4:
#     # Jupiter
#     print(f"Your weight on Jupiter is {earth_weight * 2.53}")
# elif planet_num == 5:
#     # Saturn
#     print(f"Your weight on Saturn is {earth_weight * 1.07}")
# elif planet_num == 6:
#     # Uranus
#     print(f"Your weight on Uranus is {earth_weight * 0.89}")
# elif planet_num == 7:
#     # Neptune
#     print(f"Your weight on Neptune is {earth_weight * 1.14}")
# else:
#     print("Invalid planet number")



# sub1 = float(input("Enter marks for subject 1: "))
# sub2 = float(input("Enter marks for subject 2: "))
# sub3 = float(input("Enter marks for subject 3: "))
# sub4 = float(input("Enter marks for subject 4: "))

# total = sub1 + sub2 + sub3 + sub4
# percentage = (total / 400) * 100  # Assuming each subject is out of 100

# print(f"Total Marks: {total}")
# print(f"Percentage: {percentage}%")

# if percentage > 70:
#     print("Grade: Distinction")
# elif percentage > 60:
#     print("Grade: First Division")
# elif percentage > 40:
#     print("Grade: Pass")
# else:
#     print("Grade: Fail")


# cost_price = float(input("Enter cost price of the bike: Rs "))
# tax = 0

# if cost_price > 100000:
#     tax = cost_price * 0.15
# elif cost_price > 50000:
#     tax = cost_price * 0.10
# else:
#     tax = cost_price * 0.05

# print(f"Road tax to be paid: Rs {tax}")