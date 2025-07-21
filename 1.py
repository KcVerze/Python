# python practice

def say_hello():
    print("hey")

say_hello()

print("hello world")

#basic operation

num1= input("enter a number: ")
num2= input("enter another: ")

sum = int(num1) + int(num2)
print("the sum is:", sum)

# decision making

age = int (input("How old are you:"))

if age >= 18:
    print("you're an adult. ")
else:
    print("small boy")


score = int( input("Student math score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#example

name =input("what's your name ?")
print("My name is" + " " + name + "!")

# band name generator

print("Welcome to the band name generator.")

city = input("What's the name of the city you grew up in? ")

pet_name = input("What's your pet name? ")
print("your band name could be : "+city+" "+pet_name)


# tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
final_bill = (bill+(bill*(tip/100)))/people
bill_roundup = (round(final_bill,2))
print(f"${bill_roundup}")

# odd or even

num = int(input("pick a number"))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# roller coaster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

