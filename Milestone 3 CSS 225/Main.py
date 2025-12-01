import chapter1, chapter2, chapter3, chapter4, globalvariables


# GAME STARTER SCRIPT
# This file manages the start and flow of the game.
# It asks for the username, starts chapters one by one, and saves
# global variables like username and chapter results.
# The script ensures tests only run when this file is executed directly.
# Zhyldyz Torogulova 11/30/25

def start_game():
    globalvariables.username = input("Please enter your username: ")

    # Create Player object using the username (Class usage)
    globalvariables.player = globalvariables.Player(globalvariables.username)

    # Asks user permission to start the game
    start_new_chapter = globalvariables.ask_yes_no_answer(
        f"{globalvariables.username}, do you wanna start a game? (y/n): "
    )
    if start_new_chapter:
        chapter1.play_chapter()
    else:
        print("Thank you! Bye!")
        return  # Stops the game after getting "No"

    # Asks permission to start Chapter 2
    start_new_chapter = globalvariables.ask_yes_no_answer(
        "Congrats on completing the chapter! Do you want to start Chapter 2? (y/n): "
    )
    if start_new_chapter:
        chapter2.play_chapter()
    else:
        print("Thank you! Bye!")
        return  # Ends flow if No

    # Asks permission to start Chapter 3
    start_new_chapter = globalvariables.ask_yes_no_answer(
        "Congrats on completing the chapter! Do you want to start Chapter 3? (y/n): "
    )
    if start_new_chapter:
        chapter3.play_chapter()  # Launches Chapter 3
    else:
        print("Thank you! Bye!")
        return

    # Asks permission to start Chapter 4
    start_new_chapter = globalvariables.ask_yes_no_answer(
        "Congrats on completing the chapter! Do you want to start Chapter 4? (y/n): "
    )
    if start_new_chapter:
        globalvariables.success = chapter4.play_chapter()  # Saves Chapter 4 result
    else:
        print("Thank you! Bye!")
        return

    # If Chapter 4 failed, restart the game from Chapter 1
    if not globalvariables.success:
        print("\nRestarting from Chapter 1...\n")
        start_game()  # Starting the game from the very beginning


# Runs only when this file is executed directly (not imported)
if __name__ == "__main__":
    start_game()
