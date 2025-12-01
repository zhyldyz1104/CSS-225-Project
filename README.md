# CSS-225 Milestone 3 – Text-Based Adventure Game

This project is a text-based adventure game inspired by **The Alchemist** by Paulo Coelho.  
The story follows Santiago’s journey through interactive chapters, where player choices influence the outcome.  
All chapters are written as separate Python modules for clean, modular design and future expansion.

---

## 🧩 Project Structure

- `main.py` – Game entry point. Asks for username, manages chapter flow, handles restart logic.
- `globalvariables.py` – Stores shared game state (`username`, `success`) and the **Player Class object**.
- `chapter1.py` – Story begins in Andalusia. Player can talk to villagers, visit a gypsy, sell sheep, and depart.
- `chapter2.py` – Oasis exploration. Meet the Englishman, observe tribes, follow hawk flight.
- `chapter3.py` – Meet the oasis chieftain and the alchemist. Choose to accept guidance or hesitate.
- `chapter4.py` – Final chapter. Learn spiritual lessons, solve riddles, reach the Pyramids or restart on fail.

---

## 🚀 Architecture Overview

- Modular narrative split into chapters.
- Shared state stored globally.
- One main **Player class object** used to track player identity and stats safely across the game.

---

## 🕹️ How to Run the Game

### Requirements
- Python 3.10 or later
- Windows, macOS, or Linux
- Terminal or any Python IDE

### Run
```bash
python main.py
