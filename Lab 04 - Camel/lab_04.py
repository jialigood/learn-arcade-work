import random

def main():
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    alien_distance = -20
    canteen_drinks = 3

    print("""welcome to my camel game
run away from the aliens (being politically correct)
they want the camel cuz it looks funny.
run away sis!!!!
""")
    user_done = False
    while not user_done:
        # random numbers variables
        alien_rand = random.randrange(7, 14)
        full_speed_rand = random.randrange(10, 20)
        tiredness_rand = random.randrange(1, 3)
        moderate_rand = random.randrange(5, 12)

        print("""
A. Drink from your canteen
B. Ahead moderate speed
C. Ahead full speed
D. Stop for the night
E. Status check
Q. Quit
""")
        user_choice = input("what is your choice?")
        user_choice = user_choice.lstrip()

        if user_choice.upper() == "Q":
            user_done = True

        elif user_choice.upper() == "E":
            print("")
            print("miles traveled: ", miles_traveled)
            print("drinks in canteen: ", canteen_drinks)
            print("The aliens are ", miles_traveled - alien_distance, " miles behind you!")
            print("")

        elif user_choice.upper() == "D":
            camel_tiredness = 0
            print("")
            print("the camel is happy af")
            print("")
            alien_distance += alien_rand

        elif user_choice.upper() == "C":
            miles_traveled += full_speed_rand
            thirst += 1
            camel_tiredness += tiredness_rand
            alien_distance += alien_rand
# random oasis chance
            for i in range(1):
                if random.randrange(20) == 0:
                    print("YOU FOUND AN OASIS!!!")
                    camel_tiredness = 0
                    canteen_drinks = 3
                    thirst = 0

        elif user_choice.upper() == "B":
            miles_traveled += moderate_rand
            thirst += 1
            camel_tiredness += 1
            alien_distance += alien_rand
# random oasis chance
            for i in range(1):
                if random.randrange(20) == 0:
                    print("YOU FOUND AN OASIS!!!")
                    camel_tiredness = 0
                    canteen_drinks = 3
                    thirst = 0

        elif user_choice.upper() == "A":
            if canteen_drinks > 0:
                thirst -= 1
                canteen_drinks -= 1
            else:
                print("no drinks left! whoops.")

        if thirst > 4 and thirst < 7:
            print("""
            you are thirsty
            """)

        if thirst > 6:
            print("""
            you have died of thirst
            GAME OVER
            """)
            user_done = True

        if camel_tiredness > 6 and camel_tiredness < 8 and not user_done:
            print("""
            camel is tired yall!
            """)

        if camel_tiredness > 8:
            print("""
            YOU KILLED YOUR CAMEL OMFG
            GAME OVER
            """)
            user_done = True

        if miles_traveled - alien_distance < 15 and not user_done:
            print("""
             the aliens are getting close
             """)

        if miles_traveled - alien_distance < 1 and not user_done:
            print("""
            the aliens caught up!
            GAME OVER""")
            user_done = True

        if miles_traveled >= 200 and not user_done:
            print("""
            YOU WON!!! GOOD JOB
            """)
            user_done = True

    print("""
thanks for playing""")

main()
