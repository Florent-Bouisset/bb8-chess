# Bishop B-8 Chess ♗

Bishop B-8 is a fun project to build a **UCI chess engine** — that is, a command-line chess bot capable of playing full games of chess by responding to [UCI protocol](https://en.wikipedia.org/wiki/Universal_Chess_Interface) commands.

The goal of this project is **not** to create a graphical chess interface — only to build a working and evolving chess engine that can play games with logic ranging from random moves to more strategic decision-making.

## 🧠 What is UCI?

UCI stands for **Universal Chess Interface** — it’s a protocol used by many chess engines and GUIs to communicate in a standard way. This means you can plug your bot into any GUI that supports UCI engines.

For more info and a list of compatible GUIs, see the Stockfish documentation:  
👉 https://official-stockfish.github.io/docs/stockfish-wiki/Download-and-usage.html#download-a-chess-gui

Personally, I use the GUI **[En Croissant](https://github.com/franciscoBSalgueiro/en-croissant)**.

---

## 🐍 Made with Python

This engine is built in **Python**, using:

- [`python-chess`](https://python-chess.readthedocs.io/) – for chess logic and position handling.
- My own engine logic – starting from random move selection, then evolving into smarter strategies.
- The [UCI protocol](https://en.wikipedia.org/wiki/Universal_Chess_Interface) for communication with GUIs or other engines.

---

## 🚀 Getting Started

### 1. Prerequisites

- **Python 3.9+** installed 
- **Poetry** (a dependency and environment manager for Python)

Install Poetry if not already installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or via Homebrew:

```bash
brew install poetry
```

### 2. Installation
Clone the repo and set up the environment:

```
git clone https://github.com/yourname/bishop-b8-chess.git
cd bishop-b8-chess

poetry install
```

This installs all dependencies in an isolated virtual environment.

### 3. Running the Engine (Dev Mode)
To run your engine from the command line (interacting via UCI):

```
poetry run dev
```

### 4. Build a Standalone Binary
Create a single executable binary for distribution:

```
poetry run build_binary
```
The output binary will be in the dist/ folder, which you can use with any UCI-compatible chess GUI.


---

## 🗃 Logging

When run in debug mode, all communication (UCI input/output) is saved in the `logs/` directory.  
This is useful for reviewing what happened between your engine and the GUI.

---

## 🧠 Goals & Roadmap


✅ UCI-compatible bot

✅ Random-move engine

✅ Proper logging

⬜ Greedy material-based evaluation

⬜ Positional heuristics

⬜ Elo benchmarking against weaker Stockfish versions