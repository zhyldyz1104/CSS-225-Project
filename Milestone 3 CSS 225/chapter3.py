# ------------------------------------------------------------
# CHAPTER 3 MODULE
# This file contains the third chapter of the game story.
# Player interacts with the oasis chieftain and meets the alchemist.
# It includes story atmosphere, inner transformation challenge,
# and a choice that affects progress.
# The function play_chapter() runs all chapter 3 events
# and returns player flow back to Main.py.
# ------------------------------------------------------------

import globalvariables


# Prints the opening scene and sets chapter context
def start_chapter():
    print("Chapter 3 begins. You are summoned by the chieftain of the oasis.")  # chapter start narrative
    print("The air is heavy with incense and the weight of ancient decisions.")  # atmosphere setting


# Story event: meeting the oasis chieftain and getting mission
def summoned_by_chieftain():
    print("The chieftain speaks of omens and war, of trust and betrayal.")  # chieftain introduction
    print("He asks you to interpret the signs you've seen.")  # player task hint


# Story event: introduction to the alchemist character
def speak_with_alchemist():
    print("You meet the alchemist - a man cloaked in silence and fire.")  # alchemist encounter
    print("He speaks not in answers, but in riddles that stir your soul.")  # riddle-style dialogue


# Story reward: prints alchemist teaching acceptance scene
def accept_guidance():
    print("You accept the alchemist’s guidance.")  # branch reward text
    print("He teaches you that true transformation begins within.")  # internal growth message
    print("He hands you a flask of oil and says: 'Protect this as you would your heart.'")  # key item given


# Story branch: player hesitates and pauses progress
def delay_progress():
    print("You hesitate. Doubt clouds your path.")  # hesitation narrative
    print("The alchemist nods, understanding. 'Even the desert waits for those who listen.'")  # symbolic advice


# Story event: prints desert departure scene
def proceed_to_desert():
    print("You set out into the desert, the sun blazing and your heart steady.")  # departure narration
    print("The journey has begun - not just across the sands, but into yourself.")  # symbolic transition


# Flavor text for chapter closure
def end_chapter():
    print("Chapter 3 ends. The wind carries your name across the dunes.")  # ending narration


# Runs full Chapter 3 story sequence when imported into Main.py
def play_chapter():
    start_chapter()  # launch intro scene
    summoned_by_chieftain()  # chieftain story event
    speak_with_alchemist()  # alchemist encounter scene

    # Collects player's choice about accepting guidance
    choice = globalvariables.ask_yes_no_answer("Do you accept the alchemist’s guidance? (yes/no): ")

    # Story branching based on normalized answer
    if choice == "yes":
        accept_guidance()  # inner transformation reward
        proceed_to_desert()  # continues journey
    else:
        delay_progress()  # pauses progress if not accepted

    end_chapter()  # always runs final scene
