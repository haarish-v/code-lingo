# sample.py
import os
import sys
from collections import Counter

def top_level_function(param1, param2):
    """A simple function."""
    return param1 + param2

class MyAwesomeClass:
    def __init__(self, name):
        self.name = name

    def public_method(self, value):
        """A method available to everyone."""
        print(f"{self.name} says {value}")

    def _internal_helper(self):
        """This should be ignored by our analyzer."""
        pass