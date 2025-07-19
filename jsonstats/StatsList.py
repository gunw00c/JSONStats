import statistics
from statistics import *

class StatsList(list):
    def __getattr__(self, name):
        # Handle statistical methods from the statistics module
        if hasattr(statistics, name):
            return lambda: getattr(statistics, name)(self)
        # Handle attribute access for dictionary keys
        if all(isinstance(item, dict) for item in self):
            if all(name in item for item in self):
                return StatsList([item[name] for item in self])
        raise AttributeError(f"'{name}' not found in statistics module or dictionary keys")

    def __getitem__(self, key):
        # Handle dictionary-style indexing for dictionary keys
        if all(isinstance(item, dict) for item in self):
            if all(key in item for item in self):
                return StatsList([item[key] for item in self])
            raise KeyError(f"Key '{key}' not found in all dictionaries")
        raise TypeError(f"Cannot index with '{key}' on StatsList containing non-dictionaries")
