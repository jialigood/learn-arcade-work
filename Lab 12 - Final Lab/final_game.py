import arcade

def bubbles():
    arcade.draw_circle_outline(100, 180, 40, arcade.color.WHITE, 3)
    arcade.draw_circle_outline(300, 550, 40, arcade.color.WHITE, 3)
    arcade.draw_circle_outline(450, 200, 40, arcade.color.WHITE, 3)
    arcade.draw_circle_outline(540, 135, 40, arcade.color.WHITE, 3)
    arcade.draw_circle_outline(300, 270, 40, arcade.color.WHITE, 3)
    arcade.draw_circle_outline(80, 380, 40, arcade.color.WHITE, 3)
    arcade.draw_circle_outline(200, 80, 40, arcade.color.WHITE, 3)
    arcade.draw_circle_outline(550, 500, 40, arcade.color.WHITE, 3)

def welcome_window():
    arcade.open_window(600, 600, "drawing window")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()
    # decoration circles
    bubbles()
    # text
    arcade.draw_text("QUIZ TIME!", 90, 400, arcade.color.DARK_BLUE, 70)
    arcade.draw_text("QUIZ TIME!", 88, 402, arcade.color.WHITE, 70)
    arcade.draw_text("close this window to begin the game. good luck :)", 15, 360, arcade.color.WHITE, 23)
    arcade.draw_text("close this window to begin the game. good luck :)", 13, 361, arcade.color.DARK_BLUE, 23)

def quiz_time():
    for i in range(1):
        score = 0

        print("quiz game tbh")
        print()

        # question 1
        print("question 1: what is the square root of 16?")
        print("""A. 2
B. 5
C. 4
D. 1""")
        first_answer = input("your answer:")
        first_answer = first_answer.lstrip()
        if first_answer.lower() == "c":
            print("correct!")
            score += 1
            print("score: ", score)
        else:
            print("incorrect :(")
            print("answer was C. 4")
            print("score: ", score)
            print()

        # question 2
        print("question 2: what is the capital of new zealand?")
        print("""A. wellington
B. auckland
C. queenstown
D. dunedin""")
        second_answer = input("your answer:")
        second_answer = second_answer.lstrip()
        if second_answer.lower() == "a":
            print("correct!")
            score += 1
            print("score: ", score)
        else:
            print("incorrect :(")
            print("answer was A. wellington")
            print("score: ", score)
            print()

        # question 3
        print("question 3: what is your teacher's first name?")
        third_answer = input("your answer:")
        third_answer = third_answer.lstrip()
        if third_answer.lower() == "patricia":
            print("correct!")
            score += 1
            print("score: ", score)
        else:
            print("incorrect :(")
            print("answer was patricia")
            print("score: ", score)
            print()

        # question 4
        print("question 4: the sky is blue")
        print("true or false?")
        fourth_answer = input("your answer:")
        fourth_answer = fourth_answer.lstrip()
        if fourth_answer.lower() == "true":
            print("correct!")
            score += 1
            print("score: ", score)
        else:
            print("incorrect :(")
            print("answer was true")
            print("score: ", score)
        print()

        # question 5
        print("question 5: what city are you in?")
        print("""A. seattle
B. bellevue
C. renton
D. redmond""")
        fifth_answer = input("your answer:")
        fifth_answer = fifth_answer.lstrip()
        if fifth_answer.lower() == "d":
            print("correct!")
            score += 1
            print("score: ", score)
        else:
            print("incorrect :(")
            print("answer was true")
            print("score: ", score)
            print()

        percent = score / 5 * 100
        print("final score:", score, "/5, ", percent, "%")
        print()


        def closing_window():
            if percent == 100:
                # if you get 100%
                arcade.open_window(600, 600, "drawing window")
                arcade.set_background_color(arcade.color.LIGHT_PASTEL_PURPLE)
                arcade.start_render()
                # bubbles
                bubbles()
                # text
                arcade.draw_text("PERFECTLY DONE!", 20, 360, arcade.color.WHITE, 60)
                arcade.draw_text("PERFECTLY DONE!", 18, 361, arcade.color.ROYAL_PURPLE, 60)
                arcade.draw_text("you got 100%", 182, 300, arcade.color.WHITE, 34)
                arcade.draw_text("you got 100%", 180, 301, arcade.color.ROYAL_PURPLE, 34)

            else:
                # if you get less than 100%
                result = f"ALMOST THERE! you got {percent}%"
                arcade.open_window(600, 600, "drawing window")
                arcade.set_background_color(arcade.color.PISTACHIO)
                arcade.start_render()
                # bubbles again
                bubbles()
                # text
                arcade.draw_text(result, 20, 400, arcade.color.DARK_GREEN, 36)
                arcade.draw_text(result, 22, 402, arcade.color.WHITE, 36)
# call closing window function
        closing_window()
        def print_good_job():
            print("good job")

        # call print statements
        print_good_job()

# calling first window function
welcome_window()

arcade.finish_render()
arcade.run()

# calling main function
quiz_time()

# closing window
arcade.finish_render()
arcade.run()
