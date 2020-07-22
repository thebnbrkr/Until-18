import random #We have to import this module for generating random numbers

print("-----------------------------------REDWOOD CITY-------------------------------------")
print("")
num = int(input("Press 1 to continue : "))          #a condition to begin the game

if num == 1:
    age = 0;
    status = 1;                                     '''Status = 1 - Free person 
                                                       Status = 2 - Is currently in prison
                                                       Status = 3 - Is currently in juvie
                                                       Status = 4 - Is on the run
                                                       Status = 5 - Had been to juvie
                                                       Status = 6 - Had been to prison'''
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
    naughty = 0                             #for measuring naughtiness
    club = 0                                #by default 0 , when you join some club = some number
    clubskill=0                             #increases the talent, could potentially impact the future
    money = 0                               #counting the money in your bank account
    crime = 0                               #counting the total number of crimes
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

while status == 1:
    if age >= 5 and age < 18:  # This process is needed when the age is between 4 and 19
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
            print("Press 2 for part-time jobs")
            print("Press 3 for crimes ")
            print("Press 4 for relationships")
            print("Press 5 to grow older")
            reg = int(input("Enter your choice : "))
            print("")

            if reg == 1:                                        #school
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
                    intelligence = intelligence + 1
                    print("")

                if choice == 2:
                    rand = random.randint(0, 20)
                    if rand >= 0 and rand <= 2:
                        print("You have no friends")
                        happiness = happiness - 10
                        print("happiness has decreased by 10 points")
                        print("")

                    elif rand >= 3 and rand <= 8:
                        print("You went out with your friends but you didn't enjoy the experience")
                        happiness = happiness + 0
                        print("happiness reamins the same")
                        print("")

                    elif rand >= 9 and rand <= 14:
                        print("You went out with your friends and you had a pretty good time")
                        happiness = happiness + 5
                        print("happiness has increased by 5 points")
                        print("")

                    else:
                        print("You went out with your friends and you had a really good time")
                        happiness = happiness + 10
                        print("happiness has increased by 10 points")
                        print("")

                if choice == 3:
                    rand = random.randint(0, 10)
                    if rand >= 0 and rand <= 4:
                        print("You tried to skip school but you were caught by a teacher")
                        print("The teacher decides to give you a detention")
                        print("")

                if choice == 4:
                    print("Press 1 to make fun of the teacher")
                    print("Press 2 for asking doubts")
                    print("")
                    a = int(input("Enter your choice : "))
                    if a==1:
                        rand = random.randint(0, 100)
                        if rand>=8 and rand<=16:
                            if naughty>=50:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher complained to the principal and you were suspended for a week")
                                print("")
                                naughty =naughty+10
                                happiness = happiness-10
                                print("You're hapiness decreased by 10 units")
                            else:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher gave you a detention")
                                print("")
                                naughty =naughty+10
                                happiness = happiness-10
                                print("You're hapiness decreased by 10 units")
                                print("")
                        if rand>=0 and rand<=7:
                            if naughty>=50:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher complained to the principal and you were suspended for a week")
                                print("")
                                naughty =naughty+10
                                hapiness = hapiness-10
                                print("You're hapiness decreased by 10 units")
                            else:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher gave you a detention")
                                print("")
                                naughty =naughty+10
                                happiness = happiness-10
                                print("You're hapinness decreased by 10 units")
                                print("")
                        else:
                            print("Everone laughed at your jokes")
                            happiness = happiness+10
                            naughty = naughty + 5
                            print("You're hapinness has increased by 10 units ")

                if choice == 5:
                    if age>=14:
                        print("")
                        print("Press 1 for joining the BasketBall Club")
                        print("Press 2 for joining the Chess Club")
                        print("Press 3 for joining the Football Club")
                        print("Press 4 for joining the Book Club")
                        print("Press 5 for joining the Tennis Club")
                        print("Press 6 for joining the Drama Club")
                        print("Press 7 for joining the Environmental Club")
                        print("Press 8 for joining the Cultural Club")
                        reg = int(input("Enter your choice : "))
                        print("")

                        if click == 1:
                            if skill <= 20:
                                print("Sorry You do not have the skill to join this club")
                            else:
                                print("You have joined the BasketBall club")
                                club = 1
                                clubskill = clubskill + 10
                                club = click

                        if click == 2:
                            print("You have joined the Chess Club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click
                        if click == 3:
                            if skill <= 40:
                                print("Sorry you do not have the skill to join this club")
                            else:
                                print("You have joined the Football club")
                                club = 1
                                clubskill = clubskill + 10
                                club = click

                        if click == 4:
                            print("You have joined the book club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        if click == 5:
                            if skill <= 45:
                                print("Sorry you do not have the skill to join this club")
                            else:
                                print("You have joined the Tennis Club")
                                club = 1
                                clubskill = clubskill + 10
                                club=click

                        if click == 6:
                            print("You have joined the Drama Club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        if click == 7:
                            print("You have joined the Environmental Club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        if click == 8:
                            print("You have joined the Environmental Club`")
                            club = 1
                            clubskill = clubskill + 10
                            club = click


                    else:
                        print("You're not old enough to join clubs")

                if choice == 6:
                    print("You studied harder")
                    skill = skill+5
                    intelligence = intelligence+5

            if reg == 2:
                if age>=14:
                    print("The available part time jobs are : ")
                    print("Press 1 for hotdog maker")
                    print("Press 2 for server")
                    print("Press 3 for part-time janitor")
                    print("Press 4 for grocery store salesman")
                    print("Press 5 for hotdog maker")
                    print("Press 6 for internship at pow tech")
                    print("Press 7 for babysitter at babysitterinc corp")
                    print("")
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        if skill>=20:
                            print("You're hired !!!")
                            print("Salary $8 per hour")
                            money = (8*4)*5*50
                        else :
                            print("You need atleast 20 skill units for this job")

                    if choice == 2:
                        if skill>=30:
                            print("You're hired !!!")
                            print("Salary $9 per hour")
                            money = (9*4)*5*50
                        else:
                            print("You need atleast 30 skill units for this job")


                    if choice == 3:
                        if skill>=20:
                            print("You're hired !!!")
                            print("Salary $10 per hour")
                            money = (10*4)*5*50
                        else:
                            print("You need atleast 20 skill units for this job")

                    if choice == 4:
                        if skill>=30 and intelligence>=20:
                            print("You're hired !!!")
                            print("Salary $13 per hour")
                            money = (13 * 4) * 5 * 50
                        else:
                            print("You need atleast 30 skill units and 20 intelligence units for this job")

                    if choice == 5:
                        print("You're hired !!!")
                        print("Salary $10 per hour")
                        money = (10 * 4) * 5 * 50

                    if choice == 6:
                        if skill>=90 and intelligence>=70:
                            print("You're hired !!!")
                            print("Salary $50 per hour")
                            money = (50* 4) * 5 * 50
                        else:
                            print("You need atleast 80 skill units and 70 intelligence units for this job")

                    if choice == 7:
                        if skill>=70 and intelligence>=70:
                            print("You're hired !!!")
                            print("Salary $25 per hour")
                            money = (25 * 4) * 5 * 50
                        else:
                            print("You need atleast 70 skill units and 70 intelligence units for this job")

            if reg == 3:
                if age<=12:
                    print("Press 1 to burgle a home")
                    print("Press 2 to pickpocket")
                    print("Press 3 to behave behave deleqently")
                    print("Press 4 to shoplift")
                    print("")
                    choice=int(input("Enter your choice : "))
                    if choice ==1:
                        print("You were walking down the streets and have found your target house")
                        print("")
                        if crime <3:
                            rand = 0
                            if rand == 0:
                                rob = int(input("Press 2 to rob the house"))
                                if rob == 2:
                                    print("You have successfully robbed the house")
                                    rand = random.randint(1,9000)
                                    print("You sold all the stolen items to a pawn shop and recieved $",rand)
                                    money = money+rand
                                else:
                                    print("SOMEONE CALLED YOU BREAKING INTO THE HOUSE AND CALLED THE POLICE ON YOU !!!")
                                    print("You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                    rand = random.randint(1,10)
                                    if rand<6 and crime == 0:
                                        print("You're arrested for burlary and have to spent 10 months in jail !!!")
                                        crime = crime+1
                                    elif rand<6 and crime <= 3:
                                        print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                        crime = crime+1
                                    else:
                                        print("The lawyers have helped you to stay out of jail")
                                        print("You're free")
                else:
                    print("Press 1 to burgle a home")
                    print("Press 2 to pickpocket")
                    print("Press 3 to behave behave deleqently")
                    print("Press 4 to shoplift")
                    print("Press 5 to steal a car")
                    print("Press 6 to murder a person")
                    print("Press 7 to hire a hitman")
                    print("Press 8 to launch a cyber attack")
                    choice=int(input("Enter your choice : "))


            if reg == 4:
                age = age + 1
        if (age > 18):
            break

while status ==2:
    print("Jail")
    break