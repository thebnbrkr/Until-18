import random  # We have to import this module for generating random numbers
import time

print("-----------------------------------UNTIL 18-------------------------------------")
print("")
num = input("Press any key to continue : ")  # a condition to begin the game
start = num
if start == num:
    age = 0
    status = 1  # Status = 1 - Free person
    # Status = 3 - Is currently in juvie
    # Status = 4 - Is on the run
    # Status = 5 - Had been to juvie'''
    name = input("Enter your name : ")
    print("Choose your gender : ")
    print("Press 1 for male")
    print("Press 2 for female")
    print("Press 3 for other")
    print("")
    gender = input("Enter your choice : ")  # accepting an integer for a condition

    if gender == "1":
        sex = "Male"
        print("")

    elif gender == "2":
        sex = "Female"
        print("")

    elif gender == "3":
        sex = "Other"
        print("")

    else:
        rand = random.randint(1, 3)
        if rand == 1:
            sex = "Male"
        elif rand == 2:
            sex = "Female"
        elif rand == 3:
            sex = "Other"

    skill = random.randint(0, 99)  # The random.randint() function generates a random number
    happiness = random.randint(0, 99)
    intelligence = random.randint(0, 99)
    life = random.randint(30, 99)
    partner = random.randint(50, 99)

    eighteen = 0  # to end the game
    naughty = 0  # for measuring naughtiness
    club = 0  # by default 0 , when you join some club = some number
    clubskill = 0  # increases the talent, could potentially impact the future
    money = 0  # counting the money in your bank account
    crime = 0  # counting the total number of crimes
    prison = 0 #binary; changes to 1 if you've been to prison
    dead = 0  # binary value; becomes 1 when you die
    relationship = 0  # binary value; becomes one when you're in a relationship/married
    hacker = 0  # binary value; becomes 1 when you learn hacking
    sick = 0  # binary value; becomes 1 when your sick
    social_media = 0  # no of followers on social media
    streamer = 0  # no of followers on the streaming site
    vlog = 0  # no of followers on thr vloging site
    post_pics = 0  # no of pictures posted
    post_vids = 0  # no of videos posted
    fame = 1  # your fame
    vlog = 0  # vlog counter
    stream = 0  # no of streams
    follow = 1  # followers count
    vlogf = 1  # vlog follower count
    streamf = 1  # stream follower count
    abs = 1  # a variable that will be rounded as the number of follower
    jailtime = 0  # total number of years spend in prison

    Boys = ["Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan", "Anderson",
            "Blakely", "Bo", "Bodie", "Boden", "Brit", "Lotte", "Gioto", "Xander", "Loius", "Paolo", "Marcelo", "Ben",
            "Joe", "Hasan", "Elon", "Errol", "Kimbal", "Bernie", "Azim", "Ram", "Gopal"]

    Girls = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn", "Alice",
             "Maja", "Elsa", "Ella", "Ebba", "Alica", "Olivia", "Abella", "Mia", "Isla", "Maya", "Michelle", "Adriana",
             "Lola", "Clare", "Susan", "Tulsi", "Priya", "Sita"]

    LastNames = [" Kim", " Lee", " Park", " Mae", " Choi", " Chen", " Wang", " Yang", " Smith", " Johnson",
                 " William", " Brown", " Rodriguez", " Martinez", " Davis", " Garzia", " Jones", " Hall", " Kapoor",
                 " Sharma", " Reddy", " Nair", " Khan", " Shapiro", " Aarons", " Wolowitz", " Cummins"]

    if skill >= 100:
        skill = 100

if age < 5:  # main process when the age is lesser than i
    while True:
        skill = skill - 1
        if skill >= 100:
            skill = 100
        elif skill < 0:
            skill = 0

        happiness = happiness - 1
        if happiness >= 100:
            happiness = 100
        elif happiness < 0:
            happiness = 0

        intelligence = intelligence - 1
        if intelligence >= 100:
            intelligence = 100
        elif intelligence < 0:
            intelligence = 0

        life = life + 2
        if life >= 100:
            life = 100
        if life < 20:
            sick = 1
        elif life < 0:
            life = 0
        if sick == 1:
            print("You're really sick")
            print("You've been taken to the doctor")
            rand = random.randint(0, 5)
            if rand > 3:
                print("You died")
                dead = 1
                break
            else:
                print("You're cured")
                happiness = happiness + 10
                life = life + 20

        print("")
        print("Name : ", name)
        print("Sex : ", sex)
        print("You're skill(s) : ", skill)
        print("You're happiness : ", happiness)
        print("You're intelligence : ", intelligence)
        print("You're life : ", life)
        print("Your age :", age)
        print("")
        print("Press 1 to cry")
        print("Press 2 to play")
        print("Press 3 to do both")
        print("Press 4 to grow older")
        reg = input("Enter your choice : ")
        print("")
        if reg == "1":
            print("You cried")
            skill = skill + 1.5
            happiness = happiness - 2
            print("")

        if reg == "2":
            print("You played")
            skill = skill + 2
            happiness = happiness + 5
            intelligence = intelligence + 2
            print("")

        if reg == "3":
            print("You cried and played.")
            skill = skill + 1
            happiness = happiness + 0
            intelligence = intelligence + 1
            print("")

        if reg == "4":
            age = age + 1

        else:
            print("Please ener any one of the above")
        if (age > 4):
            break

while status == 1:
    if age == 19:
        break
    else:
        if prison == 1:
            age = age-2
        else:
            age = 5

    while (age >= 5 and age < 19) and status == 1:  # This process is needed when the age is between 4 and 19
        age = age + 1
        months = 0
        while months < 11:
            months = months + 1
            life = life - 2
            if life >= 100:
                life = 100
            if life < 20:
                sick = 1
            elif life < 0:
                life = 0

            skill = skill - 2
            if skill >= 100:
                skill = 100
            elif skill < 0:
                skill = 0

            happiness = happiness - 2
            if happiness >= 100:
                happiness = 100
            elif happiness < 0:
                happiness = 0

            intelligence = intelligence - 2
            if intelligence >= 100:
                intelligence = 100
            elif intelligence < 0:
                intelligence = 0

            partner = partner - 2
            if partner >= 100:
                partner = 100
            if partner < 20:
                print("Your partner dumped you")
            elif partner <= 0:
                partner = 0

            print("Name : ", name)
            print("Sex : ", sex)
            print("You're skill(s) : ", skill)
            print("Your happiness : ", happiness)
            print("Your intelligence : ", intelligence)
            print("Your age : ", age - 1)
            print("Months : ", months)
            print("Money : ", money)
            print("")
            print("Press 1 for school")
            print("Press 2 for part-time jobs")
            print("Press 3 for crimes ")
            print("Press 4 for relationships")
            print("Press 5 for activities")
            print("Press 6 to pass to the next month")
            reg = input("Enter your choice : ")
            print("")

            if reg == "1":  # school
                months = months-1
                print("")
                print("Press 1 for doing homework")
                print("Press 2 for spendinng time with friends")
                print("Press 3 for skipping class ")
                print("Press 4 for interacting with teachers")
                print("Press 5 for joining clubs")
                print("Press 6 to study harder")
                choice = input("Enter your choice : ")

                if choice == "1":
                    print("You did your homework")
                    skill = skill + 5
                    intelligence = intelligence + 3
                    print("")

                if choice == "2":
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

                if choice == "3":
                    rand = random.randint(0, 10)
                    if rand >= 0 and rand <= 4:
                        print("You tried to skip school but you were caught by a teacher")
                        print("The teacher decides to give you a detention")
                        print("")

                if choice == "4":
                    print("Press 1 to make fun of the teacher")
                    print("Press 2 for asking doubts")
                    print("")
                    a = input("Enter your choice : ")
                    if a == "1":
                        rand = random.randint(0, 100)
                        if rand >= 8 and rand <= 16:
                            if naughty >= 50:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher complained to the principal and you were suspended for a week")
                                print("")
                                naughty = naughty + 10
                                happiness = happiness - 10
                                print("You're hapiness decreased by 10 units")
                            else:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher gave you a detention")
                                print("")
                                naughty = naughty + 10
                                happiness = happiness - 10
                                print("You're hapiness decreased by 10 units")
                                print("")
                        if rand >= 0 and rand <= 7:
                            if naughty >= 50:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher complained to the principal and you were suspended for a week")
                                print("")
                                naughty = naughty + 10
                                happiness = happiness - 10
                                print("You're hapiness decreased by 10 units")
                            else:
                                print("You're teacher have found out that you are making fun of her")
                                print("You're teacher gave you a detention")
                                print("")
                                naughty = naughty + 10
                                happiness = happiness - 10
                                print("You're hapinness decreased by 10 units")
                                print("")
                        else:
                            print("Everone laughed at your jokes")
                            happiness = happiness + 10
                            naughty = naughty + 5
                            print("You're hapinness has increased by 10 units ")

                    if a == "2":
                        print("You cleared your doubts with your techers")
                        skill = skill + 3
                        intelligence = intelligence + 3
                        print("")

                if choice == "5":
                    if age >= 14:
                        print("")
                        print("Press 1 for joining the BasketBall Club")
                        print("Press 2 for joining the Chess Club")
                        print("Press 3 for joining the Football Club")
                        print("Press 4 for joining the Book Club")
                        print("Press 5 for joining the Tennis Club")
                        print("Press 6 for joining the Drama Club")
                        print("Press 7 for joining the Environmental Club")
                        print("Press 8 for joining the Cultural Club")
                        click = input("Enter your choice : ")
                        print("")

                        if click == "1":
                            if skill <= 20:
                                print("Sorry You do not have the skill to join this club")
                            else:
                                print("You have joined the BasketBall club")
                                club = 1
                                clubskill = clubskill + 10
                                club = click

                        if click == "2":
                            print("You have joined the Chess Club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        if click == "3":
                            if skill <= 40:
                                print("Sorry you do not have the skill to join this club")
                            else:
                                print("You have joined the Football club")
                                club = 1
                                clubskill = clubskill + 10
                                club = click

                        if click == "4":
                            print("You have joined the book club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        if click == "5":
                            if skill <= 45:
                                print("Sorry you do not have the skill to join this club")
                            else:
                                print("You have joined the Tennis Club")
                                club = 1
                                clubskill = clubskill + 10
                                club = click

                        if click == "6":
                            print("You have joined the Drama Club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        if click == "7":
                            print("You have joined the Environmental Club")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        if click == "8":
                            print("You have joined the Environmental Club`")
                            club = 1
                            clubskill = clubskill + 10
                            club = click

                        else:
                            print("Please press any one of the before mentioned keys")
                            print("")

                    else:
                        print("You're not old enough to join clubs")

                if choice == "6":
                    print("You studied harder")
                    skill = skill + 5
                    intelligence = intelligence + 5
                    happiness = happiness + 4

                else:
                    print("Press one of the above")

            if reg == "2":
                months = months-1
                if age >= 14:
                    print("The available part time jobs are : ")
                    print("Press 1 for hotdog maker")
                    print("Press 2 for server")
                    print("Press 3 for part-time janitor")
                    print("Press 4 for grocery store salesman")
                    print("Press 5 for hotdog maker")
                    print("Press 6 for internship at pow tech")
                    print("Press 7 for babysitter at babysitterinc corp")
                    print("")
                    choice = input("Enter your choice : ")

                    if choice == "1":
                        if skill >= 20:
                            print("You're hired !!!")
                            print("Salary $8 per hour")
                            money = ((8 * 4) * 20) + money
                            print("")

                        else:
                            print("You need atleast 20 skill units for this job")
                            print("")

                    if choice == "2":
                        if skill >= 30:
                            print("You're hired !!!")
                            print("Salary $9 per hour")
                            money = ((9 * 4) * 20) + money
                            print("")

                        else:
                            print("You need atleast 30 skill units for this job")
                            print("")

                    if choice == "3":
                        if skill >= 20:
                            print("You're hired !!!")
                            print("Salary $10 per hour")
                            money = ((10 * 4) * 20) + money
                            print("")
                        else:
                            print("You need atleast 20 skill units for this job")
                            print("")

                    if choice == "4":
                        if skill >= 30 and intelligence >= 20:
                            print("You're hired !!!")
                            print("Salary $13 per hour")
                            money = ((13 * 4) * 20) + money
                            print("")
                        else:
                            print("You need atleast 30 skill units and 20 intelligence units for this job")
                            print("")

                    if choice == "5":
                        print("You're hired !!!")
                        print("Salary $10 per hour")
                        money = ((10 * 4) * 20) + money
                        print("")

                    if choice == "6":
                        if skill >= 90 and intelligence >= 70:
                            print("You're hired !!!")
                            print("Salary $50 per hour")
                            money = ((50 * 4) * 20) + money
                            print("")
                        else:
                            print("You need atleast 80 skill units and 70 intelligence units for this job")
                            print("")

                    if choice == "7":
                        if skill >= 70 and intelligence >= 70:
                            print("You're hired !!!")
                            print("Salary $25 per hour")
                            money = ((25 * 4) * 20) + money
                            print("")
                        else:
                            print("You need atleast 70 skill units and 70 intelligence units for this job")
                            print("")

                    else:
                        print("Press one of the above")
                        print("")

                if age < 14:
                    print("You're not old enough join clubs")

            if reg == "3":
                months = months-1
                t = 0
                if t == 0:
                    print("Press 1 to burgle a home")
                    print("Press 2 to pickpocket")
                    print("Press 3 to behave behave deleqently")
                    print("Press 4 to shoplift")
                    print("Press 5 to steal a car")
                    print("Press 6 to murder a person")
                    print("Press 7 to hire a hitman")
                    print("Press 8 to launch a cyber attack")
                    print("")
                    choice = input("Enter your choice : ")
                    if choice == "1":
                        print("You were walking down the streets and have found your target house")
                        print("")
                        if crime < 3:
                            rand = 0
                            if rand == 0:
                                rob = input("Press 2 to rob the house")
                                print("")
                                if rob != "2":
                                    print("You changed your mind")
                                    print("")
                                if rob == "2":
                                    print("You have successfully robbed the house")
                                    rand = random.randint(1, 9000)
                                    print("You sold all the stolen items to a pawn shop and recieved $", rand)
                                    money = money + rand
                                    print("Money :", money)
                                    print("")

                                else:
                                    print("SOMEONE CALLED THE POLICE ON YOU !!!")
                                    print(
                                        "You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                    rand = random.randint(1, 10)
                                    if rand < 6 and crime == 0:
                                        print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                        crime = crime + 1
                                        jailtime = 12
                                        status = 3
                                        print("")
                                        break

                                    elif rand < 6 and crime <= 3:
                                        print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                        crime = crime + 1
                                        jailtime = jailtime + 12
                                        status = 3
                                        print("")
                                        break

                                    else:
                                        print("The lawyers have helped you to stay out of jail")
                                        print("You're free")
                                        print("")

                        else:
                            rand = random.randint(0, 20)
                            if crime == 4 and rand <= 3:
                                print("SOMEONE CALLED THE POLICE ON YOU !!!")
                                print(
                                    "You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                rand = random.randint(1, 10)
                                jailtime = 12
                                status = 3
                                print("")
                                break

                            if rand < 6 and crime == 4:
                                print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                crime = crime + 1
                                jailtime = 12
                                status = 3
                                break

                            elif rand < 6 and crime > 4:
                                print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                crime = crime + 1
                                jailtime = jailtime * 2
                                status = 3
                                break

                            else:
                                print("The lawyers have helped you to stay out of jail")
                                print("You're free")

                            print("You have robbed the house")
                            rand = random.randint(1, 9000)
                            print("You sold all the stolen items to a pawn shop and recieved $", rand)
                            money = money + rand
                            print("Money :", money)
                            print("")

                    if choice == "2":
                        print("You were walking down the streets and have found your target")
                        print("")
                        if crime < 3:
                            rand = 0
                            if rand == 0:
                                rob = input("Press 2 to pickpocket")
                                print("")
                                if rob != "2":
                                    print("You changed your mind")
                                    print("")
                                if rob == "2":
                                    print("You have successfully pickpocketed")
                                    rand = random.randint(1, 10000)
                                    print("You sold all the stolen items to a pawn shop and recieved $", rand)
                                    money = money + rand
                                    print("Money :", money)
                                    print("")

                                else:
                                    print("SOMEONE CALLED THE POLICE ON YOU !!!")
                                    print(
                                        "You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                    rand = random.randint(1, 10)
                                    jailtime = 12
                                    status = 3
                                    happiness = happiness - 20
                                    print("")
                                    break

                                if rand < 6 and crime == 0:
                                    print("You're arrested for larceny and have to spent 1 year in jail !!!")
                                    crime = crime + 1
                                    jailtime = 12
                                    status = 3
                                    happiness = happiness - 20
                                    print("")
                                    break

                                elif rand < 6 and crime <= 3:
                                    print("You're arrested for larceny and have to spent 1 year in jail !!!")
                                    crime = crime + 1
                                    jailtime = jailtime + 12
                                    status == 3
                                    happiness = happiness - 20
                                    print("")
                                    break

                                else:
                                    print("The lawyers have helped you to stay out of jail")
                                    print("You're free")
                                    happiness = happiness + 10

                        else:
                            rand = random.randint(0, 20)
                            if crime == 4 and rand <= 3:
                                print("SOMEONE CALLED THE POLICE ON YOU !!!")
                                print(
                                    "You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                rand = random.randint(1, 10)
                                jailtime = 12
                                status = 3
                                break

                                if rand < 6 and crime == 4:
                                    print("You're arrested for larceny and have to spent 1 year in jail !!!")
                                    crime = crime + 1
                                    jailtime = 1
                                    status = 3
                                    happiness = happiness - 20
                                    break


                                elif rand < 6 and crime > 4:
                                    crime = crime + 1
                                    jailtime = jailtime * 2
                                    status = 3
                                    print("You're arrested for larceny and have to spent ", jailtime,
                                          " years in jail !!!")
                                    happiness = happiness - 20
                                    break


                                else:
                                    print("The lawyers have helped you to stay out of jail")
                                    print("You're free")
                                    happiness = happiness + 5

                            else:
                                print("You have successfully pickpocketted")
                                rand = random.randint(1, 10000)
                                print("You sold all the stolen items to a pawn shop and recieved $", rand)
                                money = money + rand
                                print("Money :", money)
                                happiness = happiness + 5

                    if choice == "3":
                        print("Press 1 to prank an old person")
                        print("Press 2 to propagate fake news")
                        print("Press 3 to challenge random people to a fist fight")
                        print("Press 4 to throw rocks at buildings")
                        print("Press 5 to puncture tyres of random vehicles")
                        print("")
                        click = input("Enter your choice : ")
                        print("")
                        if click == "1":
                            rand = random.randint(0, 100)
                            if rand <= 10:
                                print("The old person called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 12
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 12
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break


                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")

                        if click == "2":
                            rand = random.randint(0, 100)
                            if rand <= 10:
                                print("The police have found  out that you've propagated fake news !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 12
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 24
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")

                        if click == "3":
                            rand = random.randint(0, 100)
                            if rand <= 10:
                                print("Your opponent called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                print("")

                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 12
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 12
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")

                        if click == "4":
                            rand = random.randint(0, 100)
                            print("")

                            if rand <= 10:
                                print("Some random person called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                print("")

                            if rand <= 10 and crime < 3:
                                print("The lawyers have failed to prove your innocence")
                                print("You have to spent 1 year in prison")
                                crime = crime + 1
                                jailtime = 12
                                happiness = happiness - 10
                                status = 3
                                print("")
                                break

                            elif rand <= 10:
                                print("The lawyers have failed to prove your innocence")
                                crime = crime + 1
                                jailtime = jailtime + 12
                                print("You have to spent ", jailtime, " years in prison")
                                happiness = happiness - 10
                                status = 3
                                print("")
                                break


                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")

                        if click == "5":
                            rand = random.randint(0, 100)
                            print("")

                            if rand <= 10:
                                print("Some random person called the police on you !!!!")
                                print("You've been arrested by the police and your parents have highered a lawyer")
                                rand = random.randint(0, 100)
                                print("")

                                if rand <= 10 and crime < 3:
                                    print("The lawyers have failed to prove your innocence")
                                    print("You have to spent 1 year in prison")
                                    crime = crime + 1
                                    jailtime = 12
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand <= 10:
                                    print("The lawyers have failed to prove your innocence")
                                    crime = crime + 1
                                    jailtime = jailtime + 12
                                    print("You have to spent ", jailtime, " years in prison")
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                            else:
                                print("You had fun")
                                happiness = happiness + 1
                                skill = skill + 1
                                print("")

                        else:
                            print("Press anyone of the given keys")
                            print("")

                    if choice == "4":

                        print("You were walking down the streets and have found your target store")
                        print("")
                        if crime < 3:
                            rand = 0
                            if rand == 0:
                                rob = input("Press 2 to rob the house")
                                print("")
                                if rob != "2":
                                    print("You changed your mind")
                                    print("")
                                if rob == "2":
                                    print("You have successfully robbed the house")
                                    rand = random.randint(1, 10000)
                                    print("You sold all the stolen items to a pawn shop and recieved $", rand)
                                    money = money + rand
                                    print("Money :", money)
                                    print("")

                                else:
                                    print("SOMEONE CALLED THE POLICE ON YOU !!!")
                                    print("")
                                    print(
                                        "You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                    rand = random.randint(1, 10)
                                    print("")

                                    if rand < 6 and crime == 0:
                                        print("You're arrested for burlary and have to spent 1 year months in jail !!!")
                                        crime = crime + 1
                                        jailtime = 12
                                        status = 3
                                        print("")
                                        break

                                    elif rand < 6 and crime <= 3:
                                        print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                        crime = crime + 1
                                        jailtime = jailtime + 12
                                        status = 3
                                        print("")
                                        break

                                    else:
                                        print("The lawyers have helped you to stay out of jail")
                                        print("You're free")
                                        print("")


                        else:
                            rand = random.randint(0, 20)
                            if crime == 4 and rand <= 3:
                                print("SOMEONE CALLED THE POLICE ON YOU !!!")
                                print(
                                    "You were arrested by the police and your parents have hired a lawyer to defend you in court")
                                rand = random.randint(1, 10)
                                jailtime = 1
                                status = 3
                                print("")
                                break

                            if rand < 6 and crime == 4:
                                print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                crime = crime + 1
                                jailtime = 1
                                status = 3
                                print("")
                                break

                            elif rand < 6 and crime > 4:
                                print("You're arrested for burlary and have to spent 1 year in jail !!!")
                                crime = crime + 1
                                jailtime = jailtime * 2
                                status = 3
                                print("")
                                break

                            else:
                                print("The lawyers have helped you to stay out of jail")
                                print("You're free")
                                print("")

                            print("You have robbed the house")
                            rand = random.randint(1, 9000)
                            print("You sold all the stolen items to a pawn shop and recieved $", rand)
                            money = money + rand
                            print("Money :", money)
                            print("")

                    if choice == "5":
                        print("You were walking down the streets......")
                        time.sleep(2)
                        print("Press 1 to steal a very exppensive car")
                        print("Press 2 to steal a moderately expensive car")
                        print("Press 3 to steal a cheap car")
                        print("Press 4 to a skateboard")
                        print("")
                        click = input("Enter your choice : ")
                        print("")
                        time.sleep(1)
                        rand = random.randint(0, 99)
                        if click == "1":
                            if rand > 10:
                                print("SOMEONE CALLED THE POLICE ON YOU")
                                print("Your parents have hired a lawyer to defend you in court")
                                time.sleep(1)
                                print("")
                                print("...")
                                time.sleep(1)
                                rand = random.randint(0, 99)
                                if rand > 40 and crime < 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 3 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 36
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand > 40 and crime >= 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 5 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 60
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                            else:
                                print("")
                                print("You stole the expensive car")
                                rand = random.randint(1,10)
                                if rand == 9:
                                    time.sleep(1)
                                    a = random.randint(500000, 1000000)
                                    print("You sold the exepensive car for : $", a, " !!!!!")
                                    money = money + a
                                    print("")
                                else:
                                    print("")
                                    print("You stole the expensive car")
                                    time.sleep(1)
                                    a = random.randint(50000, 100000)
                                    print("You sold the exepensive car for : $", a, " !!!!!")
                                    money = money + a
                                    happiness = happiness + 10
                                    skill = skill + 5
                                    print("")

                        if click == "2":
                            if rand > 10:
                                print("SOMEONE CALLED THE POLICE ON YOU")
                                print("Your parents have hired a lawyer to defend you in court")
                                time.sleep(1)
                                print("")
                                print("...")
                                time.sleep(1)
                                rand = random.randint(0, 99)
                                if rand > 40 and crime < 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 3 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 36
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand > 40 and crime >= 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 5 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 60
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                            else:
                                print("")
                                print("You stole a moderately expensive car")
                                rand = random.randint(10)
                                if rand == 9:
                                    time.sleep(1)
                                    a = random.randint(15000, 49999)
                                    print("You sold the exepensive car for : $", a, " !!!!!")
                                    money = money + a
                                    print("")

                                else:
                                    print("")
                                    print("You stole the expensive car")
                                    time.sleep(1)
                                    a = random.randint(50000, 100000)
                                    print("You sold the exepensive car for : $", a, " !!!!!")
                                    money = money + a
                                    happiness = happiness + 10
                                    skill = skill + 5
                                    print("")

                        if click == "3":

                            if rand > 10:
                                print("SOMEONE CALLED THE POLICE ON YOU")
                                print("Your parents have hired a lawyer to defend you in court")
                                time.sleep(1)
                                print("")
                                print("...")
                                time.sleep(1)
                                rand = random.randint(0, 99)
                                if rand > 40 and crime < 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 3 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 36
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand > 40 and crime >= 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 5 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 60
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                            else:
                                print("")
                                print("You stole an inexpensive car")
                                rand = random.randint(10)
                                if rand == 9:
                                    time.sleep(1)
                                    a = random.randint(3000, 14999)
                                    print("You sold the exepensive car for : $", a, " !!!!!")
                                    money = money + a
                                    print("")

                                else:
                                    print("")
                                    print("You stole the moderately inexpensive car")
                                    time.sleep(1)
                                    a = random.randint(15000, 25000)
                                    print("You sold the exepensive car for : $", a, " !!!!!")
                                    money = money + a
                                    happiness = happiness + 10
                                    skill = skill + 5
                                    print("")

                        if click == "4":
                            if rand > 10:
                                print("SOMEONE CALLED THE POLICE ON YOU")
                                print("Your parents have hired a lawyer to defend you in court")
                                time.sleep(1)
                                print("")
                                print("...")
                                time.sleep(1)
                                rand = random.randint(0, 99)
                                if rand > 40 and crime < 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 3 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 36
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                                elif rand > 40 and crime >= 3:
                                    print("Your lawyers weren't able to convince the judge")
                                    print("You have been awarded with 5 years in juvie !!!!!")
                                    crime = crime + 1
                                    jailtime = 60
                                    happiness = happiness - 10
                                    status = 3
                                    print("")
                                    break

                            else:
                                print("")
                                print("You stole a skateboard")
                                rand = random.randint(10)
                                if rand == 9:
                                    time.sleep(1)
                                    a = random.randint(1000, 2999)
                                    print("You sold the skateboard for : $", a, " !!!!!")
                                    money = money + a
                                    print("")

                                else:
                                    print("")
                                    print("You stole the moderately inexpensive car")
                                    time.sleep(1)
                                    a = random.randint(20, 999)
                                    print("You sold the exepensive car for : $", a, " !!!!!")
                                    money = money + a
                                    happiness = happiness + 10
                                    skill = skill + 5
                                    print("")

                        else:
                            print("Press anyone of the given keys")
                            print("")

                    if choice == "6":
                        time.sleep(1)
                        print("Who do you want to kill ?")
                        print("")
                        print("Press 1 for Mom")
                        print("Press 2 for Dad")
                        print("Press 3 for a relative")
                        print("Press 4 for your parter")
                        print("Press 5 for a random person")
                        print("")
                        click = input("Enter your choice : ")
                        print("")

                        if click == "1":
                            time.sleep(1)
                            a = int(input("Press 2 to commit murder : "))
                            print("")
                            rand = random.randint(0, 99)
                            if rand < 15:
                                print("...")
                                time.sleep(1)
                                print("You killed your mother")
                                print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                jailtime = jailtime + 300
                                time.sleep(1)
                                print("Yor parents refused to arrange a lawyer for you")
                                print("Your sentenced to ", jailtime, "years in prison")
                                happiness = happiness - 50
                                crime = crime + 1
                                status = 3

                            elif rand >= 15 and rand <= 20:
                                print("...")
                                time.sleep(1)
                                print("You got away with murder !!!")
                                happiness = happiness + 10
                                crime = crime + 1

                            elif rand >= 20:
                                print("...")
                                time.sleep(1)
                                print("Your mother understood your motives and called the police on you")
                                print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                jailtime = jailtime + 300
                                time.sleep(1)
                                print("Yor parents refused to arrange a lawyer for you")
                                happiness = happiness - 50
                                crime = crime + 1
                                status = 3
                                break

                        if click == "2":
                            cl = 1
                            if cl == 1:
                                time.sleep(1)
                                a = int(input("Press 2 to commit murder : "))
                                print("")
                                rand = random.randint(0, 99)
                                if rand < 15:
                                    print("...")
                                    time.sleep(1)
                                    print("You killed your mother")
                                    print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                    jailtime = jailtime + 300
                                    time.sleep(1)
                                    print("Yor parents refused to arrange a lawyer for you")
                                    print("Your sentenced to ", jailtime, "years in prison")
                                    happiness = happiness - 50
                                    crime = crime + 1
                                    status = 3
                                    break

                                elif rand >= 15 and rand <= 20:
                                    print("...")
                                    time.sleep(1)
                                    print("You got away with murder !!!")
                                    happiness = happiness + 10
                                    crime = crime + 1

                                elif rand >= 20:
                                    print("...")
                                    time.sleep(1)
                                    print("Your mother understood your motives and called the police on you")
                                    print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                    jailtime = jailtime + 300
                                    time.sleep(1)
                                    print("Yor parents refused to arrange a lawyer for you")
                                    happiness = happiness - 50
                                    crime = crime + 1
                                    status = 3
                                    break

                        if click == "3":
                            cl = 1
                            if cl == 1:
                                time.sleep(1)

                                rand = random.randint(0, 99)
                                if rand < 15:
                                    print("...")
                                    time.sleep(1)
                                    print("You killed a relative")
                                    print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                    jailtime = jailtime + 300
                                    time.sleep(1)
                                    print("Yor parents refused to arrange a lawyer for you")
                                    print("Your sentenced to ", jailtime, "years in prison")
                                    happiness = happiness - 50
                                    crime = crime + 1
                                    status = 3
                                    print("")
                                    break

                                elif rand >= 15 and rand <= 20:
                                    print("...")
                                    time.sleep(1)
                                    print("You got away with murder !!!")
                                    happiness = happiness + 10
                                    crime = crime + 1
                                    print("")

                                elif rand >= 20:
                                    print("...")
                                    time.sleep(1)
                                    print("Your relative understood your motives and called the police on you")
                                    print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                    jailtime = jailtime + 300
                                    time.sleep(1)
                                    print("Yor parents refused to arrange a lawyer for you")
                                    happiness = happiness - 50
                                    crime = crime + 1
                                    status = 3
                                    print("")
                                    break

                        if click == "4":
                            if relationship == 0:
                                print("You don't have a partner")
                                print("")

                            else:
                                cl = 1
                                if cl == 1:
                                    time.sleep(1)
                                    rand = random.randint(0, 99)
                                    if rand < 15:
                                        print("...")
                                        time.sleep(1)
                                        print("You killed your partner")
                                        print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                        jailtime = jailtime + 300
                                        time.sleep(1)
                                        print("Yor parents refused to arrange a lawyer for you")
                                        print("Your sentenced to ", jailtime, "years in prison")
                                        happiness = happiness - 50
                                        crime = crime + 1
                                        relationship = 0
                                        status = 3
                                        break

                                    elif rand >= 15 and rand <= 20:
                                        print("...")
                                        time.sleep(1)
                                        print("You got away with murder !!!")
                                        happiness = happiness + 10
                                        crime = crime + 1
                                        relationship = 0

                                    elif rand >= 20:
                                        print("...")
                                        time.sleep(1)
                                        print("Your partner understood your motives and called the police on you")
                                        print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                        jailtime = jailtime + 300
                                        time.sleep(1)
                                        print("Yor parents refused to arrange a lawyer for you")
                                        happiness = happiness - 50
                                        crime = crime + 1
                                        relationship = 0
                                        status = 3
                                        break

                        if click == "5":
                            cl = 1
                            if cl == 1:
                                time.sleep(1)
                                rand = random.randint(0, 99)
                                if rand < 15:
                                    print("...")
                                    time.sleep(1)
                                    print("You killed a random person")
                                    print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                    jailtime = jailtime + 300
                                    time.sleep(1)
                                    print("Yor parents refused to arrange a lawyer for you")
                                    print("Your sentenced to ", jailtime, "years in prison")
                                    happiness = happiness - 50
                                    crime = crime + 1
                                    status = 3
                                    print("")
                                    break

                                elif rand >= 15 and rand <= 20:
                                    print("...")
                                    time.sleep(1)
                                    print("You got away with murder !!!")
                                    happiness = happiness + 10
                                    crime = crime + 1
                                    print("")

                                elif rand >= 20:
                                    print("...")
                                    time.sleep(1)
                                    print("The random person understood your motives and called the police on you")
                                    print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                    jailtime = jailtime + 300
                                    time.sleep(1)
                                    print("Yor parents refused to arrange a lawyer for you")
                                    happiness = happiness - 50
                                    crime = crime + 1
                                    status = 3
                                    print("")
                                    break

                        else:
                            print("Press anyone of the given keys")
                            print("")

                    if choice == "7":
                        print("")
                        print("Press 1 to hire a expensive hitman")
                        print("Press 2 to hire a moderately expensive hitman")
                        print("Press 3 to hire an cheap hitman")
                        print("")
                        a = input("Enter your choice : ")
                        if a == "1" and money >= 250000:
                            money = money - 250000
                            k == 1
                            if k == 1:
                                print("")
                                print("who do you wanrt to kill")
                                print("Who do you want to kill ?")
                                print("")
                                print("Press 1 for Mom")
                                print("Press 2 for Dad")
                                print("Press 3 for a relative")
                                print("Press 4 for your parter")
                                print("Press 5 for a random person")
                                print("")
                                click = input("Enter your choice : ")
                                print("")

                                if click == "1":
                                    time.sleep(1)
                                    print("")
                                    rand = random.randint(0, 99)
                                    if rand < 5:
                                        print("...")
                                        time.sleep(1)
                                        print("The hitman killed your mother")
                                        print("The hitman confessed that you were responsible for the murder !!!")
                                        print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                        jailtime = jailtime + 300
                                        print("")
                                        time.sleep(1)
                                        print("Yor parents refused to arrange a lawyer for you")
                                        print("Your sentenced to ", jailtime, "years in prison")
                                        happiness = happiness - 50
                                        crime = crime + 1
                                        status = 3
                                        print("")
                                        break

                                    elif rand >= 5 and rand < 100:
                                        print("...")
                                        time.sleep(1)
                                        print("You got away with murder !!!")
                                        happiness = happiness + 10
                                        crime = crime + 1
                                        print("")

                                if click == "2":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 5:
                                            print("...")
                                            time.sleep(1)
                                            print("The hitman killed your mother")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            jailtime = jailtime + 300
                                            time.sleep(1)
                                            print("")
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 5 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")

                                if click == "3":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 5:
                                            print("...")
                                            time.sleep(1)
                                            print("The hitman killed a relative")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 5 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")

                                if click == "4":
                                    if relationship == 0:
                                        print("You don't have a partner")
                                        money = money + 250000
                                        print("The hitman returned the money to you")
                                        print("")

                                    else:
                                        cl = 1
                                        if cl == 1:
                                            time.sleep(1)
                                            print("")
                                            rand = random.randint(0, 99)
                                            if rand < 5:
                                                print("...")
                                                time.sleep(1)
                                                print("You killed your partner")
                                                print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                                print(
                                                    "The hitman confessed that you were responsible for the murder !!!")
                                                jailtime = jailtime + 300
                                                time.sleep(1)
                                                print("Yor parents refused to arrange a lawyer for you")
                                                print("Your sentenced to ", jailtime, "years in prison")
                                                happiness = happiness - 50
                                                crime = crime + 1
                                                relationship = 0
                                                status = 3
                                                break

                                            elif rand >= 5 and rand <= 99:
                                                print("...")
                                                time.sleep(1)
                                                print("You got away with murder !!!")
                                                happiness = happiness + 10
                                                crime = crime + 1
                                                relationship = 0

                                if click == "5":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 5:
                                            print("...")
                                            time.sleep(1)
                                            print("You killed a random person")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 5 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")
                                            break

                                else:
                                    print("Press anyone of the given keys")
                                    print("")

                        elif a == "1" and money < 250000:
                            print("You don't have enough money")
                            print("You need atleast $250000")
                            print("")

                        if a == "2" and money >= 50000:
                            money = money - 50000
                            k = 1
                            if k == 1:
                                print("")
                                print("who do you want to kill")
                                time.sleep(1)
                                print("Who do you want to kill ?")
                                print("")
                                print("Press 1 for Mom")
                                print("Press 2 for Dad")
                                print("Press 3 for a relative")
                                print("Press 4 for your parter")
                                print("Press 5 for a random person")
                                print("")
                                click = input("Enter your choice : ")
                                print("")

                                if click == "1":
                                    time.sleep(1)
                                    print("")
                                    rand = random.randint(0, 99)
                                    if rand < 40:
                                        print("...")
                                        time.sleep(1)
                                        print("The hitman killed your mother")
                                        print("The hitman confessed that you were responsible for the murder !!!")
                                        print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                        jailtime = jailtime + 300
                                        print("")
                                        time.sleep(1)
                                        print("Yor parents refused to arrange a lawyer for you")
                                        print("Your sentenced to ", jailtime, "years in prison")
                                        happiness = happiness - 50
                                        crime = crime + 1
                                        status = 3
                                        print("")
                                        break

                                    elif rand >= 40 and rand < 100:
                                        print("...")
                                        time.sleep(1)
                                        print("You got away with murder !!!")
                                        happiness = happiness + 10
                                        crime = crime + 1
                                        print("")

                                if click == "2":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 40:
                                            print("...")
                                            time.sleep(1)
                                            print("The hitman killed your mother")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 40 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")

                                if click == "3":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 40:
                                            print("...")
                                            time.sleep(1)
                                            print("The hitman killed a relative")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 40 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")

                                if click == "4":
                                    if relationship == 0:
                                        print("You don't have a partner")
                                        money = money + 50000
                                        print("The hitman returned the money to you")
                                        print("")

                                    else:
                                        cl = 1
                                        if cl == 1:
                                            time.sleep(1)
                                            print("")
                                            rand = random.randint(0, 99)
                                            if rand < 40:
                                                print("...")
                                                time.sleep(1)
                                                print("You killed your partner")
                                                print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                                print(
                                                    "The hitman confessed that you were responsible for the murder !!!")
                                                jailtime = jailtime + 300
                                                print("")
                                                time.sleep(1)
                                                print("Yor parents refused to arrange a lawyer for you")
                                                print("Your sentenced to ", jailtime, "years in prison")
                                                happiness = happiness - 50
                                                crime = crime + 1
                                                relationship = 0
                                                status = 3
                                                print("")
                                                break

                                            elif rand >= 40 and rand <= 99:
                                                print("...")
                                                time.sleep(1)
                                                print("You got away with murder !!!")
                                                happiness = happiness + 10
                                                crime = crime + 1
                                                relationship = 0
                                                print("")

                                if click == "5":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 40:
                                            print("...")
                                            time.sleep(1)
                                            print("You killed a random person")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 40 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")
                                            break

                                else:
                                    print("Press anyone of the given keys")
                                    print("")

                        elif a == "2" and money < 50000:
                            print("You don't have enough money")
                            print("You need atleast $50000")
                            print("")

                        if a == "3" and money >= 5000:
                            money = money - 5000
                            k == 1
                            if k == 1:
                                print("")
                                print("who do you wanrt to kill")
                                time.sleep(1)
                                print("Who do you want to kill ?")
                                print("")
                                print("Press 1 for Mom")
                                print("Press 2 for Dad")
                                print("Press 3 for a relative")
                                print("Press 4 for your parter")
                                print("Press 5 for a random person")
                                print("")
                                click = input("Enter your choice : ")
                                print("")

                                if click == "1":
                                    time.sleep(1)
                                    print("")
                                    rand = random.randint(0, 99)
                                    if rand < 85:
                                        print("...")
                                        time.sleep(1)
                                        print("The hitman killed your mother")
                                        print("The hitman confessed that you were responsible for the murder !!!")
                                        print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                        jailtime = jailtime + 300
                                        print("")
                                        time.sleep(1)
                                        print("Yor parents refused to arrange a lawyer for you")
                                        print("Your sentenced to ", jailtime, "years in prison")
                                        happiness = happiness - 50
                                        crime = crime + 1
                                        status = 3
                                        print("")
                                        break

                                    elif rand >= 85 and rand < 100:
                                        print("...")
                                        time.sleep(1)
                                        print("You got away with murder !!!")
                                        happiness = happiness + 10
                                        crime = crime + 1
                                        print("")

                                if click == "2":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 85:
                                            print("...")
                                            time.sleep(1)
                                            print("The hitman killed your mother")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 85 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")

                                if click == "3":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 85:
                                            print("...")
                                            time.sleep(1)
                                            print("The hitman killed a relative")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 85 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")

                                if click == "4":
                                    if relationship == 0:
                                        print("You don't have a partner")
                                        money = money + 5000
                                        print("The hitman returned the money to you")
                                        print("")

                                    else:
                                        cl = 1
                                        if cl == 1:
                                            time.sleep(1)
                                            print("")
                                            rand = random.randint(0, 99)
                                            if rand < 85:
                                                print("...")
                                                time.sleep(1)
                                                print("You killed your partner")
                                                print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                                print(
                                                    "The hitman confessed that you were responsible for the murder !!!")
                                                jailtime = jailtime + 300
                                                print("")
                                                time.sleep(1)
                                                print("Yor parents refused to arrange a lawyer for you")
                                                print("Your sentenced to ", jailtime, "years in prison")
                                                happiness = happiness - 50
                                                crime = crime + 1
                                                relationship = 0
                                                status = 3
                                                print("")
                                                break

                                            elif rand >= 85 and rand <= 99:
                                                print("...")
                                                time.sleep(1)
                                                print("You got away with murder !!!")
                                                happiness = happiness + 10
                                                crime = crime + 1
                                                relationship = 0
                                                print("")

                                if click == "5":
                                    cl = 1
                                    if cl == 1:
                                        time.sleep(1)
                                        print("")
                                        rand = random.randint(0, 99)
                                        if rand < 85:
                                            print("...")
                                            time.sleep(1)
                                            print("You killed a random person")
                                            print("THE POLICE HAVE ARRESTED YOU FOR MURDER")
                                            print("The hitman confessed that you were responsible for the murder !!!")
                                            jailtime = jailtime + 300
                                            print("")
                                            time.sleep(1)
                                            print("Yor parents refused to arrange a lawyer for you")
                                            print("Your sentenced to ", jailtime, "years in prison")
                                            happiness = happiness - 50
                                            crime = crime + 1
                                            status = 3
                                            print("")
                                            break

                                        elif rand >= 85 and rand <= 99:
                                            print("...")
                                            time.sleep(1)
                                            print("You got away with murder !!!")
                                            happiness = happiness + 10
                                            crime = crime + 1
                                            print("")

                                else:
                                    print("Press anyone of the given keys")
                                    print("")

                        elif a == "3" and money < 5000:
                            print("You don't have enough money")
                            print("You need atleast $5000")
                            print("")

                    if choice == "8":
                        if hacker == 0:
                            print("You have to learn hacking ")
                            time.sleep(1)
                            print("For that you need $200")
                            print("")
                            if money <= 200:
                                print("You need $200 to enroll in a hacking course")
                                hacker = 1
                                print("")
                            else:
                                print("Press 1 to hack wifi's")
                                print("Press 2 to hack a bank account")
                                print("Press 3 to hack data and sell it")
                                print("Press 4 to hack into the server of a billion dollar company and sell their data")
                                print("")
                                click = input("Enter your choice : ")
                                if click == "1":
                                    rand = random.randint(0, 99)
                                    if rand > 30:
                                        print("You hacked into someone's wifi")
                                        print("You had fun")
                                        skill = skill + 10
                                        happiness = happiness + 10
                                        print("")
                                    elif rand < 5:
                                        print("You weren't able to access into the wifi")
                                        print("SOMEHOW THE POLICE UNDERSTOOD THAT YOU WERE COMMITTING CYBER CRIME !!!")
                                        happiness = happiness - 10
                                        skill = skill + 3
                                        jailtime = 24
                                        status = 3
                                        print("You have to serve in jail for 2 years")
                                        print("")
                                        break

                                    elif rand <= 5 and rand <= 30:
                                        print("You weren't able to access into the wifi")
                                        happiness = happiness - 10
                                        skill = skill + 3
                                        print("")

                                if click == "2":
                                    rand = random.randint(0, 99)
                                    if rand > 70:
                                        print("You hacked into someone's bank account")
                                        print("You had fun")
                                        rand = random.randint(0, 9)
                                        if rand == 9:
                                            a = random.randint(50000, 125000)
                                            money = money + a
                                            print(" You made $", a, " extra money")
                                            skill = skill + 10
                                            happiness = happiness + 30
                                            print("")
                                        else:
                                            a = random.randint(100, 45000)
                                            money = money + a
                                            print(" You made $", a, " extra money")
                                            skill = skill + 10
                                            happiness = happiness + 20
                                            print("")

                                    elif rand < 70:
                                        print("You weren't able to access into the wifi")
                                        print("SOMEHOW THE POLICE UNDERSTOOD THAT YOU WERE COMMITTING CYBER CRIME !!!")
                                        happiness = happiness - 10
                                        skill = skill + 3
                                        jailtime = 48
                                        print("You have to serve in jail for 4 years")
                                        status = 3
                                        print("")
                                        break

                                if click == "3":
                                    rand = random.randint(0, 99)
                                    if rand > 80:
                                        print("You hacked into some server and sold their data in the black market")
                                        print("You had fun")
                                        rand = random.randint(0, 9)
                                        if rand == 9:
                                            a = random.randint(500000, 12500000)
                                            money = money + a
                                            print(" You made $", a, " extra money")
                                            skill = skill + 10
                                            happiness = happiness + 30
                                            print("")
                                        else:
                                            a = random.randint(10000, 300000)
                                            money = money + a
                                            print(" You made $", a, " extra money")
                                            skill = skill + 10
                                            happiness = happiness + 20
                                            print("")

                                    elif rand < 80:
                                        print("You weren't able to access into the wifi")
                                        print("SOMEHOW THE POLICE UNDERSTOOD THAT YOU WERE COMMITTING CYBER CRIME !!!")
                                        happiness = happiness - 10
                                        skill = skill + 3
                                        jailtime = 48
                                        print("You have to serve in jail for 4 years")
                                        status = 3
                                        print("")

                                if click == "4":
                                    rand = random.randint(0, 99)
                                    if rand > 90:
                                        print("You hacked into some server and sold their data in the black market")
                                        print("You had fun")
                                        rand = random.randint(0, 9)
                                        if rand == 9:
                                            a = random.randint(5000000, 1250000000)
                                            money = money + a
                                            print(" You made $", a, " extra money")
                                            skill = skill + 10
                                            happiness = happiness + 30
                                            print("")
                                        else:
                                            a = random.randint(1000000, 80000000)
                                            money = money + a
                                            print(" You made $", a, " extra money")
                                            skill = skill + 10
                                            happiness = happiness + 20
                                            print("")

                                    elif rand < 90:
                                        print("You weren't able to access into the wifi")
                                        print("SOMEHOW THE POLICE UNDERSTOOD THAT YOU WERE COMMITTING CYBER CRIME !!!")
                                        happiness = happiness - 10
                                        skill = skill + 3
                                        jailtime = 48
                                        print("You have to serve in jail for 4 years")
                                        status = 3
                                        print("")
                                        break

                                else:
                                    print("Press anyone of the given keys")
                                    print("")

            if reg == "4":
                months = months-1
                print("Press 1 to spent time with all your relatives")
                print("Press 2 to look for a partner")
                print("Press 3 to spent time with your partner")
                print("Press 4 to break up")
                click = input("Enter your choice : ")
                print("")
                if click == "1":
                    print("You spent time with all your relatives")
                    happiness = happiness + 10

                if click == "2":
                    if relationship == 0:
                        print("Press 1 to look for a girlfriend")
                        print("Press 2 to look for a boyfriend")
                        print("")
                        a = input("Enter your choice : ")
                        if a == "1":
                            print("")
                            x = 0
                            while x < 4:
                                skill = random.randint(0, 99)  # The random.randint() function generates a random number
                                happiness = random.randint(0, 99)
                                intelligence = random.randint(0, 99)
                                names = random.choice(Girls) + random.choice(LastNames)
                                rand = random.randint(0, 10)
                                print("Name : ", names)
                                print("Happiness : ", happiness)
                                print("Intelligence : ", intelligence)
                                print("Skill : ", skill)
                                print("")
                                print("Press 1 to ask her out")
                                print("Press any key to look for a different person")
                                q = input("Enter your choice :")
                                if q == "1":
                                    rand = random.randint(0, 9)
                                    if rand <= 4:
                                        print(names, " rejected you.")
                                    else:
                                        print("You're now going out with ", names, " !!!")
                                        relationship = 1
                                        happiness = happiness + 25
                                        x = 4
                                else:
                                    x = x + 1
                                if x == 4 or x > 4:
                                    print("You have either found a partner")
                                    print("If not, then sorry")
                                    break

                        if a == "2":
                            print("")
                            x = 0
                            while x < 4:
                                skill = random.randint(0, 99)  # The random.randint() function generates a random number
                                happiness = random.randint(0, 99)
                                intelligence = random.randint(0, 99)
                                names = random.choice(Boys) + random.choice(LastNames)
                                rand = random.randint(0, 10)
                                print("Name : ", names)
                                print("Happiness : ", happiness)
                                print("Intelligence : ", intelligence)
                                print("Skill : ", skill)
                                print("")
                                print("Press 1 to ask him out")
                                print("Press any key to look for a different person")
                                q = input("Enter your choice :")
                                if q == "1":
                                    rand = random.randint(0, 9)
                                    if rand <= 4:
                                        print(names, " rejected you.")
                                    else:
                                        print("You're now going out with ", names, " !!!")
                                        relationship = 1
                                        happiness = happiness + 25
                                        x = 16
                                else:
                                    x = x + 1
                                if x == 4 and x < 16:
                                    print("You can't find anyone to date")
                                    print("")
                                    break
                                if x == 16:
                                    print("Congratulations !!!!")
                                    print("")

                        else:
                            print("Press anyone of the given keys")
                            print("")

                if click == "3":
                    if relationship == 0:
                        print("you don't have a partner")
                        print("")
                    else:
                        print("You spent time with your partner")
                        happiness = happiness + 10
                        partner = partner + 10

                if click == "4":
                    if relationship == 0:
                        print("you don't have a partner")
                        print("")
                    else:
                        print("You broke up")
                        print("")
                        relationship = 0

                elif relationship != 0:
                    print("You already have a partner")

                else:
                    print("Press anyone of the given keys")
                    print("")

            if reg == "5":
                months=months-1
                print("Press 1 to work out in the gym")
                print("Press 2 to read a book")
                print("Press 3 to read meditate")
                print("Press 4 to start a social media account")
                print("Press 5 to become a vlogger")
                print("Press 6 to become a streamer")
                print("")
                click = input("Enter your choice : ")
                if click == "1":
                    print("")
                    print("You worked out in the gym")
                    skill = skill + 2
                    life = life + 4
                    happiness = happiness + 3
                    print("")

                if click == "2":
                    print("")
                    print("You read a book")
                    skill = skill + 4
                    happiness = happiness + 3
                    intelligence = intelligence + 5
                    print("")

                if click == "3":
                    print("")
                    print("You meditated")
                    happiness = happiness + 4
                    life = life + 2
                    print("")

                if click == "4":
                    print("")
                    print("Press 1 to post a picture")
                    print("Press 2 to post a video")
                    print("")
                    a = input("Enter your choice : ")
                    if a == "1":
                        print("You posted a picture")
                        post_pics = post_pics + 1
                        print("Total number of pictures posted", post_pics)
                        happiness = happiness + 2
                        abs = abs * 2
                        follow = round(abs)
                        print("Followers : ", follow)
                        print("")

                    if a == "2":
                        print("You posted a videos")
                        post_vids = post_vids + 1
                        print("Total number of pictures posted", post_vids)
                        happiness = happiness + 2
                        abs = abs * 2
                        follow = round(abs)
                        print("Followers : ", follow)
                        print("")

                    else:
                        print("lease any one of the given choices")
                        print("")

                if click == "5":
                    print("You uploaded a video")
                    vlog = vlog + 1
                    print("Total number of pictures posted", vlog)
                    happiness = happiness + 2
                    abs = abs * 1.75
                    vlogf = round(abs)
                    print("Followers : ", vlogf)
                    print("Need atleast 5000 followers for monetization")
                    print("")
                    if vlogf >= 5000 and vlogf <= 10000:
                        money = money + 1
                        print("You made $1 in revenue")
                        print("")

                    elif vlogf >= 10000 and vlogf <= 50000:
                        money = money + 5
                        print("You made $5 in revenue")
                        print("")

                    elif vlogf >= 50000 and vlogf <= 100000:
                        money = money + 10
                        print("You made $10 in revenue")
                        print("")

                    elif vlogf >= 100000 and vlogf <= 200000:
                        money = money + 20
                        print("You made $20 in revenue")
                        print("")

                    elif vlogf >= 200000 and vlogf <= 300000:
                        money = money + 30
                        print("You made $30 in revenue")
                        print("")

                    elif vlogf >= 300000 and vlogf <= 400000:
                        money = money + 40
                        print("You made $40 revenue")
                        print("")

                    elif vlogf >= 400000 and vlogf <= 500000:
                        money = money + 50
                        print("You made $50 in revenue")
                        print("")

                    elif vlogf >= 500000 and vlogf <= 600000:
                        money = money + 60
                        print("You made $60 in revenue")
                        print("")

                    elif vlogf >= 600000 and vlogf <= 700000:
                        money = money + 70
                        print("You made $70 in revenue")
                        print("")

                    elif vlogf >= 700000 and vlogf <= 800000:
                        money = money + 80
                        print("You made $80 in revenue")
                        print("")

                    elif vlogf >= 800000 and vlogf <= 900000:
                        money = money + 90
                        print("You made $60 in this stream")
                        print("")

                    elif vlogf >= 900000 and vlogf <= 1000000:
                        money = money + 100
                        print("You made $60 in revenue")
                        print("")

                    elif vlogf >= 1000000 and vlogf <= 5000000:
                        money = money + 500
                        print("You made $500 in revenue")
                        print("")

                    elif vlogf >= 5000000 and vlogf <= 10000000:
                        money = money + 2000
                        print("You made $500 in revenue")
                        print("")

                    elif vlogf >= 10000000 and vlogf <= 50000000:
                        money = money + 20000
                        print("You made $20,000 in revenue")
                        print("")

                    elif vlogf >= 50000000 and vlogf <= 100000000:
                        money = money + 50000
                        print("You made $50,000 in revenue")
                        print("")

                    if vlogf > 100000000:
                        print("You made $500,000 in revenue")
                        money = money + 500000
                        print("")

                if click == "6":
                    print("You streamed a video")
                    stream = stream + 1
                    print("Total number of pictures posted", stream)
                    happiness = happiness + 2
                    abs = abs * 1.75
                    streamf = round(abs)
                    print("Followers : ", streamf)
                    print("")

                    if streamf >= 5000 and streamf <= 10000:
                        money = money + 1
                        print("You made $1 in this stream")
                        print("")

                    elif streamf >= 10000 and streamf <= 50000:
                        money = money + 5
                        print("You made $5 in this stream")
                        print("")

                    elif streamf >= 50000 and streamf <= 100000:
                        money = money + 10
                        print("You made $10 in this stream")
                        print("")

                    elif streamf >= 100000 and streamf <= 200000:
                        money = money + 20
                        print("You made $20 in this stream")
                        print("")

                    elif streamf >= 200000 and streamf <= 300000:
                        money = money + 30
                        print("You made $30 in this stream")
                        print("")

                    elif streamf >= 300000 and streamf <= 400000:
                        money = money + 40
                        print("You made $40 in this stream")
                        print("")

                    elif streamf >= 400000 and streamf <= 500000:
                        money = money + 50
                        print("You made $50 in this stream")
                        print("")

                    elif streamf >= 500000 and streamf <= 600000:
                        money = money + 60
                        print("You made $60 in this stream")
                        print("")

                    elif streamf >= 600000 and streamf <= 700000:
                        money = money + 70
                        print("You made $70 in this stream")
                        print("")

                    elif streamf >= 700000 and streamf <= 800000:
                        money = money + 80
                        print("You made $80 in this stream")
                        print("")

                    elif streamf >= 800000 and streamf <= 900000:
                        money = money + 90
                        print("You made $60 in this stream")
                        print("")

                    elif streamf >= 900000 and streamf <= 1000000:
                        money = money + 100
                        print("You made $60 in this stream")
                        print("")

                    elif streamf >= 1000000 and streamf <= 5000000:
                        money = money + 500
                        print("You made $500 in this stream")
                        print("")

                    elif streamf >= 5000000 and streamf <= 10000000:
                        money = money + 2000
                        print("You made $500 in this stream")
                        print("")

                    elif streamf >= 10000000 and streamf <= 50000000:
                        money = money + 20000
                        print("You made $20,000 in this stream")
                        print("")

                    elif streamf >= 50000000 and streamf <= 100000000:
                        money = money + 50000
                        print("You made $50,000 in this stream")
                        print("")

                    if streamf > 100000000:
                        print("You made $500,000 in this stream")
                        money = money + 500000
                        print("")

            if reg == "6":
                if (months > 11):
                    break

            if age == 19:
                print("GAME OVER,YOU'RE NOW 18")
                print("Thanks for playing")
                break
                exit(0)

            else:
                print("")

    while (age >= 5 and age < 19) and status == 3:  # This process is needed when the age is between 4 and 19

        while age == 19:
            print("Your 18")
            break
        prison = 1
        life = life - 2
        if life >= 100:
            life = 100
        if life < 20:
            sick = 1
        elif life < 0:
            life = 0

        skill = skill + 1
        if skill >= 100:
            skill = 100
        elif skill < 0:
            skill = 0

        happiness = happiness - 1
        if happiness >= 100:
            happiness = 100
        elif happiness < 0:
            happiness = 0

        intelligence = intelligence - 1
        if intelligence >= 100:
            intelligence = 100
        elif intelligence < 0:
            intelligence = 0

        partner = partner - 2
        if partner >= 100:
            partner = 100
        elif partner <= 0:
            partner = 0

        print("######### JUVIENILE PRISON #########")
        print("")

        print("While you're in prison, you're skill will increase as you will engage in prison jobs")
        print("Age : ", age - 1)
        print("Duration of your sentence (months) : ", jailtime)
        print("Money : ", money)
        print("")
        print("press 1 to work out")
        print("press 2 to interact with other inmates")
        print("press 3 to try to escape from prison")
        print("press 4 to read books")
        print("Press 5 to grow older")
        print("")
        choice = input("Enter your choice : ")
        if choice == "1":
            print("You worked out in prison")
            happiness = happiness + 5
            skill = skill + 5
            print("")

        if choice == "2":
            rand = random.randint(0, 6)
            if rand < 2:
                print("Another prisoner has challenged you for a fight")
                print("Press 1 to fight with the person")
                print("Press 2 to ignore the proposal")
                click = input("Enter your choice : ")
                print("")
                rand = random.randint(0, 99)
                if click == "1" and rand < 15:
                    print("The guards have saw you fighting in prison")
                    print("Your sentence has been extended by 2 yeas !!!!")
                    jailtime = jailtime + 24
                    happiness = happiness - 20
                    print("")

                if click == "1" and (rand >= 15 and rand <= 20):
                    print("You accidently killed the other prisoner while fighting !!!!")
                    print("Your sentence has been extended by 50 yeas !!!!")
                    jailtime = jailtime + 600
                    happiness = happiness - 50
                    print("")

                if click == "1" and (rand >= 20 and rand <= 25):
                    print("You accidently killed you while fighting !!!!")
                    dead = 1
                    break

                if click == "2" and rand < 15:
                    print("")
                    print("The prisoner bet you uo anyway")
                    happiness = happiness - 10

                if click == "2" and (rand >= 15 and rand <= 20):
                    print("")
                    print("The prisoner bet you uo anyway")
                    print("The other person killed you")
                    print("")

                else:
                    rand = random.randint(0, 2)
                    if rand == 0:
                        print("The fight ended in a draw")
                        skill = skill + 1
                        happiness = happiness + 2
                        print("")


                    elif rand == 1:
                        print("The other prisoner won the fight")
                        skill = skill + 1
                        happiness = happiness - 2
                        print("")

                    elif rand == 2:
                        print("You won the fight")
                        skill = skill + 5
                        happiness = happiness + 10
                        print("")

            else:
                print("")
                print("press 1 to talk with other inmates")
                print("press 2 to challenge an inmate for a fight")
                click = input("Enter your choice : ")
                print("")
                if click == "1":
                    rand = random.randint(0, 99)
                    if rand < 15:
                        print("You and the other inmate have a conflict of opinion")
                        print("The other inmates challenges you for a fight")
                        print("Press 1 to fight")
                        print("Press 2 to agree to disagree")
                        print("Press 3 to apologize")
                        a = input("Enter your choice : ")
                        print("")
                        if a == "1":
                            rand = random.randint(0, 5)
                            if rand == 0:
                                print("The other prisoner killed you")
                                dead = 1
                                print("")
                                break


                            elif rand == 1:
                                print("You killed the other prisoner")
                                print(
                                    "You are being charged with manslaughter and you have to spent 50 years in prison additionally !!!!")
                                jailtime = jailtime + 600
                                skill = skill + 10
                                happiness = happiness - 50
                                print("")


                            elif rand == 2:
                                print("A guard saw you fighting")
                                print(
                                    "You're charged for fighting in prison and have to spend 2 years in prisn additionally !!!!")
                                jailtime = jailtime + 24
                                happiness = happiness - 10
                                print("")


                            else:
                                print("You fought in prison")
                                skill = skill + 10
                                happiness = happiness + 10

                        elif a == "2":
                            rand = random.randint(0, 10)
                            if rand == 1:
                                print("You agreed to disagree")
                                print("The other inmate wasn't satisfied with your response")
                                print("The other inmate killed you")
                                dead = 1
                                print("")
                                break

                            else:
                                print("You agreed to disagree")
                                print("")

                        elif a == "3":
                            rand = random.randint(0, 10)
                            if rand == 1:
                                print("You apologized to the other inmate")
                                print("The other inmate wasn't satisfied with your response")
                                print("The othe inmate killed you")
                                dead = 1
                                print("")
                                break

                            else:
                                print("You apologized to the other inmate")
                                print("")

                if click == "2":
                    print("You challenged an inmate for a fight")
                    rand = random.randint(0, 10)
                    print("")
                    if rand == 8:
                        print("You accidently killed the other prisoner in the fight")
                        happiness = happiness - 30
                        skill = skill + 10
                        jailtime = jailtime + 600
                        print("Your sentence has been extended by 50 years")
                        print("")

                    if rand == 9:
                        print("The other person accidently killed you in a fight")
                        print("You Died")
                        dead = 1
                        print("")
                        break

                    if rand == 10:
                        print(" A guard saw you fighting")
                        print(" Ypur sentence has been extended for 2 years for fighting in prison")
                        jailtime = jailtime + 24
                        print("")

                else:
                    print("Please choose one among the mentioned options")
                    print("")

        if choice == "3":
            print("")
            print("Do you want to escape ?")
            click = input("Press 1 to continue")
            if click == "1":
                j = 0
                if j == 0:
                    rand = random.randint(1, 38)
                    if rand == 1:
                        print("2+3 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 7")
                        print("press 4 for 8")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 2:
                        print("20+3 = ")
                        print("")
                        print("press 1 for 23")
                        print("press 2 for 24")
                        print("press 3 for 25")
                        print("press 4 for 26")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 3:
                        print("2+4 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 7")
                        print("press 4 for 8")
                        print("")
                        a = input("Enter your choice")
                        if a == "2":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 4:
                        print("2+5 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 7")
                        print("press 4 for 8")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 5:
                        print("2+6 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 7")
                        print("press 4 for 8")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 6:
                        print("What is the full form of UN")
                        print("")
                        print("press 1 for United Nations")
                        print("press 2 for United Notion")
                        print("press 3 for Unlisted Notion")
                        print("press 4 for Unlisted Nothing")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 7:
                        print("Which among these options use photosynthesis: ")
                        print("")
                        print("press 1 for plants")
                        print("press 2 for humans")
                        print("press 3 for photographers")
                        print("press 4 for water")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 8:
                        print("Which placeis the capital of India ")
                        print("")
                        print("press 1 for New Delhi")
                        print("press 2 for Mumbai")
                        print("press 3 for Hyderabad")
                        print("press 4 for Bangaluru")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 9:
                        print("Which among these options is the capital of USA")
                        print("")
                        print("press 1 for Washington D.C")
                        print("press 2 for New York City")
                        print("press 3 for Seattle")
                        print("press 4 for Pheonix")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 10:
                        print(" 16 x 16 = ")
                        print("")
                        print("press 1 for 196")
                        print("press 2 for 256")
                        print("press 3 for 325")
                        print("press 4 for 576")
                        print("")
                        a = input("Enter your choice")
                        if a == "2":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 12:
                        print("Who among these is the founder of Amazon ?")
                        print("")
                        print("press 1 for Bill Clinton")
                        print("press 2 for Steve Jobs")
                        print("press 3 for Bill Gates")
                        print("press 4 for Jeff Bezoa")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 13:
                        print("Which among these options is the capital of Australia ")
                        print("")
                        print("press 1 for Sydney")
                        print("press 2 for Perth")
                        print("press 3 for Melbourne")
                        print("press 4 for Canberra")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 14:
                        print("Which among these options is the capital of Germany")
                        print("")
                        print("press 1 for Leipzig")
                        print("press 2 for Frankfurt")
                        print("press 3 for Berlin")
                        print("press 4 for Munich")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 15:
                        print("Who is the creator of linux")
                        print("")
                        print("press 1 for Dennis Ritchie")
                        print("press 2 for Brian Kernighan")
                        print("press 3 for Linus Torvalds")
                        print("press 4 for Steve Jobs ")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 16:
                        print("Which among these is a famous cricketer  ")
                        print("")
                        print("press 1 for Kurt Cobain")
                        print("press 2 for Brian Lara")
                        print("press 3 for Joe Rogan")
                        print("press 4 for Abhijit Banerjee")
                        print("")
                        a = input("Enter your choice")
                        if a == "2":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 17:
                        print("15 x 10 =")
                        print("")
                        print("press 1 15000")
                        print("press 2 1500")
                        print("press 3 150")
                        print("press 4 15")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 18:
                        print("Who among these is the co- founder of we work")
                        print("")
                        print("press 1 for Adam Neumann")
                        print("press 2 for Javed Karim")
                        print("press 3 for Larry Ellison")
                        print("press 4 for John McAfee")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 19:
                        print("Which among these movies have Tom Hanks acted in ? ")
                        print("")
                        print("press 1 for Once upon a time in Hollywood")
                        print("press 2 for The social network")
                        print("press 3 for The wolf of Wall Street")
                        print("press 4 for Forrest Gump")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 20:
                        print("In which platform is pewdiepie most popular ? ")
                        print("")
                        print("press 1 for Twitch")
                        print("press 2 for Snapchat")
                        print("press 3 for Twitter")
                        print("press 4 for Youtube")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 21:
                        print(" 2*2*2 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 7")
                        print("press 4 for 8")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 22:
                        print("root of 625")
                        print("")
                        print("press 1 for 23")
                        print("press 2 for 24")
                        print("press 3 for 25")
                        print("press 4 for 26")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 23:
                        print("2*4 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 7")
                        print("press 4 for 8")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 24:
                        print("2*5 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 10")
                        print("press 4 for 8")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 25:
                        print("2*6 = ")
                        print("")
                        print("press 1 for 5")
                        print("press 2 for 6")
                        print("press 3 for 7")
                        print("press 4 for 12")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 26:
                        print("Which company did David Filo and Jerry Yang start ?")
                        print("")
                        print("press 1 for Yahoo")
                        print("press 2 for Yelp")
                        print("press 3 for Netflix")
                        print("press 4 for Texaco")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 27:
                        print("Which company did Ma Huateng start ?")
                        print("")
                        print("press 1 for Tencent")
                        print("press 2 for Alibaba")
                        print("press 3 for Weibo")
                        print("press 4 for JD.com")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 28:
                        print("Who co-founded microsoft along with Bill Gates ")
                        print("")
                        print("press 1 for Ashton Kutcher")
                        print("press 2 for Paul Allen")
                        print("press 3 for Jack Doorsey")
                        print("press 4 for Tim Sweeny")
                        print("")
                        a = input("Enter your choice")
                        if a == "2":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 29:
                        print("Which among these options is the capital of California")
                        print("")
                        print("press 1 for San Francisco")
                        print("press 2 for Arkansas")
                        print("press 3 for Los Angeles")
                        print("press 4 for Sacramento")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 30:
                        print("In which year did World War 1 end ?")
                        print("")
                        print("press 1 for 1914")
                        print("press 2 for 1918")
                        print("press 3 for 2008")
                        print("press 4 for 1920")
                        print("")
                        a = input("Enter your choice")
                        if a == "2":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 11:
                        print("In which year did USA attain Independece ?")
                        print("")
                        print("press 1 for 1777")
                        print("press 2 for 1853")
                        print("press 3 for 1889")
                        print("press 4 for 1776")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 31:
                        print("In which year did India attain Independence ?")
                        print("")
                        print("press 1 for 1928")
                        print("press 2 for 1880")
                        print("press 3 for 1945")
                        print("press 4 for 1947")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 32:
                        print("Who among these is the co-founder of netflix ?")
                        print("")
                        print("press 1 for Ratan Tata")
                        print("press 2 for Mark Cuban")
                        print("press 3 for Reed Hastings")
                        print("press 4 for Divya Narendra")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 33:
                        print("Who is the creator of Ruby ?")
                        print("")
                        print("press 1 for Craig Federighi")
                        print("press 2 for Bjarne Stroustrup")
                        print("press 3 for Masayoshi Son")
                        print("press 4 for Yukihiro Matsumoto")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 34:
                        print(" Where was UNIX developed ?")
                        print("")
                        print("press 1 for Stanford University")
                        print("press 2 for Bell Labs")
                        print("press 3 for UC Berkley")
                        print("press 4 for MIT")
                        print("")
                        a = input("Enter your choice")
                        if a == "2":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 35:
                        print("Who built Temple OS ?")
                        print("")
                        print("press 1 Chris Hughes")
                        print("press 2 Marissa Mayer")
                        print("press 3 Terry Davis")
                        print("press 4 Sheryl Sandberg")
                        print("")
                        a = input("Enter your choice")
                        if a == "3":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 36:
                        print("Who among these developed Etherium ?")
                        print("")
                        print("press 1 for Vitalik Buterin")
                        print("press 2 for Lex Fridman")
                        print("press 3 for Ben Goertzel")
                        print("press 4 for Ken Thompson")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 37:
                        print("Who built Matlab ?")
                        print("")
                        print("press 1 for John Backus")
                        print("press 2 for Margaret Hamilton")
                        print("press 3 for Martin Odersky")
                        print("press 4 for Cleve Moler")
                        print("")
                        a = input("Enter your choice")
                        if a == "4":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended b3 years")
                            jailtime = jailtime + 3
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

                    if rand == 38:
                        print("Which video streaming service was previously known as 'justin.tv' ?")
                        print("")
                        print("press 1 for Twitch")
                        print("press 2 for bitwave.tv")
                        print("press 3 for dailymotion")
                        print("press 4 for dlive")
                        print("")
                        a = input("Enter your choice")
                        if a == "1":
                            print("You broke out of prison")
                            status = 1
                            crime = crime + 1
                            print("")

                        else:
                            print("You tried to escape from prison")
                            print("But a guard caught you !!!!")
                            print("your sentence has been extended by 3 years")
                            jailtime = jailtime + 36
                            happiness = happiness - 20
                            crime = crime + 1
                            print("")

        if choice == "4":
            print("You read books")
            skill = skill + 1
            intelligence = intelligence + 5

        else:

            jailtime = jailtime - 12
            age = age + 1

            if jailtime == 0:
                status = 1
                age = age + 1
                print("You're evicted from prison")
                print('')

            elif age == 19:
                print("Game Over,You're now 18")
                break

while dead == 1:
    while eighteen == 0:
        print("You died")
        print("Thanks for playing")
        print("Game over")
        eighteen = 1
        break