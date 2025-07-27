# tests/test_analyzer.py
from code_lingo.analyzer import analyze_code

def test_full_analysis(tmp_path):
    """
    Tests the analyze_code function with a sample file containing
    imports, a function, and a class with methods.
    
    The 'tmp_path' fixture provides a temporary directory unique to this test run.
    """
    # 1. Define sample Python code to be analyzed
    sample_code = """
import os
from collections import Counter

def top_level_function(arg1, arg2):
    pass

class MyTestClass:
    def __init__(self, name):
        self.name = name

    def public_method(self):
        pass

    def _internal_helper(self):
        # This should be ignored by the analyzer
        pass
"""
    
    # 2. Create a temporary file in the temp directory and write our code to it
    test_file = tmp_path / "test_module.py"
    test_file.write_text(sample_code, encoding="utf-8")

    # 3. Run the analyzer on our temporary file
    analysis_results = analyze_code(str(test_file))

    # 4. Define the expected outcome
    expected_results = {
        "imports": ["collections", "os"],
        "functions": [
            {"name": "top_level_function", "args": ["arg1", "arg2"]}
        ],
        "classes": {
            "MyTestClass": [
                {"name": "public_method", "args": ["self"]}
            ]
        }
    }

    # 5. Assert that the actual results match the expected results
    assert sorted(analysis_results["imports"]) == sorted(expected_results["imports"])
    assert analysis_results["functions"] == expected_results["functions"]
    assert analysis_results["classes"] == expected_results["classes"]