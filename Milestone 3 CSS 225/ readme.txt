CSS-225 Final Project – Adventure Game Technical Documentation
Author: Zhyldyz Torogulova
Course: CSS-225

------------------------------------------------------------
1. Where the code is hosted
------------------------------------------------------------

The source code for this project is hosted on GitHub:

Repository: <INSERT_GITHUB_REPO_URL_HERE>

The same version of the project (non-zipped) is available in this repository.
A zipped copy (including this readme.txt and all .py files) is uploaded to the course
assignment submission folder.

------------------------------------------------------------
2. External services
------------------------------------------------------------

This project does not use any external services, APIs, or databases.

- No web services
- No external libraries beyond the Python standard library

All input/output happens in the terminal/console.

------------------------------------------------------------
3. Languages and technologies
------------------------------------------------------------

- Programming language: Python 3.x
- Paradigm: Procedural and object-oriented (use of functions and at least one Class)
- Technologies:
  - Standard input/output via the terminal
  - Modular design using multiple Python files (modules)

------------------------------------------------------------
4. System requirements and supported applications
------------------------------------------------------------

Minimum requirements:

- Python 3.10 or later installed
- Operating System:
  - Windows, macOS, or Linux
- A terminal/command prompt, or an IDE that can run Python files:
  - For example: VS Code, PyCharm, Thonny, IDLE, etc.

No internet connection is required to run the game.

------------------------------------------------------------
5. Coding and naming conventions
------------------------------------------------------------

- File names:
  - main.py – main entry point of the game
  - globalvariables.py – shared global variables and helper functions
  - chapter1.py – Chapter 1 logic
  - chapter2.py – Chapter 2 logic
  - chapter3.py – Chapter 3 logic
  - chapter4.py – Chapter 4 logic
  - (Optional) Additional modules, such as a Player class file, follow the same pattern.

- Functions and variables:
  - snake_case naming (e.g., start_game, play_chapter, ask_yes_no_answer)
  - Boolean variables are named to indicate True/False state (e.g., success)
  - Global shared values (such as username) are stored in globalvariables.py

- Classes:
  - Class names use PascalCase (e.g., Player)

Inline comments are used within modules to describe the purpose of functions
and major sections of logic.

------------------------------------------------------------
6. How to run/build/deploy the program
------------------------------------------------------------

There is no build process required. The project is run directly with Python.

Steps to run:

1. Ensure all .py files are in the same directory:
   - main.py
   - globalvariables.py
   - chapter1.py
   - chapter2.py
   - chapter3.py
   - chapter4.py
   - (and any additional Class file, if used)

2. Open a terminal or command prompt in that directory.

3. Run the game with:

   python main.py

4. Follow the prompts displayed in the terminal.

There is no separate deployment process; the game is a local console application.

------------------------------------------------------------
7. Overview of the architecture
------------------------------------------------------------

High-level architecture:

- main.py
  - Entry point of the program.
  - Asks the user for a username.
  - Controls the flow between chapters.
  - Calls chapter1.play_chapter(), chapter2.play_chapter(), etc.
  - Handles restart logic if the final chapter signals failure (e.g., restarting from Chapter 1).

- globalvariables.py
  - Stores global shared state such as:
    - username
    - success (boolean value indicating if the game was completed successfully)
  - Contains helper functions such as:
    - ask_yes_no_answer(question): validates yes/no-like input and normalizes it to "yes" or "no".
  - (Optionally) may store a Player Class object that represents the current player.

- chapter1.py
  - Implements the first chapter of the story (Andalusia, villagers, gypsy, sheep).
  - Uses globalvariables.username for personalized dialogue.
  - Contains a play_chapter() function that runs all chapter 1 logic.

- chapter2.py
  - Implements the second chapter (oasis, Englishman, hawk).
  - Contains a play_chapter() function to run chapter 2 events.

- chapter3.py
  - Implements interaction with the chieftain and the alchemist.
  - Uses yes/no input (via ask_yes_no_answer) to decide if the player accepts guidance.
  - Contains a play_chapter() function.

- chapter4.py
  - Implements the final spiritual lessons and riddle challenge.
  - The solve_riddles() function returns True or False.
  - play_chapter() returns a boolean success value which is used by main.py to
    decide whether to restart the game.

Class usage (example, if implemented):

- Player (in globalvariables.py or a separate module):
  - Attributes:
    - name (username)
    - possible stats (e.g., gold, knowledge, progress)
  - Used to store and access player-related information in different chapters.

------------------------------------------------------------
8. How to start the program (start the game)
------------------------------------------------------------

To start the game:

1. Open a terminal in the project directory.
2. Run:

   python main.py

3. When prompted, enter your username.
4. Answer the questions (yes/no) to progress through the chapters.
   - The helper function normalizes inputs like "y", "yes", "yep", "ok" to "yes",
     and "n", "no", "nope" to "no", and re-prompts on invalid inputs.

If the player fails the final challenge in Chapter 4, the game will automatically
restart from Chapter 1, allowing replay and exploration of different choices.
