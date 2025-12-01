# ------------------------------------------------------------
# CHAPTER 1 MODULE
# This module handles story interactions set in Andalusia.
# It retrieves the global username and success state from
# globalvariables.py and uses the global ask_yes_no_answer()
# for input handling to support story branching.
# ------------------------------------------------------------

import globalvariables


# Prints the opening location scene of Chapter 1 (story flavor only)
def start_game():
    print("Player starts in Andalusian village.")  # opening scene output


# Asks player if they want to talk to villagers.
# Uses the global validator and converts result into boolean for flow control.
def talk_to_villagers():
    talk = globalvariables.ask_yes_no_answer(
        f"{globalvariables.username},Do you want to talk to villagers? "
    )  # collects validated answer

    if talk == "yes":
        print("Talking to villagers...")  # narration if yes
        talk = True   # convert to boolean
    else:
        print("Continue")  # narration if no or skip
        talk = False  # convert to boolean

    return talk  # returns True or False to play_chapter()


# Automatic story reward printed after talking to villagers (no input)
def gain_knowledge_of_omens():
    print("Gained knowledge of omens.")  # reward narration


# Asks player if they want to visit the gypsy and returns boolean result
def visit_gypsy():
    visit = globalvariables.ask_yes_no_answer("Do you wanna visit gypsy? ")  # collects validated input

    if visit == "yes":
        print("Visiting gypsy...")  # narration if yes
        visit = True
    else:
        print("Continue")  # narration if skipped
        visit = False

    return visit  # returns True/False for story branching


# Prints prophecy narration (only story output, no return value)
def receive_prophecy():
    print(f"{globalvariables.username},Received prophecy about treasure.")  # prophecy scene


# Asks player if they want to sell sheep and returns boolean result
def sell_sheep():
    sell = globalvariables.ask_yes_no_answer(
        f"{globalvariables.username},Do you wanna sell sheep? "
    )  # collects validated answer

    if sell == "yes":
        print("Selling sheep...")  # narration if yes
        sell = True
    else:
        print("Continue")  # narration if no
        sell = False

    return sell  # return boolean state to chapter flow


# Prints player gold gained narration after selling sheep (no input)
def gain_gold():
    print("Gained gold from selling sheep.")  # reward scene, no return


# Prints Chapter 1 closing scene, always runs (no input, no return)
def depart_for_desert():
    print("Departing for the desert... End of Chapter 1.")  # chapter conclusion


# Executes full Chapter 1 story and connects the choices to events.
# Called from Main.py.
def play_chapter():
    print(f"{globalvariables.username}, you are a simple shepherd boy in Andalusia.")  # introduction narration
    print("You dream of something more — a treasure, a journey, a destiny.")  # motivation line
    print("Your story begins in a quiet village surrounded by hills and sheep.")  # start context

    # Branch 1: Talk to villagers → reward knowledge
    if talk_to_villagers():
        gain_knowledge_of_omens()  # triggers omens knowledge scene

    # Branch 2: Visit the gypsy → prophecy scene
    if visit_gypsy():
        receive_prophecy()  # prints prophecy narration

    # Branch 3: Sell sheep → earn gold
    if sell_sheep():
        gain_gold()  # prints gold gain narration

    # Final mandatory Chapter 1 event: depart to desert
    depart_for_desert()  # moves game to next milestone chapter
