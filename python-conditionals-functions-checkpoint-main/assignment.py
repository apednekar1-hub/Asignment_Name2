# Name: Antariksh
# Period: PM

# ============================================================
# Python Skills Check — Slides 61–116
# CONDITIONALS & FUNCTIONS — CHALLENGE VERSION
# ============================================================

# DIRECTIONS
# ============================================================
# - I recommend you create a repo first and clone it.
# - Drag this file into your repo and push when you are done.
#
# Complete each task underneath its directions.
#
# RULES:
# - Use ONLY concepts we have learned in class.
# - Use the EXACT variable and function names provided.
# - Do not delete the directions.
# - Your entire Python file must run without errors.
# - Do NOT manually type an answer that Python should determine.
# - Pay attention to indentation.
# - Read carefully. MANY questions are intentionally tricky.
# - Unless a task says otherwise, do NOT use min() or max().
# - Your conditions should work even if the variable values are changed.
#
# IMPORTANT:
# Some questions are designed so that the ORDER of your conditions matters.
# Some questions have edge cases such as ties or boundary values.
# Test your logic carefully.


# ============================================================
# SECTION 1 — COMPARISON WARM-UP
# ============================================================

# TASK 1:
# Create: 
#
number_one = 25
number_two = 40
#
def number_greator(number_one, number_two):
    if number_one > number_two:
        return number_one
    elif number_two > number_one:
     return "number_two is greater"
     
answer = number_greator(number_one, number_two)
print(answer)

# Write an if statement that prints:
#
# number_two is greater
#
# ONLY if number_two is greater than number_one.


# TASK 2:
# Create:
#
score = 80
def score_number(score):
   if score >= 70:
    return "Passing Score"

score_result = score_number(score)
print(score_result)

#
# Print:
# Passing score
#
# if score is GREATER THAN OR EQUAL TO 70.


# TASK 3:
# Create:
#
lives = 0
#
def life(lives):
   if lives == 0:
    return "Game Over"

life_result = life(lives)
print(life_result)

# Print:
# Game over
#
# ONLY if lives is exactly 0.


# TASK 4:
# Create:
#
username = "student"
#
def verify_user(username):
  if username == "admin":
    return "Approved"
  else: username == "invalid"
  return "Different username"

user_verification = verify_user(username)
print(user_verification)

# Print:
# Different username
#
# ONLY if username is NOT equal to "admin".


# ============================================================
# SECTION 2 — BOUNDARIES & ORDER MATTER
# ============================================================

# TASK 5:
# Create:
#
age = 18
#
def calculated_age(age):
  if age >= 65:
    return "Age is over 65"
  elif age >= 18 and age <= 64:
    return "Age is through 64"
  else:
    return "Age is under 13"

age_calculated = calculated_age(age)
print(age_calculated)
  
# Print:
# Child       if age is under 13
# Teen        if age is 13 through 17
# Adult       if age is 18 through 64
# Senior      if age is 65 or older
#
# Use if / elif / else.
#
# THINK:
# Which condition should be checked first?


# TASK 6:
# Create:
#
grade = 90
#
def grade_levl(grade):
  if grade >= 90:
    return "A"
  elif grade <= 89 and grade >= 80:
    return "B"
  elif grade <= 79 and grade >= 70:
    return "C"
  else:
    return "F"

grade_level = grade_levl(grade)
print(grade_level)

# Print:
# A if grade is 90 or higher
# B if grade is 80–89
# C if grade is 70–79
# D if grade is 60–69
# F if grade is below 60
#
# IMPORTANT:
# grade = 90 should print ONLY:
# A


# TASK 7:
# Create:
#
temp = 70
#
def temp_calcuated(temp):
  if temp >= 90:
    return "Hot"
  elif temp <= 89 and temp >= 70:
    return "Warm"
  elif temp <= 69 and temp >= 50:
    return "Mild"
  else:
    return "Cold"

calculated_temp = temp_calcuated(temp)
print(calculated_temp)

# Print:
# Cold       if below 50
# Mild       if 50 through 69
# Warm       if 70 through 89
# Hot        if 90 or higher
#
# Be careful with 50, 70, and 90.


# TASK 8:
# Create:
#
speed = 65
#
def speed_calculated(speed):
  if speed < 25:
    return "Too Slow"
  elif speed >= 25 and speed <= 65:
    return "Normal"
  elif speed >= 66 and speed <= 80:
    return "Speeding"
  else:
    return "Reckless"
    
calculated_speed = speed_calculated(speed)
print(calculated_speed)

# Print:
# Too Slow       if speed is below 25
# Normal         if speed is 25 through 65
# Speeding       if speed is 66 through 80
# Reckless       if speed is above 80
#
# The value 65 must print:
# Normal


# TASK 9:
# Create:
#
amount = 100
#
def purchase_amount(amount):
  if amount < 25:
    return "Small purchase"
  elif amount >= 25 and amount <= 99:
    return "Mediun purchase"
  elif amount >= 100 and amount <= 499:
    return "Large purchase"
  else:
    return "Huge purchase"

amount_purchase = purchase_amount(amount)
print(amount_purchase)

# Print:
# Small purchase       if amount is below 25
# Medium purchase      if amount is 25 through 99
# Large purchase       if amount is 100 through 499
# Huge purchase        if amount is 500 or more
#
# THINK carefully about your comparison operators.


# ============================================================
# SECTION 3 — AND / OR THINKING
# ============================================================

# TASK 10:
# Create:
#
age = 16
has_ticket = True
#
def age_ticket(age, has_ticket):
  if age >= 13 and has_ticket == True:
    return "You may enter"
  else:
    return "Entry denied"
  
ticket_age = age_ticket(age, has_ticket)
print(ticket_age)

# Print:
# You may enter
#
# ONLY if age is at least 13 AND has_ticket is True.
#
# Otherwise print:
# Entry denied


# TASK 11:
# Create:
#
temperature = 91
#
def temp_lvl(temperature):
  if temperature < 32 or temperature > 90:
    return "Extreme temperature"
  else: 
    return "Normal temperature"

lvl_temp = temp_lvl(temperature)
print(lvl_temp)

# Print:
# Extreme temperature
#
# if temperature is below 32 OR above 90.
#
# Otherwise print:
# Normal temperature


# TASK 12:
# Create:
#
username = "admin"
password = "python123"
#
def user_pass(username, password):
  if username == "admin" and password == "python123":
    return "Acess granted"
  else: 
    return "Acess denied"

pass_user = user_pass(username, password)
print(pass_user)

# Print:
# Access granted
#
# ONLY if BOTH values are correct.
#
# Otherwise print:
# Access denied


# TASK 13:
# Create:
#
age = 70
has_membership = False

def discount(has_membership, age):
  if age >= 65 or has_membership == True:
    return "discount applies"
  else:
    return "No discount"

validated_discount = discount(has_membership, age)
print(validated_discount)


#
# Print:
# Discount applies
#
# if the person is 65 or older OR has_membership is True.
#
# Otherwise print:
# No discount


# TASK 14:
# Create:
#
number = 25
#
def range_number(number):
  if number >= 10 and number <= 30:
    return "In range"
  else: 
    return "Out of range"

number_range = range_number(number)
print(number_range)

# Print:
# In range
#
# if number is from 10 through 30 INCLUDING 10 and 30.
#
# Otherwise print:
# Out of range


# TASK 15:
# Create:
#
number = 10
#
def range_number(number):
  if number < 20 or number > 80:
    return "Outside middle function"
  else:
    return "Inside middle number"

n_range = range_number(number)
print(n_range)

# Print:
# Outside middle range
#
# if number is LESS THAN 20 OR GREATER THAN 80.
#
# Otherwise print:
# Inside middle range
#
# Test mentally with:
# 10
# 50
# 90


# ============================================================
# SECTION 4 — HIGHEST / LOWEST / MIDDLE
# ============================================================

# TASK 16:
# Create:
#
a = 12
b = 7
c = 19
#
def highest_value(c, b, a):
  if a > b and a > c:
    return "a is highest"
  elif b > a and b > c:
    return "b is highest"
  elif c > b and c > a:
    return "c is highest"

value_high = highest_value(c, b, a)
print(value_high)

# WITHOUT using max(), determine which variable contains
# the HIGHEST value.
#
# Print:
# a is highest
# OR
# b is highest
# OR
# c is highest


# TASK 17:
# Create:
#
x = 44
y = 13
z = 28
#
def lowest_value(x, y, z):
  if x < y and x < z:
    return (x, " is the lowest")
  elif y < x and y < z:
    return (y, " is the lowest")
  else:
    return (z, " is the lowest")

value_lowest = lowest_value(x, y, z)
print(value_lowest)

# WITHOUT using min(), determine which variable contains
# the LOWEST value.
#
# Print the correct variable name followed by:
# is lowest


# TASK 18:
# Create:
#
num1 = 10
num2 = 30
num3 = 20
#
def middle_value(num1, num2, num3):
  if num1 < num3 and num1 > num2:
    print(num1)
  elif num2 < num1 and num2 > num3:
    print(num2)
  else:
    print(num3)

value_middle = middle_value(num1, num2, num3)

# WITHOUT using min(), max(), or sorting,
# determine the MIDDLE value.
#
# Print:
# Middle: [value]
#
# HINT:
# The middle value is not the highest and not the lowest.


# TASK 19:
# Create:
#
first = 20
second = 20
third = 8
#
def highest_number(first, second, third):
  if first > second and first > third:
    return "First is highest"
  elif second > first and second > third:
    return "Second is highest"
  elif third > first and third > second:
    return "Third is highest"
  if first == second:
    return "First and Second are tied"
  elif first == third:
    return "First is tied with Third"
  elif second == first:
    return "Second is tied with first"
  elif second == third:
    return "Second is tied with third"
  elif third == first:
    return "Third is tied with first"
  elif third == second:
    return "Third is tied with second"

number_highest = highest_number(first, second, third)
print(number_highest)

# Determine what is highest.
#
# Your program must correctly handle the tie.
#
# Possible outputs:
# first is highest
# second is highest
# third is highest
# first and second are tied for highest
# first and third are tied for highest
# second and third are tied for highest
# all three are tied


# TASK 20:
# Create:
#
first = 5
second = 5
third = 5
#
def equal_numbers(first, second, third):
  if first == second and second == third:
    return "All three are equal"
  elif first == second or second == third or first == third:
    return "Two are equal"
  else:
    return "None of the numbers are equal"

numbers_equal = equal_numbers(first, second, third)
print(numbers_equal)


# Determine whether:
#
# - all three are equal
# - exactly two are equal
# - none are equal
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Your code should still work if the values are changed.


# TASK 21:
# Create:
#
a = 9
b = 9
c = 9
#
def number_match(a, b, c):
  if a == c or b == c:
    return "A match exists"
  else:
    return "No match"

match_number = number_match(a, b, c)
print(match_number)


# Determine whether AT LEAST TWO numbers match.
#
# Print:
# A match exists
#
# Otherwise print:
# No match


# TASK 22:
# Create:
#
a = 14
b = 7
c = 20
#
def number_look(a, b, c):
  if a > b and a < c or a < b and a > c:
    return "a is between be and c"
  else:
    return "a is not between b and c"

look_number = number_look(a, b, c)
print(look_number)
  

# Determine whether a is BETWEEN b and c.
#
# Print:
# a is between b and c
#
# if that is true.
#
# Otherwise print:
# a is not between b and c
#
# IMPORTANT:
# Your code should still work if b is greater than c.


# TASK 23:
# Create:
#
a = 30
b = 20
c = 70
#
def low_high(a, b, c):
  if a > c or a < b:
    return "Different order"
  elif b < c and c > b:
    return "Correct order"
  else:
    return "Different order"

high_low = low_high(a, b, c)
print(high_low)

# Determine whether b is the lowest AND c is the highest.
#
# If BOTH are true, print:
# Correct order
#
# Otherwise print:
# Different order


# ============================================================
# SECTION 5 — USER INPUT LOGIC
# ============================================================

# TASK 24:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
first_number = input("Give me a whole number: ")
second_number = input("Give me a whole number: ")
third_number = input("Give me a whole number: ")
#
# WITHOUT using min() or max(), print the LOWEST number.
def low_number(first_number, second_number, third_number):
  if first_number < second_number and first_number < third_number:
    return "First number is lowest"
  elif second_number < first_number and second_number < third_number:
    return "Second number is lowest"
  else:
    return "Third number is lowest"

number_low = low_number(first_number, second_number, third_number)
print(number_low)


# TASK 25:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
value1 = input("Give me a whole number: ")
value2 = input("Give me a whole number: ")
value3 = input("Give me a whole number: ")
#
# WITHOUT using min() or max(), print the HIGHEST number.
def highest_number(value1, value2, value3):
   if value1 > value2 and value1 > value3:
      return "First number is highest"
   elif value2 > value1 and value2 > value3:
      return "Second number is highest"
   else:
      return "Third number is highest"

number_highest = highest_number(value1, value2, value3)
print(number_highest)

# TASK 26:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
n1 = int(input("Enter in a whole number: "))
n2 = int(input("Enter in a whole number: "))
n3 = int(input("Enter in a whole number: "))

def increase_n(n1, n2, n3):
  if n1 > n2 and n1 > n3 and n2 > n3:
    return "Increasing"
  else:
    return "Not increasing"

n_increase = increase_n(n1, n2, n3)
print(n_increase)

#
# Determine whether the user entered them in STRICTLY increasing order.
#
# Example:
# 3, 8, 10 -> Increasing
#
# 3, 3, 10 -> NOT Increasing
#
# Print:
# Increasing
# OR
# Not increasing


# TASK 27:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
n1 = int(input("Enter in a whole number: "))
n2 = int(input("Enter in a whole number: "))
n3 = int(input("Enter in a whole number: "))
#
def decreasing_n(n1, n2, n3):
  if n1 > n2 and n1 > n3 and n2 > n3:
    return "Decreasing"
  else:
    return "Not Decreasing"

n_decreasing = decreasing_n(n1, n2, n3)
print(n_decreasing)

# Determine whether the numbers are in STRICTLY decreasing order.
#
# Print:
# Decreasing
# OR
# Not decreasing


# TASK 28:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
a = input("Give me three whole #s: ")
b = input("Give me three whole #s: ")
c = input("Give me three whole #s: ")

def matching_numbers(a, b, c):
  if a == b and b == c:
    return "All same"
  elif b == c or b == a:
    return "Two same"
  elif c == a or c == b:
    return "Two same"
  elif a == b and a == c:
    return "Two same"
  else:
    return "All different"

numbers_matching = matching_numbers(a, b, c)
print(numbers_matching)

#
# Print:
# All same
# if all three match
#
# Two same
# if exactly two match
#
# All different
# if none match


# TASK 29:
# Ask the user for a score from 0 to 100.
#
# Store it in:
#
user_score = int(input("Give me a score from 0 to 100: "))
#
def score_look(user_score):
  if user_score < 0 or user_score > 100:
    return "Invalid Score"
  elif user_score <= 59:
    return "F"
  elif user_score >= 60 and user_score <= 69:
    return "D"
  elif user_score >= 70 and user_score <= 79:
    return "C"
  elif user_score >= 80 and user_score <= 89:
    return "B"
  else:
    return "A"

look_score = score_look(user_score)
print(look_score)

# FIRST determine if the score is valid.
#
# If it is below 0 OR above 100, print:
# Invalid score
#
# Otherwise print the letter grade:
# A, B, C, D, or F
#
# THINK:
# You should not assign a letter grade to an invalid score.


# ============================================================
# SECTION 6 — FUNCTIONS BASICS
# ============================================================

# TASK 30:
# Create a function named:
#
def say_hello():
    print("Hello!")

hello = say_hello()

#
# It should print:
# Hello!
#
# Call it once.


# TASK 31:
# Create a function named:
#
name = input("Put name: ")

def greet_student(name):
  print("Hello", name)

student_greet = greet_student(name)

#
# Give it ONE parameter:
#
# name
#
# Print:
# Hello [name]
#
# Call it THREE times using different names.


# TASK 32:
# Create a function named:
#

#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print the sum of all three.
#
# Call it at least TWO times.

def add_three(a, b, c):
  print(a + b + c)

add_three(10, 15, 2)
add_three(12, 13, 1)

# ============================================================
# SECTION 7 — FUNCTIONS + CONDITIONALS
# ============================================================

# TASK 33:
# Create a function named:
#
def check_number(number):
  if number < 0:
    return "Negative"
  elif number > 0:
    return "Postive"
  else:
    return "Zero"

number_check = check_number(10)
print(number_check)

# Give it ONE parameter:
#
# number
#
# Print:
# Positive
# Negative
# or
# Zero
#
# Call it using:
# 10
# -5
# 0


# TASK 34:
# Create a function named:
#

def check_even_odd(number):
  if number % 2 != 0:
    print ("Odd")
  else:
    print ("Even")
check_even_odd(11)
  
#
# Give it ONE parameter:
#
# number
#
# Print:
# Even
# OR
# Odd
#
# Test it at least FOUR times.


# TASK 35:
# Create a function named:
#
def ticket_type(age):
  if age < 13:
    print("Child")
  elif age >= 13 and age <= 17:
    print("Teen")
  elif age >= 18 and age <= 64:
    print("Adult")
  else:
    print("Senior")

ticket_type(12)
ticket_type(13)
ticket_type(17)
ticket_type(18)
ticket_type(64)
ticket_type(65)

#
# Give it ONE parameter:
#
# age
#
# Print:
# Child
# Teen
# Adult
# Senior
#
# using these ranges:
#
# Child: under 13
# Teen: 13–17
# Adult: 18–64
# Senior: 65+
#
# Test boundary values:
# 12
# 13
# 17
# 18
# 64
# 65


# TASK 36:
# Create a function named:
#
def find_highest(a, b, c):
  if a < b and c < b:
    print("B is the highest")
  elif c < a and b < a:
    print("A is the highest")
  else:
    print("C is the highest")

find_highest(5, 20, 11)
find_highest(100, 25, 60)
find_highest(8, 9, 30)

#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), print the highest value.
#
# Test:
# find_highest(5, 20, 11)
# find_highest(100, 25, 60)
# find_highest(8, 9, 30)


# TASK 37:
# Create a function named:
#
def find_lowest(a, b, c):
  if a > b and c > b:
     print("B is the lowest")
  elif c > a and b > a:
      print("A is the lowest")
  else:
      print("C is the lowest")

find_lowest(2, 3, 4)
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), print the lowest value.
#
# Test at least THREE times.


# TASK 38:
# Create a function named:
#
def find_middle(a, b, c):
  if a < b and a < c and c < b:
    print("The middle is C")
  elif a < b and a < c and b < c and b > a:
    print("The middle is B")
  else:
    print("The middle is A")

find_middle(10, 30, 20)
     
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), max(), or sorting,
# print the MIDDLE value.
#
# Test:
# find_middle(10, 30, 20)
# find_middle(100, 5, 50)
# find_middle(7, 9, 8)


# TASK 39:
# Create a function named:
#
def compare_three(a, b, c):
  if a == b and a != c:
    print("Exactly Two Equal")
  elif a == c and a != b:
    print("Exactly Two Equal")
  else:
    print("All different")

compare_three(2, 3, 2)
      
#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Test all three situations.


# TASK 40:
# Create a function named:
#
def is_in_range(number, low, high):
  if number > low < high:
    print("In range")
  elif number < high > low:
    print("In of Range")
  else:
    print("Out of Range")
is_in_range(10, 40, 50)

#
# Give it THREE parameters:
#
# number
# low
# high
#
# Print:
# In range
#
# if number is between low and high INCLUDING the endpoints.
#
# Otherwise print:
# Out of range
#
# IMPORTANT:
# Your function should still work if low and high
# are accidentally passed in backwards.
#
# Example:
# is_in_range(50, 100, 1)
#
# should still print:
# In range


# ============================================================
# SECTION 8 — RETURN VALUES
# ============================================================

# TASK 41:
# Create a function named:
#
def multiply_numbers(num1, num2):
  return num1 * num2

mutiplication_result = multiply_numbers(6, 7)
print(mutiplication_result)
#
# Give it TWO parameters:
#
# num1
# num2
#
# RETURN their product.
#
# Store the result of:
# multiply_numbers(6, 7)
#
# inside:
# multiplication_result
#
# Print multiplication_result.


# TASK 42:
# Create a function named:
#
def larger_number(a, b):
  if b > a:
    return b
  elif a > b:
    return a
  else:
    return a or b

bigger = larger_number(15, 40)
print(bigger)

#
# Give it TWO parameters:
#
# a
# b
#
# RETURN the larger value.
#
# If they are equal, RETURN that value.
#
# Store the result of:
# larger_number(15, 40)
#
# inside:
# bigger
#
# Print bigger.


# TASK 43:
# Create a function named:
#
def highest_of_three(a, b, c):
  if a > b and a > c:
    return a
  elif b > c and b > a:
    return b
  else:
    return c
highest_result = highest_of_three(18, 42, 27)
print(highest_result)
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), RETURN the highest value.
#
# Store:
# highest_of_three(18, 42, 27)
#
# inside:
# highest_result
#
# Print highest_result.


# TASK 44:
# Create a function named:
#
def lowest_of_three(a, b, c):
  if a < b and a < c:
    return a
  elif b < a and b < c:
    return b
  else:
    return c
lowest_result = lowest_of_three(a, b, c)
print(lowest_result)

#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), RETURN the lowest value.
#
# Test it at least THREE times.


# TASK 45:
# Create a function named:
#
def middle_of_three(a, b, c):
  if a > b < c:
    return b
  elif b > a < c:
    return a
  elif a > c < b:
    return c
middle_result = middle_of_three(10, 30, 20)
print(middle_result)
#
# Give it THREE parameters:
#
# a
# b
# c
#
# RETURN the middle value.
#
# Do NOT use min(), max(), or sorting.
#
# Test:
# middle_of_three(10, 30, 20)
# middle_of_three(50, 5, 25)
# middle_of_three(8, 7, 9)


# ============================================================
# SECTION 9 — RETURN + REUSE
# ============================================================

# TASK 46:
# Create a function named:
#
def get_highest(a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c
def get_lowest(a, b, c):
  if a < b and a < c:
    return a
  elif b < a and b < c:
    return b
  else: 
    return c

highest = get_highest(40, 50, 90)
lowest = get_lowest(30, 20, 10)
print(highest - lowest)
#
# Give it THREE parameters and RETURN the highest number.
#
# Then create another function named:
#
# get_lowest
#
# Give it THREE parameters and RETURN the lowest number.
#
# Use:
#
# a = 30
# b = 10
# c = 20
#
# Store the returned values in:
#
# highest
# lowest
#
# Then calculate:
#
# difference
#
# by subtracting lowest from highest.
#
# Print difference.
#
# IMPORTANT:
# Do NOT repeat the highest/lowest logic outside the functions.


# TASK 47:
# Create:
#
a = 9
b = 4
c = 1
#
# Use your get_highest() and get_lowest() functions from above.
#
# Store both returned values.
#
# Then determine if the difference between highest and lowest
# is greater than 10.
#
# Print:
# Large spread
#
# or:
# Small spread
def get_highest(a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c

def get_lowest(a, b, c):
  if a < b and a < c:
    return a
  elif b < a and b < c:
    return b
  else: 
    return c

highest_get = get_highest(a, b, c)
lowest_get = get_lowest(a, b, c)

spread_number = highest_get - lowest_get

def spread_value(spread_number):
  if spread_number > 10:
    print("Large Spread")
  else:
    print("Small Spread")

spread_value(spread_number)

# TASK 48:
# Create a function named:
#
# best_of_two
#
# Give it TWO parameters and RETURN the larger value.
#
# Then use it to determine the highest of THREE numbers
# WITHOUT writing a new three-number comparison.
#
# You should call best_of_two() more than once.
#
# Use:
a = 12
b = 1
c = 31
#
# Store the final answer in:
#
# highest
#
# Print highest.
#
# THINK:
# How can one function call feed into another?

# def best_of_two(value1, value2):
#   if value1 > value2:
#     if a < value1 and b > value1 and c < value1:
#       return b
#     elif a > value1 and b < value1 and c < value1:
#       return a
#     else:
#       return c
#   elif value1 < value2:
#     if a < value2 and b > value2 and c < value1:
#       return b
#     elif a > value2 and b < value2 and c < value2:
#       return a
#     else:
#       return c

def best_of_two(a, b):
  if a < b:
    return b
  else: 
    return a

highest1 = best_of_two(12, 1)
highest1 = best_of_two(highest1, 31)
print(highest1)

# TASK 49:
# Create a function named:
#
# worst_of_two
#
# Give it TWO parameters and RETURN the smaller value.
#
# Use it more than once to find the LOWEST of:
#
# a = 22
# b = 5
# c = 17
#
# Store the final result in:
#
# lowest
#
# Print lowest.
def worst_of_two(value1, value2):
  if value1 < value2:
    return value1
  else:
    return value2

lowest1 = worst_of_two(22, 5)
lowest1 = worst_of_two(lowest1, 17)
print(lowest1)

# ============================================================
# SECTION 10 — LOGIC CHALLENGES
# ============================================================

# TASK 50:
# Create:
#
# a = 12
# b = 7
# c = 19
#
# Determine whether b is the MIDDLE value.
#
# Print:
# b is middle
#
# or:
# b is not middle
#
# Do NOT calculate the middle value separately first.
def middle_value(a, b, c):
  if c > b > a:
    print("b is middle")
  else:
    print("b is not middle")

value_middle = middle_value(12, 7, 19)

# TASK 51:
# Create:
#
# a = 25
# b = 25
# c = 10
#
# Determine whether the HIGHEST value appears more than once.
#
# Print:
# Highest is tied
#
# or:
# Highest is unique
def high_unique(a, b, c):
  if a > b and a > c:
    print("Highest is unique")
  elif c > b and c > a:
    print("Highest is unique")
  elif b > a and b > c:
    print("Highest is unique")
  elif a == b and a > c:
    print("Highest is tied")
  elif a == c and a > b:
    print("Highest is tied")
  elif b == c and b > a:
    print("Highest is tied")
  else:
    print("Highest is tied")

unique_high = high_unique(25, 25, 10)

# TASK 52:
# Create:
#
a = 3
b = 8
c = 5
#
# Determine whether the numbers are:
#
# Strictly increasing
# Strictly decreasing
# Neither
#
# Print ONE result.
def direction_moving(a, b, c):
  if a < b < c:
    print("Strictly increasing")
  elif a > b > c:
    print("Strictly decreasing")
  else:
    return("Neither")

moving_direction = direction_moving(a, b, c)

# TASK 53:
# Create:
#
a = 5
b = 5
c = 10
#
# Determine whether the values are in NON-DECREASING order.
#
# This means each value may stay the same or get larger.
#
# Examples:
# 3, 3, 7 -> yes
# 3, 7, 7 -> yes
# 3, 7, 2 -> no
#
# Print:
# Non-decreasing
# OR
# Not non-decreasing
def decreasing_numbers(a, b, c):
  if a < b < c:
    print("Non-decreasing")
  else:
    print("Not non-decreasing")

numbers_decreasing = decreasing_numbers(a, b, c)

# TASK 54:
# Create:
#
age = 17
has_permission = True
has_ticket = False
#
# A person may enter if:
#
# - they are 18 or older
#
# OR
#
# - they are under 18 AND have_permission is True AND have_ticket is True
#
# Print:
# Entry allowed
#
# or:
# Entry denied
#
# Read this one carefully.

def ticket_access(age, has_permission, has_ticket):
  if age >= 18 or (age < 18 and has_permission and has_ticket):
    print("Entry allowed")
  else:
    print("Entry denied")

access_ticket = ticket_access(age, has_permission, has_ticket)

# TASK 55:
# Create:
#
score = 88
attendance = 92
#
# Print:
# Honors
#
# if score is at least 90 AND attendance is at least 90.
#
# Print:
# Pass
#
# if score is at least 70 AND attendance is at least 75,
# but the student did not qualify for Honors.
#
# Otherwise print:
# Fail
#
# Only ONE message should print.

def score_attendance(score, attendance):
  if score >= 90 and attendance >= 90:
    print("Honors")
  elif score >= 70 and attendance >= 75:
    print("Pass")
  else:
    print("Fail")

attendance_score = score_attendance(score, attendance)
# ============================================================
# SECTION 11 — DEBUGGING CHALLENGES
# ============================================================

# TASK 56:
# The programmer wants exactly ONE result.
#
# Fix the code so score = 95 prints ONLY:
#
# Excellent
#
score = 95
#
if score <= 70:
  print("Passing")
if score >= 90:
  print("Excellent")

# TASK 57:
# The programmer wants 18 to count as Adult.
#
# Fix the logic.
#
age = 18
#
if age >= 18:
  print("Adult")
else:
  print("Minor")


# TASK 58:
# The programmer wants numbers from 10 through 20,
# INCLUDING 10 and 20, to print:
#
# Valid
#
# Fix the condition.
#
number = 20
#
if number >= 10 and number <= 20:
  print("Valid")
else:
  print("Invalid")


# TASK 59:
# The programmer wants the function to RETURN the answer.
#
# Fix it.
#
def add_numbers(a, b):
  total = a + b
  return total

result = add_numbers(4, 6)
print(result)


# TASK 60:
# Fix the function so the variable result works outside
# of the function.
#
def subtract(a, b):
  answer = a - b
  return answer

result = subtract(20, 8)
print(result)


# ============================================================
# FINAL BOSS 1 — THREE NUMBER ANALYZER
# ============================================================

# TASK 61:
# Create a function named:
#
# analyze_three_numbers
#
# Give it THREE parameters:
#
# a
# b
# c
#
# It must:
#
# 1. Determine the highest value.
# 2. Determine the lowest value.
# 3. Determine the middle value.
# 4. Determine whether all three are equal.
# 5. Determine whether exactly two are equal.
#
# Print:
#
# Highest: [value]
# Lowest: [value]
# Middle: [value]
#
# Then print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Test:
# analyze_three_numbers(8, 3, 15)
# analyze_three_numbers(20, 20, 20)
# analyze_three_numbers(5, 5, 9)
# analyze_three_numbers(-5, 0, -12)

def analyze_three_numbers(a, b, c):
    # Highest
    if a >= b and a >= c:
        highest = a
    elif b >= a and b >= c:
        highest = b
    else:
        highest = c

    # Lowest
    if a <= b and a <= c:
        lowest = a
    elif b <= a and b <= c:
        lowest = b
    else:
        lowest = c

    # Middle
    if (b <= a <= c) or (c <= a <= b):
        middle = a
    elif (a <= b <= c) or (c <= b <= a):
        middle = b
    else:
        middle = c

    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Middle:", middle)

    if a == b == c:
        print("All equal")
    elif a == b or a == c or b == c:
        print("Exactly two equal")
    else:
        print("All different")

analyze_three_numbers(8, 3, 15)
analyze_three_numbers(20, 20, 20)
analyze_three_numbers(5, 5, 9)
analyze_three_numbers(-5, 0, -12)



# ============================================================
# FINAL BOSS 2 — NUMBER RANKING
# ============================================================

# TASK 62:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
user_num1 = input("Give me a whole number: ")
user_num2 = input("Give me a whole number: ")
user_num3 = input("Give me a whole number: ")
#
# Print the numbers from LOWEST to HIGHEST.
#
# Example:
# User enters:
# 30
# 10
# 20
#
# Output:
# 10
# 20
# 30
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your program must still work if the order of inputs changes.
if user_num1 <= user_num2 and user_num1 <= user_num3:
    lowest = user_num1
    if user_num2 <= user_num3:
        middle, highest = user_num2, user_num3
    else:
        middle, highest = user_num3, user_num2
elif user_num2 <= user_num1 and user_num2 <= user_num3:
    lowest = user_num2
    if user_num1 <= user_num3:
        middle, highest = user_num1, user_num3
    else:
        middle, highest = user_num3, user_num1
else:
    lowest = user_num3
    if user_num1 <= user_num2:
        middle, highest = user_num1, user_num2
    else:
        middle, highest = user_num2, user_num1

print(lowest)
print(middle)
print(highest)


# ============================================================
# FINAL BOSS 3 — FUNCTION REUSE
# ============================================================

# TASK 63:
# Create these THREE functions:
#
# get_highest(a, b, c)
# get_lowest(a, b, c)
# get_middle(a, b, c)
#
# Each function must RETURN the correct value.
#
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# first
# second
# third
#
# Call all three functions.
#
# Store the returned results in:
#
# highest
# lowest
# middle
#
# Then print:
#
# Highest: [highest]
# Middle: [middle]
# Lowest: [lowest]
#
# Do NOT use min(), max(), or sorting.
first = int(input("Enter first: "))
second = int(input("Enter second: "))
third = int(input("Enter third: "))

def get_highest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def get_lowest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

def get_middle(a, b, c):
    if (b <= a <= c) or (c <= a <= b):
        return a
    elif (a <= b <= c) or (c <= b <= a):
        return b
    else:
        return c

highest = get_highest(first, second, third)
lowest = get_lowest(first, second, third)
middle = get_middle(first, second, third)

print("Highest:", highest)
print("Middle:", middle)
print("Lowest:", lowest)


# ============================================================
# FINAL BOSS 4 — CONDITIONAL DECISION SYSTEM
# ============================================================

# TASK 64:
# Create a function named:
#
# admission_decision
#
# Give it THREE parameters:
#
# grade
# attendance
# interview
#
# Rules:
#
# - If grade is 90 or higher AND attendance is 90 or higher,
#   print "Accepted"
#
# - Otherwise, if grade is 80 or higher AND attendance is 80 or higher
#   AND interview is "pass", print "Accepted"
#
# - Otherwise print "Not accepted"
#
# Test:
#
# admission_decision(95, 95, "fail")
# admission_decision(85, 85, "pass")
# admission_decision(85, 85, "fail")
# admission_decision(75, 100, "pass")
#
# THINK:
# The first person should still be accepted even though
# the interview value is "fail".
def admission_decision(grade, attendance, interview):
    if grade >= 90 and attendance >= 90:
        print("Accepted")
    elif grade >= 80 and attendance >= 80 and interview == "pass":
        print("Accepted")
    else:
        print("Not accepted")

admission_decision(95, 95, "fail")
admission_decision(85, 85, "pass")
admission_decision(85, 85, "fail")
admission_decision(75, 100, "pass")


# ============================================================
# FINAL BOSS 5 — THINK CAREFULLY
# ============================================================

# TASK 65:
# Create:
#
a = 15
b = 8
c = 15
#
# Your program must determine BOTH:
#
# 1. The highest value
# 2. Whether that highest value is unique or tied
#
# Print:
#
# Highest: [value]
#
# Then print ONE of:
#
# Unique highest
# Tied highest
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your logic should still work if the variable values change.

if a >= b and a >= c:
    highest = a
elif b >= a and b >= c:
    highest = b
else:
    highest = c

print("Highest:", highest)

count = 0
if a == highest:
    count += 1
if b == highest:
    count += 1
if c == highest:
    count += 1

if count > 1:
    print("Tied highest")
else:
    print("Unique highest")



# ============================================================
# SECTION 12 — LEETCODE-STYLE REAL PROBLEM CHALLENGES
# ============================================================
#
# These problems are intentionally DIFFERENT from the earlier tasks.
# Instead of simply asking you to find the highest number, check a range,
# or assign a grade, each problem gives you a small situation to solve.
#
# RULES:
# - Use the EXACT function name and parameters given.
# - Do NOT use input() unless the problem specifically tells you to.
# - RETURN the answer unless the problem specifically tells you to print.
# - Your function must work for ALL valid test cases.
# - Do NOT hard-code the example answers.
# - Use only concepts covered in class.
# - Test every example after writing your function.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 66 — TEMPERATURE CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
# convert_temperature
#
# Parameters:
#
# temperature
# scale
#
# The scale will be either:
#
# "C"
# or
# "F"
#
# If scale is "C", the temperature given is Celsius.
# Convert it to Fahrenheit using:
#
# Fahrenheit = Celsius * 1.8 + 32
#
# If scale is "F", the temperature given is Fahrenheit.
# Convert it to Celsius using:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# RETURN the converted temperature.
#
# Examples:
#
# convert_temperature(0, "C")      -> 32
# convert_temperature(100, "C")    -> 212
# convert_temperature(32, "F")     -> 0
# convert_temperature(68, "F")     -> 20
#
# CHALLENGE:
# The same function must be able to convert in BOTH directions.

def convert_temperature(temperature, scale):
  if scale == "C":
    return temperature * 1.8 + 32
  elif scale == "F":
    return (temperature - 32) / 1.8

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 67 — KELVIN CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
# to_kelvin
#
# Parameters:
#
# temperature
# scale
#
# If scale is "C":
#
# Kelvin = Celsius + 273.15
#
# If scale is "F":
#
# First convert Fahrenheit to Celsius:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# Then convert Celsius to Kelvin.
#
# RETURN the Kelvin temperature.
#
# Examples:
#
# to_kelvin(0, "C")     -> 273.15
# to_kelvin(100, "C")   -> 373.15
# to_kelvin(32, "F")    -> 273.15
# to_kelvin(212, "F")   -> 373.15
#
# THINK:
# One input can require TWO calculations before you return the answer.

def to_kelvin(temperature, scale):
  if scale == "C":
    return temperature + 273.15
  elif scale == "F":
    celsius = (temperature - 32) / 1.8
    return celsius + 273.15


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 68 — PARKING GARAGE
# ------------------------------------------------------------
#
# Write a function named:
#
# parking_cost
#
# Parameter:
#
# hours
#
# Parking costs:
#
# First hour: $5
# Each additional hour: $3
#
# If the car is parked for more than 8 hours,
# the maximum daily charge is $25.
#
# RETURN the total parking cost.
#
# Examples:
#
# parking_cost(1)   -> 5
# parking_cost(2)   -> 8
# parking_cost(5)   -> 17
# parking_cost(9)   -> 25
# parking_cost(20)  -> 25
#
# THINK:
# Do not accidentally charge $3 for the first hour.
def parking_cost(hours):
  if hours <= 0:
    return 0
  cost = 5 + (hours - 1) * 3
  if cost > 25:
    return 25
  return cost

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 69 — MOVIE TICKET TOTAL
# ------------------------------------------------------------
#
# Write a function named:
#
# movie_total
#
# Parameters:
#
# age
# is_weekend
#
# Ticket prices:
#
# Under 13: $8
# Ages 13–64: $12
# Age 65+: $7
#
# On weekends, add $3 to the ticket price.
#
# RETURN the final ticket price.
#
# Examples:
#
# movie_total(10, False)  -> 8
# movie_total(10, True)   -> 11
# movie_total(30, False)  -> 12
# movie_total(70, True)   -> 10
#
# THINK:
# First determine the base ticket price.
# Then decide whether something must be added.

def movie_total(age, is_weekend):
  if age < 13:
    price = 8
  elif age <= 64:
    price = 12
  else:
    price = 7
        
  if is_weekend:
    price += 3
    return price


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 70 — ELECTRIC BILL
# ------------------------------------------------------------
#
# Write a function named:
#
# electric_bill
#
# Parameter:
#
# usage
#
# The bill is calculated using these rules:
#
# 0–100 units:
# $0.10 per unit
#
# More than 100 units:
# The first 100 units cost $0.10 each.
# Every unit AFTER 100 costs $0.20 each.
#
# RETURN the total bill.
#
# Examples:
#
# electric_bill(50)   -> 5.0
# electric_bill(100)  -> 10.0
# electric_bill(120)  -> 14.0
# electric_bill(200)  -> 30.0
#
# IMPORTANT:
# For 120 units, only 20 units should be charged at $0.20.

def electric_bill(usage):
  if usage <= 100:
    return usage * 0.10
  else:
    return (100 * 0.10) + ((usage - 100) * 0.20)

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 71 — LEAP YEAR
# ------------------------------------------------------------
#
# Write a function named:
#
# is_leap_year
#
# Parameter:
#
# year
#
# A year is a leap year if:
#
# - it is divisible by 400
#
# OR
#
# - it is divisible by 4 BUT NOT divisible by 100
#
# RETURN True if it is a leap year.
# Otherwise RETURN False.
#
# Examples:
#
# is_leap_year(2024)  -> True
# is_leap_year(2025)  -> False
# is_leap_year(1900)  -> False
# is_leap_year(2000)  -> True
#
# This problem is intentionally tricky.
#
# THINK:
# A year divisible by 100 is NOT automatically a leap year.

def is_leap_year(year):
  if year % 400 == 0:
    return True
  if year % 100 == 0:
    return False
  if year % 4 == 0:
    return True
  return False


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 72 — TRIANGLE VALIDITY
# ------------------------------------------------------------
#
# Write a function named:
#
# valid_triangle
#
# Parameters:
#
# a
# b
# c
#
# Three side lengths can form a triangle only if:
#
# a + b > c
# a + c > b
# b + c > a
#
# ALL THREE conditions must be true.
#
# RETURN True if the sides can form a triangle.
# Otherwise RETURN False.
#
# Examples:
#
# valid_triangle(3, 4, 5)   -> True
# valid_triangle(5, 5, 5)   -> True
# valid_triangle(1, 2, 10)  -> False
# valid_triangle(2, 3, 5)   -> False
#
# Notice that 2 + 3 = 5 is NOT enough.
# It must be GREATER THAN.

def valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 73 — TRIANGLE TYPE
# ------------------------------------------------------------
#
# Write a function named:
#
# triangle_type
#
# Parameters:
#
# a
# b
# c
#
# First, determine whether the three sides form a valid triangle.
#
# If they do NOT, RETURN:
#
# "invalid"
#
# If all three sides are equal, RETURN:
#
# "equilateral"
#
# If exactly two sides are equal, RETURN:
#
# "isosceles"
#
# Otherwise RETURN:
#
# "scalene"
#
# Examples:
#
# triangle_type(3, 3, 3)   -> "equilateral"
# triangle_type(5, 5, 8)   -> "isosceles"
# triangle_type(3, 4, 5)   -> "scalene"
# triangle_type(1, 2, 10)  -> "invalid"
#
# THINK:
# Check whether the triangle is valid BEFORE classifying it.
def triangle_type(a, b, c):
  if not (a + b > c and a + c > b and b + c > a):
    return "invalid"
  if a == b == c:
    return "equilateral"
  elif a == b or a == c or b == c:
    return "isosceles"
  else:
    return "scalene"

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 74 — ROCK PAPER SCISSORS
# ------------------------------------------------------------
#
# Write a function named:
#
# rps_winner
#
# Parameters:
#
# player1
# player2
#
# Each argument will be:
#
# "rock"
# "paper"
# or
# "scissors"
#
# RETURN:
#
# "tie"
#
# if both players choose the same thing.
#
# RETURN:
#
# "player1"
#
# if player 1 wins.
#
# RETURN:
#
# "player2"
#
# if player 2 wins.
#
# Rules:
#
# rock beats scissors
# scissors beats paper
# paper beats rock
#
# Examples:
#
# rps_winner("rock", "scissors")  -> "player1"
# rps_winner("paper", "rock")     -> "player1"
# rps_winner("rock", "paper")     -> "player2"
# rps_winner("paper", "paper")    -> "tie"
#
# This is a logic problem.
# There are several possible combinations.

def rps_winner(player1, player2):
  if player1 == player2:
    return "tie"
  elif (player1 == "rock" and player2 == "scissors") or \
    (player1 == "scissors" and player2 == "paper") or \
      (player1 == "paper" and player2 == "rock"):
    return "player1"
  else:
    return "player2"


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 75 — CLOSEST TO 100
# ------------------------------------------------------------
#
# Write a function named:
#
# closest_to_100
#
# Parameters:
#
# a
# b
#
# RETURN whichever number is closer to 100.
#
# If they are equally far away from 100, RETURN:
#
# -1
#
# Examples:
#
# closest_to_100(90, 80)    -> 90
# closest_to_100(105, 120)  -> 105
# closest_to_100(90, 110)   -> -1
#
# RESTRICTION:
# Do NOT use abs().
#
# THINK:
# A number may be above OR below 100.
# You will need to determine each number's distance from 100.

def closest_to_100(a, b):
  dist_a = a - 100 if a >= 100 else 100 - a
  dist_b = b - 100 if b >= 100 else 100 - b 
  if dist_a < dist_b:
    return a
  elif dist_b < dist_a:
    return b
  else:
    return -1

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 76 — DELIVERY FEE
# ------------------------------------------------------------
#
# Write a function named:
#
# delivery_fee
#
# Parameters:
#
# order_total
# distance
#
# Rules:
#
# If order_total is $50 or more AND distance is 5 miles or less:
# RETURN 0
#
# Otherwise, if distance is 5 miles or less:
# RETURN 5
#
# Otherwise:
# RETURN 10
#
# Examples:
#
# delivery_fee(60, 3)  -> 0
# delivery_fee(30, 3)  -> 5
# delivery_fee(60, 8)  -> 10
# delivery_fee(30, 8)  -> 10
#
# THINK:
# A large order does NOT always mean free delivery.

def delivery_fee(order_total, distance):
  if order_total >= 50 and distance <= 5:
    return 0
  elif distance <= 5:
    return 5
  else:
    return 10


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 77 — ATM WITHDRAWAL
# ------------------------------------------------------------
#
# Write a function named:
#
# can_withdraw
#
# Parameters:
#
# balance
# amount
#
# A withdrawal is allowed only if:
#
# - amount is greater than 0
# - amount is less than or equal to balance
# - amount is divisible by 20
#
# RETURN True if the withdrawal is allowed.
# Otherwise RETURN False.
#
# Examples:
#
# can_withdraw(500, 100)  -> True
# can_withdraw(500, 125)  -> False
# can_withdraw(50, 100)   -> False
# can_withdraw(500, 0)    -> False
#
# ALL conditions must be true.
def can_withdraw(balance, amount):
  return (amount > 0) and (amount <= balance) and (amount % 20 == 0)


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 78 — RESTAURANT TIP
# ------------------------------------------------------------
#
# Write a function named:
#
# tip_amount
#
# Parameters:
#
# bill
# service
#
# service will be:
#
# "poor"
# "good"
# or
# "excellent"
#
# Tip rules:
#
# poor       -> 10%
# good       -> 18%
# excellent  -> 25%
#
# RETURN the tip amount.
#
# Examples:
#
# tip_amount(100, "poor")       -> 10
# tip_amount(100, "good")       -> 18
# tip_amount(100, "excellent")  -> 25
# tip_amount(80, "good")        -> 14.4
#
# THINK:
# RETURN only the TIP, not the final bill.

def tip_amount(bill, service):
  if service == "poor":
    return bill * 0.10
  elif service == "good":
    return bill * 0.18
  elif service == "excellent":
    return bill * 0.25

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 79 — PHONE BATTERY WARNING
# ------------------------------------------------------------
#
# Write a function named:
#
# battery_status
#
# Parameters:
#
# battery
# is_charging
#
# RETURN:
#
# "critical"
# if battery is 5 or lower AND it is NOT charging
#
# "low"
# if battery is 20 or lower AND it is NOT charging
#
# "charging"
# if is_charging is True
#
# "normal"
# otherwise
#
# Examples:
#
# battery_status(3, False)   -> "critical"
# battery_status(15, False)  -> "low"
# battery_status(3, True)    -> "charging"
# battery_status(80, False)  -> "normal"
#
# THINK:
# The order of the conditions matters.
def battery_status(battery, is_charging):
  if is_charging:
    return "charging"
  elif battery <= 5:
    return "critical"
  elif battery <= 20:
    return "low"
  else:
    return "normal"

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 80 — TAXI FARE
# ------------------------------------------------------------
#
# Write a function named:
#
# taxi_fare
#
# Parameters:
#
# miles
# is_night
#
# Fare rules:
#
# Base fare: $4
# Each mile: $2
#
# If is_night is True, add a $5 night fee.
#
# RETURN the total fare.
#
# Examples:
#
# taxi_fare(0, False)  -> 4
# taxi_fare(5, False)  -> 14
# taxi_fare(5, True)   -> 19
#
# Build the final answer from the rules instead of
# hard-coding different totals.

def taxi_fare(miles, is_night):
  fare = 4 + (miles * 2)
  if is_night:
    fare += 5
    return fare

# ------------------------------------------------------------
# LEETCODE-STYLE TASK 81 — GAME DAMAGE
# ------------------------------------------------------------
#
# Write a function named:
#
# calculate_damage
#
# Parameters:
#
# attack
# defense
# critical
#
# First calculate:
#
# damage = attack - defense
#
# If damage would be less than 0, damage becomes 0.
#
# If critical is True, DOUBLE the damage.
#
# RETURN the final damage.
#
# Examples:
#
# calculate_damage(20, 5, False)  -> 15
# calculate_damage(20, 5, True)   -> 30
# calculate_damage(5, 20, False)  -> 0
# calculate_damage(5, 20, True)   -> 0
#
# THINK:
# The critical hit should happen AFTER defense is removed.

def calculate_damage(attack, defense, critical):
  damage = attack - defense
  if damage < 0:
    damage = 0
  if critical:
    damage *= 2
    return damage


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 82 — STORE COUPON
# ------------------------------------------------------------
#
# Write a function named:
#
# final_price
#
# Parameters:
#
# price
# coupon
#
# coupon will be:
#
# "none"
# "SAVE10"
# "SAVE25"
#
# Rules:
#
# "none"   -> no discount
# "SAVE10" -> 10% off
# "SAVE25" -> 25% off
#
# RETURN the FINAL price after the discount.
#
# Examples:
#
# final_price(100, "none")    -> 100
# final_price(100, "SAVE10")  -> 90
# final_price(100, "SAVE25")  -> 75
# final_price(80, "SAVE25")   -> 60
#
# THINK:
# A 25% discount means the customer pays 75% of the price.
def final_price(price, coupon):
  if coupon == "SAVE10":
    return price == 100 * 0.10
  elif coupon == "SAVE25":
    return price == 100 * 0.25
  elif coupon == "none":
    return price == 100
  print("No discount")
 

# ============================================================
# GIT CHECK
# ============================================================

# When you are completely finished:
#
# 1. Save your file.
# 2. Run your ENTIRE program.
# 3. Fix all errors.
# 4. Make sure you can explain your code.
#
# Then use:
#
# git status
# git add .
# git commit -m "Complete conditionals and functions challenge"
# git push
