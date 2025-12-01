# ------------------------------------------------------------
# CHAPTER 4 MODULE
# This file contains the fourth and final chapter of the game.
# It continues the journey across the desert with the alchemist
# and includes personal transformation trials.
# Chapter includes:
#  - traveling in the desert,
#  - optional spiritual lessons,
#  - solving riddles that determine success,
#  - returning True/False to Main.py for game flow control.
# The function play_chapter() executes full chapter 4 logic
# and returns the result for integration safety.
# ------------------------------------------------------------

import globalvariables


# Prints the opening scene and sets Chapter 4 story context
def start_chapter():
    print("Chapter 4 begins. You travel with the alchemist across the vast desert.")  # chapter start narrative
    print("The wind whispers secrets, and the sun burns away illusions.")  # atmosphere narration


# Asks if player wants to learn spiritual lessons
def learn_spiritual_lessons():
    # Uses global yes/no validator to normalize input
    choice = globalvariables.ask_yes_no_answer("Do you want to learn spiritual lessons from the alchemist? (yes/no): ")

    # Story branch based on normalized answer
    if choice == "yes":
        print("You sit by the fire as the alchemist speaks of the Soul of the World...")  # spiritual branch
        print("You begin to understand that everything is connected.")  # connection message
    else:
        print("You choose to continue without spiritual guidance.")  # skip branch
        print("The desert feels colder, and the silence heavier.")  # atmosphere consequence


# Riddle-solving trial
def solve_riddles():
    # Uses global yes/no validator to normalize input
    choice = globalvariables.ask_yes_no_answer("Do you want to solve the alchemist’s riddles? (yes/no): ")

    # Game branching based on normalized answer
    if choice == "yes":
        print("You ponder the riddles, each one revealing a deeper truth.")  # riddle success narration
        print("Wisdom flows through you like desert wind.")  # wisdom scene
        print("You reach the Pyramids. 🏜️✨ Congratulations — you have arrived at your destiny!")  # mission success
        return True  # chapter success
    else:
        print("You struggle to understand. The path fades.")  # failure narration
        print("You must retry... Returning to the beginning of the game.")  # consequence
        return False  # chapter failed


# Runs full Chapter 4 sequence
def play_chapter():
    start_chapter()  # launch opening scene
    learn_spiritual_lessons()  # optional guidance branch runs
    success = solve_riddles()  # riddle trial determines success
    return success  # returns boolean result to Main.py
