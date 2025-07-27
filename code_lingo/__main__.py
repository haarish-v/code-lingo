# code_lingo/__main__.py
import argparse
import os
from .analyzer import analyze_code
from .reporter import Reporter

def main():
    """
    The main entry point for the command-line tool.
    """
    parser = argparse.ArgumentParser(
        description="Code Lingo: A tool to generate human-readable summaries of Python code."
    )
    
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="The path to the Python file or directory to analyze. Defaults to the current directory."
    )

    args = parser.parse_args()
    target_path = args.path

    # Case 1: The path is a single Python file
    if os.path.isfile(target_path) and target_path.endswith(".py"):
        try:
            analysis_results = analyze_code(target_path)
            reporter = Reporter(target_path, analysis_results)
            report = reporter.generate_report()
            print(report)
        except Exception as e:
            print(f"Error processing file {target_path}: {e}")

    # Case 2: The path is a directory
    elif os.path.isdir(target_path):
        python_files = []
        # os.walk recursively finds all files in a directory tree
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(".py"):
                    # Create the full path to the file and add it to our list
                    full_path = os.path.join(root, file)
                    python_files.append(full_path)
        
        if not python_files:
            print(f"No Python files found in '{target_path}'.")
            return

        print(f"Found {len(python_files)} Python file(s). Analyzing...\n")

        # Analyze and report on each file found
        for filepath in python_files:
            try:
                analysis_results = analyze_code(filepath)
                reporter = Reporter(filepath, analysis_results)
                report = reporter.generate_report()
                print(report)
            except Exception as e:
                print(f"Error processing file {filepath}: {e}\n")

    # Case 3: The path is invalid
    else:
        print(f"Error: Path '{target_path}' is not a valid Python file or directory.")


if __name__ == "__main__":
    main()