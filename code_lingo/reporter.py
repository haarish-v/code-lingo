# code_lingo/reporter.py
import os

class Reporter:
    """Formats the analysis data into a human-readable report."""

    def __init__(self, filepath: str, analysis_data: dict):
        # We use os.path.basename to get just the filename from a full path
        self.filename = os.path.basename(filepath)
        self.data = analysis_data
        self.report_lines = []

    def _format_section(self, title: str, items: list, formatter):
        """Helper to format a generic section to avoid repeating code."""
        if not items:
            return
        
        self.report_lines.append(f"\n{title}:")
        for item in items:
            self.report_lines.append(formatter(item))

    def _format_imports(self):
        imports = self.data.get("imports", [])
        self._format_section("Imports", imports, lambda imp: f"  - {imp}")

    def _format_functions(self):
        functions = self.data.get("functions", [])
        def formatter(func):
            args = ", ".join(func['args'])
            return f"  - {func['name']}({args})"
        self._format_section("Functions", functions, formatter)

    def _format_classes(self):
        classes = self.data.get("classes", {})
        if not classes:
            return

        self.report_lines.append("\nClasses:")
        for class_name, methods in classes.items():
            self.report_lines.append(f"  - {class_name}")
            if methods:
                for method in methods:
                    args = ", ".join(method['args'])
                    self.report_lines.append(f"    - {method['name']}({args})")
            else:
                self.report_lines.append("    (No public methods found)")

    def generate_report(self) -> str:
        """Generates the full text report by calling the formatters."""
        self.report_lines.append(f"--- Code Lingo Report for: {self.filename} ---")
        
        self._format_imports()
        self._format_functions()
        self._format_classes()
        
        self.report_lines.append("\n" + ("-" * 45))

        return "\n".join(self.report_lines)