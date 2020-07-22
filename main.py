import random #We have to import this module for generating random numbers

print("-----------------------------------REDWOOD CITY-------------------------------------")
print("")
num = int(input("Press 1 to continue : "))          #a condition to begin the game

if num == 1:
    age = 0;
    name =  input("Enter your name : ")
    print("Choose your gender : ")
    print("Press 1 for male")
    print("Press 2 for female")
    print("Press 3 for other")
    gender = int(input("Enter your choice")) #accepting an integer for a condition

    if gender == 1:
        sex = "Male"
    elif gender == 2:
        sex = "Female"
    elif gender == 3:
        sex = "Other"

    skill = random.randint(0,99)            #The random.randint() function generates a random number
    happiness = random.randint(0,99)
    intelligence = random.randint(0,99)
    attractiveness = random.randint(0,99)
    skill = 99

    if skill>= 100:
        skill =100

if age<5:                                       #main process when the age is lesser than i
        while True:
            skill = skill-1
            if skill>=100:
                skill=100

            happiness = happiness-1
            if happiness>=100:
                happiness=100

            intelligence = intelligence-1
            if intelligence>=100:
                intelligence=100

            attractiveness = attractiveness-1
            if attractiveness>=100:
                attractiveness=100

            print("Name : ", name)
            print("Sex : ", sex)
            print("You're skill(s) : ",skill)
            print("You're happiness : ",happiness)
            print("You're intelligence : ",intelligence)
            print("You're attractiveness : ",attractiveness)
            print("Your age :", age)
            print("Press 1 to cry")
            print("Press 2 to play")
            print("Press 3 to do both")
            print("Press 4 to grow older")
            reg = int(input("Enter your choice : "))
            print("")

            if reg == 1:
                print("You cried")
                skill = skill + 0.5
                happiness =  happiness -1
                print("")

            if reg == 2:
                print("You played")
                skill = skill + 1
                happiness = happiness +5
                intelligence = intelligence +1
                print("")

            if reg == 3:
                print("You cried and played.")
                skill = skill + 1
                happiness = happiness +0
                intelligence = intelligence +1
                print ("")

            if reg == 4:
                age=age+1
            if(age>4):
                break

if age>=5 and age<18:       #This process is needed when the age is between 4 and 19
    while True:
        skill = skill - 2
        if skill >= 100:
            skill = 100

        happiness = happiness - 1
        if happiness >= 100:
            happiness = 100

        intelligence = intelligence - 1
        if intelligence >= 100:
            intelligence = 100

        attractiveness = attractiveness - 1
        if attractiveness >= 100:
            attractiveness = 100

        print("Name : ", name)
        print("Sex : ", sex)
        print("You're skill(s) : ", skill)
        print("Your age :", age)
        print("Press 1 for school")
        print("Press 2 for activities")
        print("Press 3 for crimes ")
        print("Press 4 to grow older")
        reg = int(input("Enter your choice : "))
        print("")

        if reg == 1:
            print("")
            print("Press 1 for doing homework")
            print("Press 2 for spendinng time with friends")
            print("Press 3 for skipping class ")
            print("Press 4 for interacting with teachers")
            print("Press 5 for joining clubs")
            print("Press 6 to study harder")
            choice = int(input("Enter your choice : "))

            if choice == 1:
                print("You did your homework")
                skill = skill + 2
                intelligence = intelligence +1
                print("")

            if choice == 2:
                rand = random.randint(0,20)
                if rand >= 0 and rand<= 2:
                    print("You have no friends")
                    happiness = happiness -10
                    print("happiness has decreased by 10 points")
                    print("")

                elif rand>=3 and rand<=8:
                    print ("You went out with your friends but you didn't enjoy the experience")
                    happiness = happiness + 0
                    print("happiness reamins the same")
                    print("")

                elif rand>=9 and rand<=14:
                    print ("You went out with your friends and you had a pretty good time")
                    happiness = happiness + 5
                    print("happiness has increased by 5 points")
                    print("")

                else :
                    print ("You went out with your friends and you had a really good time")
                    happiness = happiness + 10
                    print("happiness has increased by 10 points")
                    print("")

            if choice == 3:
                rand = random.randint(0,10)
                if rand >=0 and rand<=4:
                    print("You tried to skip school but you were caught by a teacher")
                    print("The teacher decides to give you a detention")

                    print("")
                print("")

        if reg == 2:
            print("You played")
            skill = skill + 1
        if reg == 3:
            print("You cried and played.")
            skill == skill + 1.5
        if reg == 4:
            age = age + 1
        if (age > 4):
            break

