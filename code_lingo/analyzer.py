# code_lingo/analyzer.py
import ast

class CodeAnalyzer(ast.NodeVisitor):
    """
    This class walks through the Abstract Syntax Tree of Python code
    and collects statistics about classes, functions, and imports.
    """
    def __init__(self):
        self.stats = {
            "imports": set(),
            "functions": [],
            "classes": {}
        }

    def visit_Import(self, node):
        """Called when an 'import foo' statement is found."""
        for alias in node.names:
            self.stats["imports"].add(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        """Called when a 'from foo import bar' statement is found."""
        if node.module:
            self.stats["imports"].add(node.module)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        """Called when a function definition is found."""
        # We ignore functions starting with '_' to hide private/internal details.
        if not node.name.startswith('_'):
            args = [arg.arg for arg in node.args.args]
            self.stats["functions"].append({"name": node.name, "args": args})
        # Don't visit children of a function, as we don't want to find nested functions.

    def visit_ClassDef(self, node):
        """Called when a class definition is found."""
        if not node.name.startswith('_'):
            methods = []
            # Look at the children nodes of the class
            for item in node.body:
                # We only care about function definitions (methods) inside the class
                if isinstance(item, ast.FunctionDef):
                    # And we ignore private methods
                    if not item.name.startswith('_'):
                        method_args = [arg.arg for arg in item.args.args]
                        methods.append({"name": item.name, "args": method_args})
            self.stats["classes"][node.name] = methods
        # We handled the children, so no need to call generic_visit.

def analyze_code(filepath: str) -> dict:
    """
    Reads a Python file, parses it into an AST, and returns a structured summary.
    
    Args:
        filepath: The path to the Python file.

    Returns:
        A dictionary containing the analysis results.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        source_code = f.read()
    
    tree = ast.parse(source_code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    
    # Convert set of imports to a sorted list for consistent output
    analyzer.stats["imports"] = sorted(list(analyzer.stats["imports"]))
    
    return analyzer.stats