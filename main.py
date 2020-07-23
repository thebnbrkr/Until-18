import random #We have to import this module for generating random numbers
import time

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

    naughty = 0                             #for measuring naughtiness
    club = 0                                #by default 0 , when you join some club = some number
    clubskill=0                             #increases the talent, could potentially impact the future
    money = 0                               #counting the money in your bank account
    crime = 0                               #counting the total number of crimes
    jailtime = 0                            #total nnumber of years spend in prison
    dead = 0                                #binary value; becomes 1 when you die
    if skill>= 100:
        skill =100

if age<5:                                       #main process when the age is lesser than i
        while True:
            skill = skill-1
            if skill>=100:
                skill=100
            elif skill>0:
                skill = 0

            happiness = happiness-1
            if happiness>=100:
                happiness=100
            elif happiness>0:
                happiness = 0

            intelligence = intelligence-1
            if intelligence>=100:
                intelligence=100
            elif intelligence>0:
                intelligence = 0


            print("Name : ", name)
            print("Sex : ", sex)
            print("You're skill(s) : ",skill)
            print("You're happiness : ",happiness)
            print("You're intelligence : ",intelligence)
            print("Your age :", age)
            print("Press 1 to cry")
            print("Press 2 to play")
            print("Press 3 to do both")
            print("Press 4 to grow older")
            reg = int(input("Enter your choice : "))
            print("")

            if reg == 1:
                print("You cried")
                skill = skill + 1.5
                happiness =  happiness -2
                print("")

            if reg == 2:
                print("You played")
                skill = skill + 2
                happiness = happiness +5
                intelligence = intelligence +2
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
    if (age >= 5 and age < 18) and status == 1:  # This process is needed when the age is between 4 and 19
        while True:

            skill = skill-2
            if skill>=100:
                skill=100
            elif skill>0:
                skill = 0

            happiness = happiness-2
            if happiness>=100:
                happiness=100
            elif happiness>0:
                happiness = 0

            intelligence = intelligence-2
            if intelligence>=100:
                intelligence=100
            elif intelligence>0:
                intelligence = 0

            print("Name : ", name)
            print("Sex : ", sex)
            print("You're skill(s) : ", skill)
            print("Your happiness : ", happiness)
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
                    skill = skill + 5
                    intelligence = intelligence + 3
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
                        happiness = happiness + 2
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
                                happiness = happiness-10
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
                t = 0
                if t==0:
                    print("Press 1 to burgle a home")
                    print("Press 2 to pickpocket")
                    print("Press 3 to behave behave deleqently")
                    print("Press 4 to shoplift")
                    print("Press 5 to steal a car")
                    print("Press 6 to murder a person")
                    print("Press 7 to hire a hitman")
                    print("Press 8 to launch a cyber attack")
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
                                    print("Money :", money)

                                else:
                                    print("SOMEONE CALLED YOU BREAKING INTO THE HOUSE AND CALLED THE POLICE ON YOU !!!")
                                    print("You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                    rand = random.randint(1,10)
                                    if rand<6 and crime == 0:
                                        print("You're arrested for burlary and have to spent 10 months in jail !!!")
                                        crime = crime+1
                                        jailtime = 1
                                        status = 3
                                        break
                                    elif rand<6 and crime <= 3:
                                        print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                        crime = crime+1
                                        jailtime = jailtime +1
                                        status = 3
                                    else:
                                        print("The lawyers have helped you to stay out of jail")
                                        print("You're free")
                        else:
                            rand = random.radint(0,20)
                            if crime==4 and rand<=3:
                                print("SOMEONE CALLED YOU BREAKING INTO THE HOUSE AND CALLED THE POLICE ON YOU !!!")
                                print("You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                rand = random.randint(1, 10)

                                if rand < 6 and crime == 4:
                                    print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                    crime = crime + 1
                                    jailtime = 1
                                    status = 3

                                elif rand<6 and crime > 4:
                                    print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                    crime = crime+1
                                    jailtime = jailtime*2
                                    status = 3

                                else:
                                    print("The lawyers have helped you to stay out of jail")
                                    print("You're free")

                            else:
                                print("You have robbed the house")
                                rand = random.randint(1, 9000)
                                print("You sold all the stolen items to a pawn shop and recieved $", rand)
                                money = money + rand
                                print("Money :", money)


                    if choice == 2:
                        print("You were walking down the streets and have found your target")
                        print("")
                        if crime < 3:
                            rand = 0
                            if rand == 0:
                                rob = int(input("Press 2 to pickpocket"))
                                if rob == 2:
                                    print("You have successfully pickpocketed")
                                    rand = random.randint(1, 10000)
                                    print("You sold all the stolen items to a pawn shop and recieved $", rand)
                                    money = money + rand
                                    print("Money :", money)

                                else:
                                    print("SOMEONE CALLED YOU BREAKING INTO THE HOUSE AND CALLED THE POLICE ON YOU !!!")
                                    print("You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                    rand = random.randint(1, 10)

                                    if rand < 6 and crime == 0:
                                        print("You're arrested for larceny and have to spent 1 year in jail !!!")
                                        crime = crime + 1
                                        jailtime = 1
                                        status = 3
                                        happiness = happiness - 20


                                    elif rand < 6 and crime <= 3:
                                        print("You're arrested for larceny and have to spent 1 year in jail !!!")
                                        crime = crime + 1
                                        jailtime = jailtime + 1
                                        status == 3
                                        happiness = happiness -20

                                    else:
                                        print("The lawyers have helped you to stay out of jail")
                                        print("You're free")
                                        happiness = happiness + 10

                        else:
                            rand = random.radint(0, 20)
                            if crime == 4 and rand <= 3:
                                print("SOMEONE CALLED YOU BREAKING INTO THE HOUSE AND CALLED THE POLICE ON YOU !!!")
                                print("You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                rand = random.randint(1, 10)

                                if rand < 6 and crime == 4:
                                    print("You're arrested for larceny and have to spent 1 year in jail !!!")
                                    crime = crime + 1
                                    jailtime = 1
                                    status = 3
                                    happiness = happiness -20


                                elif rand < 6 and crime > 4:
                                    crime = crime + 1
                                    jailtime = jailtime * 2
                                    status = 3
                                    print("You're arrested for larceny and have to spent ",jailtime," years in jail !!!")
                                    happiness = happiness -20


                                else:
                                    print("The lawyers have helped you to stay out of jail")
                                    print("You're free")
                                    happiness = happiess+ 5

                            else:
                                print("You have successfully pickpocketted")
                                rand = random.randint(1, 10000)
                                print("You sold all the stolen items to a pawn shop and recieved $", rand)
                                money = money + rand
                                print("Money :", money)
                                happiness = happiness + 5


                    if choice == 3:
                        print("Press 1 to prank an old person")
                        print("Press 2 to propagate fake news")
                        print("Press 3 to challenge random people to a fist fight")
                        print("Press 4 to throw rocks at buildings")
                        print("Press 5 to puncture tyres of random vehicles")
                        print("")
                        click= int(input("Enter your choice : "))
                        if click == 1:
                            rand = random.random.randint(0,100)
                            if rand<=10:
                                print("The old person called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0,100)
                                if rand<=10 and crime<3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime+1
                                    jailtime = 1
                                    happiness = happiness -10
                                    status =3

                                    print("")
                                    break

                                elif rand<=10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime+2
                                    print("You have to spent ",jailtime," years in prison")
                                    happiness = happiness -10
                                    status =3

                                    print("")
                                    break

                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1

                        if click == 2:
                            rand = random.random.randint(0, 100)
                            if rand <= 10:
                                print("The police have found  out that you've propagated fake news !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 1
                                    happiness = happiness - 10
                                    status = 3
                                    print("")

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 2
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")

                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1

                        if click == 3:
                            rand = random.random.randint(0, 100)
                            if rand <= 10:
                                print("Your opponent called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 1
                                    happiness = happiness - 10
                                    status = 3
                                    print("")

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 2
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")

                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")

                        if click == 4:
                            rand = random.random.randint(0, 100)
                            if rand <= 10:
                                print("Some random person called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 1
                                    happiness = happiness - 10
                                    status = 3
                                    print("")

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 2
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")


                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")

                        if click == 5:
                            rand = random.random.randint(0, 100)
                            if rand <= 10:
                                print("Some random person called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 1
                                    happiness = happiness - 10
                                    status = 3
                                    print("")

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 2
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")

                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")


            if reg == 4:
                print("Press 1 to spent time with all your relatives")
                print("Press 2 to look for a partner")
                click = int(input("Enter your choice : "))
                print("")
                if click == 1:
                    print("You spent time with all your relatives")
                    happiness = happiness +10
                if click == 2:
                    print("-----UNDER DEVELOPMENT--------")

            if reg == 5:
                age = age + 1
        if (age > 18):
            break

while (age >= 5 and age < 18) and status == 3:  # This process is needed when the age is between 4 and 19

    skill = skill + 1
    if skill >= 100:
        skill = 100
    elif skill > 0:
        skill = 0

    happiness = happiness - 1
    if happiness >= 100:
        happiness = 100
    elif happiness > 0:
        happiness = 0

    intelligence = intelligence - 1
    if intelligence >= 100:
        intelligence = 100
    elif intelligence > 0:
        intelligence = 0

    print("######### JUVIENILE PRISON #########")
    i = 0
    print("")
    print("While you're in prison, you're skill will increase as you will engage in prison jobs")
    print("Age : ", age)
    print("Duration of your sentence : ",jailtime)
    print("Money : ",money)
    print("")
    print("press 1 to work out")
    print("press 2 to interact with other inmates")
    print("press 3 to try to escape from prison")
    print("press 4 to read books")
    print("Press 5 to grow older")
    print("")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("You worked out in prison")
        happiness = happiness + 5
        skill = skill +  5
        print("")

    if choice == 2:
        rand = random.randint(0,6)
        if rand<2:
            print("Another prisoner has challenged you for a fight")
            print("Press 1 to fight with the person")
            print("Press 2 to ignore the proposal")
            click = int(input("Enter your choice : "))
            rand = random.randint(0,99)
            if click ==1 and rand<15:
                print("The guards have saw you fighting in prison")
                print("Your sentence has been extended by 2 yeas !!!!")
                jailtime= jailtime+2
                happiness = happiness-20
                print("")

            if click == 1 and (rand>=15 and rand<=20):
                print("You accidently killed the other prisoner while fighting !!!!")
                print("Your sentence has been extended by 50 yeas !!!!")
                jailtime = jailtime + 50
                happiness = happiness - 50
                print("")

            if click == 1 and (rand>=20 and rand<=25):
                print("You accidently killed you while fighting !!!!")
                dead = 1
                break

            else:
                rand = random.randint(0,2)
                if rand ==0:
                    print("The fight ended in a draw")
                    skill = skill +1
                    happiness = happiness + 2
                    print("")


                elif rand ==1:
                    print("The other prisoner won the fight")
                    skill = skill +1
                    happiness = happiness - 2
                    print("")

                elif rand ==2:
                    print("You won the fight")
                    skill = skill + 5
                    happiness = happiness + 10
                    print("")

        else:
            print("")
            print("press 1 to talk with other inmates")
            print("press 2 to challenge an inmate for a fight")
            click = int(input("Enter your choice : "))
            print("")
            if click == 1:
                rand = random.randint(0,99)
                if rand<15:
                    print("You and the other inmate have a conflict of opinion")
                    print("The other inmates challenges you for a fight")
                    print("Press 1 to fight")
                    print("Press 2 to agree to disagree")
                    print("Press 3 to apologize")
                    a = int(input("Enter your choice : "))
                    print("")
                    if a ==1:
                        rand=random.randint(0,5)
                        if rand==0:
                            print("The other prisoner killed you")
                            dead == 1
                            print("")
                            break

                        elif rand==1:
                            print("You killed the other prisoner")
                            print("You are being charged with manslaughter and you have to spent 50 years in prison additionally !!!!")
                            jailtime=jailtime+50
                            skill = skill+10
                            happiness = happiness -50
                            print("")
                            break

                        elif rand==2:
                            print("A guard saw you fighting")
                            print("You're charged for fighting in prison and have to spend 2 years in prisn additionally !!!!")
                            jailtime = jailtime+2
                            happiness = hapiness -10
                            print("")
                            break

                        else:
                            print("You fought in prison")
                            skill = skill + 10
                            happiness = happiness+10

                    elif a==2:
                        


    break