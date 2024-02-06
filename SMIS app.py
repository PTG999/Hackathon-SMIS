import time
import random
logins=["pkalra"]
print("welcome to SMIS, the Screen Managment Intelligence System","\n")
time.sleep(2)

def timer():
    print("\n")
    print("Welcome to the screen time timer")
    time.sleep(0.7)
    print("the purpose of this is for you to take a break after the timer ends","\n")
    time.sleep(1)
    print("would you like to set a personal timer, or can we suggest you one 'p for personal and s for suggestion'")
    while True:
        timer=input()
        if timer=="p":
            print("enter the number of minutes you want for your timer")
            seconds=int(input())
            print("setting timer")
            for n in range(3,1,-1):
                time.sleep(1)
                print(n)
                n=n-1
            time.sleep(1)
            print("STAAAART!")
            time.sleep(seconds*60)
            print("TIME IS UP!")
            break
        elif timer=="s":
            seconds=random.randint(20,40)
            print("you got",seconds,"minutes!")
            print("setting timer")
            for n in range(3,1,-1):
                time.sleep(1)
                print(n)
                n=n-1
            time.sleep(1)
            print("STAAAART!")
            time.sleep(seconds*60)
            print("TIME IS UP!")
            break
        else:
            print("sorry I cannot understand")
            time.sleep()
            print("enter again")

def suggestions():
    print("Great Choice!")
    time.sleep(0.5)
    print("here we give suggestion on what you can do instead of watching a screen!","\n")
    time.sleep(1)
    f=open("suggestions.txt","r")
    a=f.read()
    b=a.split("\n")
    for i in range(0,10):
        print(b[i])
        time.sleep(1)
    print("\n")
    print("would you like more suggestions? 'y for yes and n for no")
    while True:
        more=input()
        if more=="y":
            for i in range(10,20):
                print(b[i])
                time.sleep(1)
            break
        elif more=="n":
            print("Hope you find what you needed!")
            break
        else:
            print("sorry I did not understand")

def end_program():
    print("Thank you for visiting my app, please come again")

def home_page():
    run_again = True
    while run_again:
        print("Welcome to the HomePage")
        print("which app feature would you like to acccess")
        time.sleep(2)
        print("\n")
        features=["1.ScreenTime Timer","2.Redcuing Screen Time Limit","3.exit"]
        time.sleep(0.3)
        for n in features:
            print(n)
            time.sleep(.7)
        inner_run = True
        while inner_run:
            num = input()
            if num == "1":
                timer()
                inner_run = False
            elif num == "2":
                suggestions()
                inner_run = False
            elif num == "3":
                end_program()
                run_again = False
                inner_run = False
            else:
                print("try again")

def new():
    print("time to generate your username!")
    print("give me your first and last name")
    name=input()
    first,last=name.split()
    user=first[0]+last
    return(user)

def login():
    while True:
        time.sleep(0.7)
        print("give me your username")
        usr=input()
        if usr in logins:
            a=usr
            return(a)
            break
        else:
            print("sorry wrong username or create an account")

def login_page():
    print("Great! Now let's login. Are you a New user or Old user.'n' for new and 'o' for old.")
    while True:
        user=input()
        if user=="n":
            final=new()
            print("generating username")
            for n in range(1,4):
                time.sleep(1)
                print(".")
            print("username :",final)
            logins.append(final)
            time.sleep(0.7)
            print("now let's login...")
            time.sleep(0.3)
            final=login()
            print("loading")
            for n in range(1,4):
                time.sleep(1)
                print(".")
            print("welcome,", final)
            break
        elif user=="o":
            final=login()
            print("loading")
            for n in range(1,4):
                time.sleep(1)
                print(".")
            print("welcome,", final)
            break
        else:
            print("sorry I did not understand")
            time.sleep(.7)
            print("please enter again...")
    time.sleep(1)
    home_page()

login_page()