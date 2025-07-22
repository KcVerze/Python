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
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")



# Treasure island

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

decision1 = input("Direction -- left or right ?")
if decision1 == "left":
    decision2 = input("Decision -- Swim or Wait")
    if decision2 == "wait":
        decision3 = input("Which door?")
        if decision3 == "blue":
            print("Eaten by beasts. Game Over")
        elif decision3 == "yellow":
            print("You win")
        elif decision3 == "red":
            print("burned by fire. Game Over")
        else:
            print ("Game Over")
    else:
        print("Attacked by trout Game Over.")
else:
    print("Fall into a hole Game Over.")



# head or tails
import random


num = random.random()

print(num)

num_round = round(num)

print(num_round)

if num_round == 0:
    print("heads")
else:
    print("tails")




# rock paper scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
sel1 =int(input("rock = 0 , paper = 1, scissors = 2 , pick : "))
options = [rock,paper,scissors]
print(options[sel1])

print("computer chose:")
sel2 = random.randint(0,2)
print(options[sel2])

# win , lose ,draw

if sel1 >= 3 or sel1 < 0:
    print("You typed an invalid number. You lose!")
elif sel1 == 0 and sel2 == 2:
    print("You win!")
elif sel2 == 0 and sel1 == 2:
    print("You lose!")
elif sel2 > sel1:
    print("You lose!")
elif sel1 > sel2:
    print("You win!")
elif sel2 == sel1:
    print("It's a draw!")