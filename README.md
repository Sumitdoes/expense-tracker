# Expense Tracker CLI

A command-line tool to log, categorize, and analyze personal spending — built while learning Python fundamentals through a real, deployed project instead of isolated tutorials.

## Features
- Add expenses with item, category, and amount
- Input validation (rejects non-numeric amounts, empty fields)
- Per-entry spending alerts when a single expense exceeds ₹10,000
- Persistent storage — data survives across sessions via JSON
- Category-wise spending breakdown
- Handles corrupted/missing data files without crashing

## What I Learned
- File I/O and JSON serialization for persistent data
- Input validation loops and error handling with try/except
- Debugging: the difference between a set `{}` and a dict `{}`, and why it silently breaks downstream code
- Reading tracebacks and terminal output carefully before assuming code is broken

## How to Run
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
python main.py
```

## Built With
- Python 3.14
- `json` for storage (no external dependencies yet)
