# Code Lingo 🗣️

> _Get the lay of the land of any Python file or project in seconds._

**Code Lingo** is a command-line tool that generates **human-readable summaries** of Python code. Whether you’re onboarding to a new codebase or revisiting old projects, Code Lingo helps you quickly understand the structure — so you can focus on what really matters: the logic.

---

## 🧠 The Problem

When working with unfamiliar Python code, it's tedious and time-consuming to manually open files just to see:

- What classes are defined?
- What public methods exist?
- What modules are imported?

**Code Lingo** automates this discovery process, giving you an instant summary of code structure using Python's `ast` module.

---

## ✨ Features

- 🔍 **Analyze Single Files or Entire Directories**  
  Point it to a file or folder — Code Lingo will do the rest.
  
- 📚 **Readable Summaries**  
  Clean breakdowns of imports, functions, classes, and public methods.

- 🚫 **Ignore Internals**  
  Internal helpers (like `_private_stuff`) are ignored by default to reduce noise.

- 🛠️ **AST-Powered**  
  Uses Python’s Abstract Syntax Tree (`ast`) for precise and reliable parsing.

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/haarish-v/code-lingo.git
   cd code-lingo
````

2. **Create and activate a virtual environment**

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate (Windows PowerShell)
   .\venv\Scripts\Activate.ps1

   # OR (macOS/Linux)
   source venv/bin/activate
   ```

3. **Install the package in editable mode**

   ```bash
   pip install -e .
   ```

   ✅ This will install `codelingo` as a command-line tool.

---

## 🚀 Usage

Once installed, you can run Code Lingo like this:

### ▶️ Analyze a single file

```bash
codelingo path/to/your/file.py
```

### 📂 Analyze a full directory

```bash
codelingo path/to/your/project/
```

---

## 📦 Example Output

```text
--- Code Lingo Report for: sample.py ---

Imports:
  - collections
  - os
  - sys

Functions:
  - top_level_function(param1, param2)

Classes:
  - MyAwesomeClass
    - public_method(self, value)

---------------------------------------------
```

---

## ✅ Running Tests

Code Lingo uses `pytest` for testing. To run tests:

1. Install `pytest` if not already:

   ```bash
   pip install pytest
   ```

2. From the root of the project, run:

   ```bash
   pytest
   ```

---

## 🔗 Links

* 👨‍💻 **Portfolio**: [haarish.in](https://haarish.in)
* 🧠 **LeetCode**: [Haarish\_v](https://leetcode.com/u/Haarish_v/)
* 💼 **LinkedIn**: [linkedin.com/in/haarishv](https://www.linkedin.com/in/haarishv/)

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for more information.

---

## 🙌 Contributions

Pull requests are welcome! If you have ideas to improve this tool or want to add features, feel free to fork and submit a PR.

---

```
