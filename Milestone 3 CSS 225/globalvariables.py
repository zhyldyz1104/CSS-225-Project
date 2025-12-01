success = True  # to control the game so we can retry in some cases
username = ""

# ------------------------------------------------------------
# PLAYER CLASS
# This class stores player data such as username, gold,
# knowledge, and chapter progress. It will be used globally
# in Main.py and all chapters.
# ------------------------------------------------------------
class Player:
    def __init__(self, username):
        self.username = username  # Player name
        self.gold = 0            # Player gold balance
        self.knowledge = False   # Omens knowledge state
        self.current_chapter = 1 # Chapter tracker


# глобальный объект игрока (пока пустой, main.py его создаст)
player = None


def ask_yes_no_answer(question: str) -> str:
    while True:
        ans = input(question).strip().lower()
        if ans in ["y", "yes", "yep", "ok", "yeah", "yea", "sure", "yup", "yess", "yepp", "yup", "yeahh"]:
            return "yes"
        if ans in ["n", "no", "nope", "nah", "nooo", "nop", "nopeee"]:
            return "no"
        print("❗ Please write yes or no!")
