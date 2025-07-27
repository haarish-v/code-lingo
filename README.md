# Code Lingo 🗣️

A command-line tool that generates human-readable summaries of your Python code's structure. Get the "lay of the land" of any Python file or project in seconds.

---

## The Problem

When you dive into a new codebase or revisit an old project, you spend valuable time just figuring out the basic structure. What classes are in this file? What are its public methods? What does it import? Manually opening each file is tedious and inefficient.

**Code Lingo** solves this by instantly giving you a high-level overview, letting you focus on the logic that matters.

---

## Features

* **Analyze Single Files or Entire Directories**: Point `codelingo` at any Python file or project folder.
* **Clear, Readable Summaries**: Get a clean breakdown of imports, functions, and classes with their public methods.
* **Ignores Internals**: Automatically ignores "private" members (like `_internal_helper`) to keep the output focused on the public API.
* **Built with `ast`**: Uses Python's Abstract Syntax Tree for accurate and reliable code analysis.

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/haarish-v/code-lingo.git](https://github.com/haarish-v/code-lingo.git)
    cd code-lingo
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the venv
    python -m venv venv

    # Activate on Windows (PowerShell)
    .\venv\Scripts\Activate.ps1

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the package in editable mode:**
    ```bash
    pip install -e .
    ```
    This will make the `codelingo` command available in your terminal.

---

## Usage

Once installed, you can use the `codelingo` command.

**To analyze a single file:**
```bash
codelingo path/to/your/file.py