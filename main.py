import activities
import random
print("-----------------------------------REDWOOD CITY-------------------------------------")
print("")
num = int(input("Press 1 to continue : "))
if num == 1:
    age = 0;
    skill = random.randint(0,99)
if age<5:
        while True:

            print("Your age :", age)
            print("Press 1 to cry")
            print("Press 2 to play")
            print("Press 3 to do both")
            print("Press 4 to grow older")
            reg = int(input("Enter your choice : "))
            if reg == 1:
                print("You cried")
                skill = skill + 0.5
            if reg == 2:
                print("You played")
                skill = skill + 1
            if reg == 3:
                print("You cried and played.")
                skill == skill + 1.5
            if reg == 4:
                age=age+1
            if(age>4):
                break
if age>=5 and age<18:

    while True:
        print(age)
        age = age + 1
        if (age > 13):
            break

