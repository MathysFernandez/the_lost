# the_lost

## 🚀 Project Home

Welcome to our project's wiki page!

This page serves as the central entry point for all essential information regarding **The Lost** project.

---

## 🔍 Project Overview

**The Lost** is a Pygame game where you explore a vast maze from a top-down perspective, featuring a safe central area inspired by *The Maze Runner* film.

Our goal is to deliver an **immersive and engaging experience** where every interaction and challenge brings you closer to finding your way out of this world.

Game development is streamlined thanks to the integration of a dedicated map editor (`Conceptor.py`).

---

## 📈 Project Architecture

* **`main.py`**: The main game file, containing the game loop with scenes for the menu, game, etc.
* **`Conceptor.py`**: A program for developers to modify the game map.
* **`Files/config.py`**: Configuration file for screen dimensions, title, etc.
* **`Files/textures_manager.py`**: Handles texture loading and scaling, as well as grid and collision data preparation.
* **`Files/Lecteur_map.py`**: Allows reading and modifying the JSON map file.
* **`Assets/`**: Contains all game assets (images, sounds, etc.).
* **`map/`**: Contains all game maps (JSON files).

---

## 🕹️ Game Controls

* **Z, Q, S, D** and **Arrow keys**: For movement.
* **SHIFT + Z/Q/S/D/Arrow keys**: For faster movement.

---

## ▶️ Quick Start

To clone the project, install dependencies, and run the game locally:

1.  **Clone this repository** in your bash terminal:
    ```bash
    git clone https://github.com/MathysFernandez/the_lost.git
    ```
2.  **Install dependencies**:
    * **Python** (the latest version)
    * **Pygame**: Use the command `pip install pygame`
3.  **Launch the game** with:
    ```bash
    main.py
    ```
4.  **Launch the editor mode** with:
    ```bash
    Conceptor.py
    ```

---

## 👤 Authors

Mathys Fernandez
