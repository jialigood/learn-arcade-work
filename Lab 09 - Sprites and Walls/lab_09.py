import arcade
number_true = "True"
number_false = "False"

# Setting the Variables
def opening_picture():

    arcade.open_window(1000, 1000, "Welcome to Quiz Time with John!")
    arcade.set_background_color(arcade.csscolor.GOLD)
    arcade.start_render()
    arcade.draw_text("Welcome to Quiz time with John!",  250, 600, arcade.csscolor.BLACK, 24)
    arcade.draw_text("Become a world champion if you score 15/15! Good luck!",  100, 500, arcade.csscolor.BLACK, 24)
    snowman()
def final_statement():

    total_score = 0
    # Print Final Statement
    # Score Percentage
    percentage_final = (total_score / 25) * 10
    print("Good Game, That was fun you should try again sometime! Wow you killed it, your final score is:", total_score)
    print("Your percentage is", percentage_final)
def snowman():

    # Draw snowman
    arcade.draw_circle_filled(645, 420, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(645, 480, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(645, 520, 20, arcade.color.WHITE)
    arcade.draw_line(615, 480, 590, 490, arcade.color.BLACK)
    arcade.draw_line(670, 480, 690, 490, arcade.color.BLACK)
    #Print Welcome Statement
def main():

    total_score = 0
    print("Welcome to the most impressive and dazzling quiz game you have ever seen! ")
    print("To answer the questions either enter True or False (Make sure its capitalized)! Good luck!")

    #Setting Input For Question 1
    answer = input("The Empire State Building is the tallest building in the world? ")
    if answer == number_false:
        print("Correct!")
        total_score += 1
        print("Your new score is", total_score)
    else:
        print("The correct answer is False, Better luck next time!")
        print("Your current score is:", total_score)



    #Setting Input For Question Two
    answer = input("Whale Songs are used to map out the ocean floor? ")
    if answer == number_true:
        print("Correct, Your killing it!")
        total_score += 1
        print("Your new score is", total_score)
    else:
        print("Im sorry, The correct answer is True")
        print("Your current score is:", total_score)
    print()



    #Setting Input For Question Three
    answer = input("The allies created a fake army to trick the Nazi's into believing the D-Day attack was elsewhere? ")
    if answer == number_true:
        print("Correct!")
        total_score += 1
        print("Your new score is", total_score)
    else:
        print("The correct answer is True.")
        print("Your current score is:", total_score)
    print()


    #Setting Input For Question Four
    answer = input("In 2014 a red bull stunt pilot single handedly hover his helicopter next to the ocean and got a bucket of water setting numerous helicopter world records? ")
    if answer == number_false:
        print("Correct!")
        total_score += 1
        print("Your new score is", total_score)
    else:
        print("The correct answer is False, So close! (Not really)")
        print("Your current score is:", total_score)
    print()

    # Setting Input For Question Five
    answer = input("The worlds entire population could fit inside Los Angeles? ")
    if answer == number_true:
        print("Correct!")
        total_score += 1
        print("Your new score is", total_score)
    else:
        print("The correct answer is True, Isnt that amazing!")
        print("Your current score is:", total_score)
    print()
    final_statement()




opening_picture()

arcade.finish_render()
arcade.run()

main()
