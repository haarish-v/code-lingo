# 🚀 Code Lingo — Understand Your Code Instantly

> A sleek command-line tool that generates **human-readable summaries** of Python codebases using Python’s built-in `ast` module.

---

## 📌 Overview

When diving into unfamiliar Python code, the first challenge is understanding the structure — what classes exist, which functions are defined, and what the file imports. Manually navigating each file is inefficient.

**Code Lingo** eliminates this friction by producing a high-level summary of any Python file or project folder in seconds.

---

## ✨ Features

- 🔍 **Single File or Full Directory Support** — Analyze individual files or entire project folders with ease.
- 📑 **Readable Summaries** — Clearly lists imports, top-level functions, and public class methods.
- 🚫 **Noise-Free Output** — Skips private functions and internal helpers (like `_hidden_function`) to keep results clean.
- 🛠 **Accurate Parsing with `ast`** — Leverages Python’s Abstract Syntax Tree for reliable and extensible code analysis.

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/haarish-v/code-lingo.git
cd code-lingo
```

2. **Create and activate a virtual environment**

```bash
# Create the venv
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (macOS/Linux)
source venv/bin/activate
```

3. **Install the package in editable mode**

```bash
pip install -e .
```

✅ This installs `codelingo` as a terminal command.

---

## 🚀 Usage

### 📂 Analyze a single file

```bash
codelingo path/to/your/file.py
```

### 🗂 Analyze an entire directory

```bash
codelingo path/to/your/project/
```

---

## 🧪 Example Output

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

To run unit tests with `pytest`:

1. Install dependencies (if not already):

```bash
pip install pytest
```

2. Run tests from the project root:

```bash
pytest
```

---

## 📄 License

**MIT License** — See the [LICENSE](./LICENSE) file for details.

---

## 🔗 Links

- 🧠 LeetCode: [Haarish_v](https://leetcode.com/u/Haarish_v/)
- 👨‍💼 LinkedIn: [linkedin.com/in/haarishv](https://www.linkedin.com/in/haarishv/)
- 🌐 Portfolio: [haarish.in](https://haarish.in)

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork this repo and submit a pull request.

---
