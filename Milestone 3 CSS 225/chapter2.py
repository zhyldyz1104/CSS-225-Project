# ------------------------------------------------------------
# CHAPTER 2 MODULE
# This file contains the second chapter of the game story.
# It shows the player's arrival at the oasis and key story events.
# Chapter includes:
#  - meeting and helping the Englishman,
#  - exploring the oasis atmosphere,
#  - following the hawk as a sign,
#  - moving the story toward the alchemist.
# The function play_chapter() runs all Chapter 2 events
# and is called from Main.py.
# ------------------------------------------------------------


# Prints the opening scene of Chapter 2 (flavor text)
def start_chapter():
    print("Chapter 2 begins. You arrive at the oasis, the air shimmering with heat and mystery.")  # chapter start scene


# Automatic story event: meeting Englishman and offering help
def help_englishman():
    print("You meet an Englishman searching for the secrets of alchemy.")  # englishman introduction
    print("He asks for your help in finding the alchemist.")  # player mission hint


# Flavor text for exploration of the oasis environment
def explore_oasis():
    print("You explore the oasis, passing palm trees and listening to the quiet hum of desert life.")  # location atmosphere
    print("You notice tribes gathering, and a sense of tension in the air.")  # story tension build-up


# Story event for spotting and following hawk flight as a sign
def follow_hawk_flight():
    print("You spot a hawk circling above.")  # hawk visual cue
    print("Its flight seems to trace a hidden path - perhaps a sign, an omen.")  # omen message
    print("You follow it, feeling the desert whisper its secrets.")  # symbolic action


# Prints the chapter conclusion line (flavor text)
def end_chapter():
    print("Chapter 2 ends. You feel closer to your Personal Legend, but the desert still holds many mysteries.")  # chapter end scene


# Runs full Chapter 2 story sequence when called from Main.py
def play_chapter():
    start_chapter()       # launches chapter opening
    help_englishman()     # runs Englishman story event
    explore_oasis()       # runs oasis exploration narration
    follow_hawk_flight()  # runs hawk-following omen sequence
    end_chapter()         # launches final scene of chapter 2
