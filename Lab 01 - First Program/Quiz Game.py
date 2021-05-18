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

print("final score: ", score)
print("good job ig")

