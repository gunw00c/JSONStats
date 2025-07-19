import keyword
import re
from .StatsList import StatsList

class load:
    class JSONList:
        def __init__(self, items):
            self.items = [load(item) for item in items]
        
        def values(self):
            return [item.values() for item in self.items]
        
        def __str__(self):
            items = [str(item) for item in self.items]
            return f"[{','.join(items)}]"

        def __getattr__(self, name):
            # Collect the specified attribute from each item in the list and return as StatsList
            try:
                return StatsList([getattr(item, name).values() for item in self.items])
            except AttributeError:
                raise AttributeError(f"'{name}' not found in one or more items")

    class JSONValue:
        def __init__(self, value):
            self.value = value
        
        def values(self):
            return self.value
        
        def __str__(self):
            if isinstance(self.value, (str, bool, type(None))):
                return repr(self.value)
            return str(self.value)

    class JSONDictionary:
        def __init__(self, data):
            for key, value in data.items():
                safe_key = re.sub(r'[^a-zA-Z0-9_]', '_', key)
                if keyword.iskeyword(safe_key) or safe_key[0].isdigit():
                    safe_key = f"_{safe_key}"
                setattr(self, safe_key, load(value))
        
        def values(self):
            return {key: getattr(self, key).values() for key in vars(self)}
        
        def __str__(self):
            items = [f"{repr(key)}:{str(getattr(self, key))}" for key in vars(self)]
            return f"{{{','.join(items)}}}"

    def __init__(self, data):
        if isinstance(data, dict):
            self._value = load.JSONDictionary(data)
        elif isinstance(data, list):
            self._value = load.JSONList(data)
        else:
            self._value = load.JSONValue(data)

    def values(self):
        return self._value.values()

    def __str__(self):
        return str(self._value)

    def __getattr__(self, name):
        return getattr(self._value, name)

    def jump(self):
        """Returns a load object wrapping a list of values from a top-level dictionary, ignoring keys."""
        if isinstance(self._value, load.JSONDictionary):
            values = [getattr(self._value, key).values() for key in vars(self._value)]
            return load(values)
        raise ValueError("jump() can only be called on a load object wrapping a dictionary")
