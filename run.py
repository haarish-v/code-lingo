# run.py
from code_lingo.analyzer import analyze_code
from code_lingo.reporter import Reporter

# The file we want to analyze
target_file = "sample.py"

# 1. Analyze the code to get the data dictionary
analysis_results = analyze_code(target_file)

# 2. Create a reporter instance with the results
reporter = Reporter(target_file, analysis_results)

# 3. Generate and print the beautiful report
report = reporter.generate_report()
print(report)