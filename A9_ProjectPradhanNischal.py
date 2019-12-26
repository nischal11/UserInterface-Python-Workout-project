# Nischal Pradhan IT 209 A9 project NP Fitness Online Weight training Gym


class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Athlete(Person):
    # Athlete class

    def __init__(self, name, age, gender, weight, height, goal, skill):
        self.name = str(name)
        self.age = int(age)
        self.gender = str(gender)
        self.weight = float(weight)
        self.height = float(height)
        self.goal = str(goal)
        self.skill = str(skill)
        self.schedule = []
        self.Excercise = []

    def __init__(self, name="test", age=24, gender="male", weight=160, height=6.2, goal="shredding", skill="beginner"):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.goal = goal
        self.skill = skill
        self.schedule = []
        self.Excercise = []

    # this code calculates BMI of the Athlete
    def calcBMI(self):
        return ((self.weight * 703) / self.height ** 2)

    # this code evaluates the athlete BMI status weight

    def bmistatus(self):
        bmi = self.calcBMI()
        if bmi < 18.5:
            return ('\n *******ATHLETE IS UNDER WEIGHT******* \n')
        elif 18.5 <= bmi <= 25:
            return ('\n *******ATHLETE IS NORMAL WEIGHT******** \n')
        elif bmi > 25:
            return ('\n *******ATHLETE IS OVER WEIGHT******* \n')

    # this gets user input for athlete
    def userinput(self):
        self.name = str(input("Athlete name: "))
        self.age = float(input("Athlete age:"))
        self.gender = input("Athlete gender:")
        self.goal = input("Athlete goal (Bulking or Shredding):")
        self.weight = float(input("Athlete weight (lbs):"))
        self.height = float(input("Athlete height (inches):"))
        self.skill = input("Athlete skill(Beginner or Advanced):")

    # this code adds athlete to the roster
    def addAthlete(self, a_obj):
        if not isinstance(a_obj, Athlete):
            return False, "Athlete has NOT been added "
        else:
            self.roster.append(a_obj)
        return True, ("Athlete has been added")

    # gets weight and sets it for this specific Athlete
    def getWeight(self, weight):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight
        return True

    # gets height and sets it for this specific Athlete
    def getHeight(self, height):
        return self.height

    def setHeight(self, height):
        self.height = height
        return True

    def printSchedule(self):
        print('\n Clients and Rosters', self.name)
        for x in self.roster:
            print(x)

    def printWorkout(self):
        print('\n Clients Excercise', self.name)
        for x in self.workout:
            print(x)

    def printExcercise(Athlete, Excercise, Coach):

        print("Athlete's BMI")
        print(Athlete.calcBMI())
        print(Athlete.bmistatus())
        if Athlete.goal == 'bulking' or Athlete.goal == 'Bulking':
            print(" Your goal is Bulking so your best fit is Coach:")
            print("Coach name :", Coach.name)
            print("Coach age :", Coach.age)
            print("Coach email :", Coach.email)
            print("Coach gender :", Coach.gender)
            BA = open("advancedbulk.txt", "r")
            data = BA.read()
            BA.close()
            print(data)

        if Athlete.goal == 'shredding' or Athlete.goal == 'Shredding':
            print(" Your goal is Shredding so your best fit is Coach:")
            print("Coach name :", Coach.name)
            print("Coach age :", Coach.age)
            print("Coach email :", Coach.email)
            print("Coach gender :", Coach.gender)
            BA = open("advancedshred.txt", "r")
            data = BA.read()
            BA.close()
            print(data)

    def __str__(self):
        return ('\nName:' + str(self.name) + '\nAge:' + str(self.age) + '\nGender:' +
                str(self.gender) + '\nWeight:' + str(self.weight) + '\nHeight:' +
                str(self.height) + '\nPlan:' + str(self.goal) + '\nbmistatus:' + Athlete.bmistatus(self))


class Coach(Person):
    # Coach class subcalss of Person
    def __init__(self, name, age, gender, email, specialty):
        self.name = str(name)
        self.age = str(age)
        self.gender = str(gender)
        self.email = str(email)
        self.specialty = str(specialty)
        self.roster = []

    def addCoach(self, c_obj):
        if not isinstance(c_obj, Coach):
            return False, ("Coach has NOT been added")
        else:
            self.schedule.append(c_obj)
        return True, ("Coach has been added")

    # adds athlete to the roster
    def addAthlete(self, a_obj):
        if not isinstance(a_obj, Athlete):
            return False, "Atlete has NOT been added "
        else:
            print("\n\n")
            print("********Athlete has been added to the Coach Roster*******")
            self.roster.append(a_obj)
        return True, ("Athlete has been added")

    # prints roster of athletes for each coach
    def printRoster(self):
        print(self.name)
        for z in self.roster:
            print('\n ATHLETE INFO:')
            print(z)


class Excercise():
    # Excercise class
    def __intit__(self, skill, goal, plan_num, steps):
        self.skill = str(skill)
        self.goal = str(goal)
        self.plan_num = str(plan_num)
        self.steps = []


def main():
    print('\n***********WELCOME TO NPFITNESS Online GYM  ***********')
    anotherAthlete = True
    # print('\n Clients Created')
    c1 = Athlete('Christian Guzman', '24', 'Male', 200, 6.2, 'bulking', '1')
    e1 = Excercise()

    # print('\n Coaches Created')
    t1 = Coach('Frank Zane ', '30', 'Male', 'Fzane@npfitness.com', 'shredding')
    t3 = Coach('Jay Cutler ', '32', 'Male', 'jcutler@npfitness.com', 'bulking')
    print('\n******** COACH WILL BE ASSIGNED AFTER USER FILLS OUT THE FORM  **************')

    # this will continue to get info about athletes, and print their workout plans
    while anotherAthlete:
        c2 = Athlete()
        c2.userinput()
        if (c2.goal == 'bulking') or (c2.goal == 'Bulking'):
            Coach.addAthlete(t3, c2)
            Athlete.printExcercise(c2, e1, t3)
        if (c2.goal == 'shredding') or (c2.goal == 'Shredding'):
            Coach.addAthlete(t1, c2)
            Athlete.printExcercise(c2, e1, t1)
        anotherAthleteChoice = input("\n Add another athlete? (Yes/NO)")
        if anotherAthleteChoice == "Yes" or anotherAthleteChoice == "yes":
            anotherAthlete = True
        else:
            anotherAthlete = False
    # prints the total roster
    print("****TOTAL ROSTER LIST****")
    print("Coaches - ")
    t1.printRoster()
    t3.printRoster()


main()

