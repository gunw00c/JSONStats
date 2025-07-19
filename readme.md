# json stats

The `json stats` package provides a Python class for wrapping JSON-like data (dictionaries, lists, and primitive values) into objects that support attribute-style access (e.g., `obj.key` instead of `obj['key']`). It includes a `jump` function to extract dictionary values as a list and integrates with the `StatsList` class for statistical operations on lists of values.

## Features
- **Attribute Access**: Access dictionary keys as attributes (e.g., `json_obj.name` for `{"name": "value"}`).
- **Jump Function**: Extract values from a top-level dictionary into a `Json` object wrapping a list (e.g., `json_obj.jump()`).
- **Statistical Operations**: Use `StatsList` to perform statistical calculations (e.g., `json_obj.jump().age.mean()`) on lists of values.
- **Safe Key Handling**: Automatically converts invalid dictionary keys (e.g., containing spaces or reserved keywords) into valid Python attribute names.
- **Compact Serialization**: Convert objects back to native Python dictionaries/lists/values with `values()` or get a compact string representation with `str()`.

## Installation
The `json stats` package is distributed as a Python package named `jsonstats`, which includes the `Json` and `StatsList` classes. It requires Python 3.7 or later and has no external dependencies beyond the Python standard library.

### Option 1: Copy the Package
1. **Download the `jsonstats` Folder**:
   - Copy the `jsonstats` folder (containing `__init__.py` and `json.py`) into your project directory or your Python environment’s `site-packages` directory.
   - Alternatively, clone the repository (if hosted) or download from the package source.

2. **Verify Python Version**:
   - Ensure you have Python 3.7 or later installed, as the package relies on dictionary order preservation and standard library modules (`statistics`, `keyword`, `re`).

3. **Import the Package**:
   - Import the `Json` class or `load` function in your Python code:
     ```python
     import jsonstats
     ```

### Option 2: Install from Repository (if hosted)
If the `jsonstats` package is hosted in a repository (e.g., GitHub), you can install it using `git` or `pip` (if published to PyPI):

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd jsonstats
   ```

2. **Copy to Project or Install Locally**:
   - Copy the `jsonstats` folder to your project directory or `site-packages`.
   - Alternatively, install locally using `pip`:
     ```bash
     pip install .
     ```

3. **Import the Package**:
   ```python
     import jsonstats
     ```

**Note**: If the package is published to PyPI, you can install it directly with:
```bash
pip install jsonstats
```

## Usage
Below are examples demonstrating the key features of the `json stats` package.

### Basic Attribute Access
```python
import jsonstats

# Create a Json object from a dictionary
data = {
    "John Smith": {"age": 31, "height": 175, "weight": 80},
    "Emma Johnson": {"age": 40, "height": 165, "weight": 55},
    "Michael Chen": {"age": 50, "height": 180, "weight": 90},
    "Sarah Davis": {"age": 21, "height": 170, "weight": 60},
    "David Wilson": {"age": 34, "height": 178, "weight": 85}
}
json_obj = jsonstats.load(data)

# Access attributes
print(json_obj.John_Smith.age)  # 31
print(json_obj.Emma_Johnson.height)  # 165
```

### Using the `jump` Function
The `jump` function extracts the values of a top-level dictionary into a `Json` object wrapping a list.
```python
# Extract dictionary values
jumped = json_obj.jump()
print(jumped)  # [{'age':31,'height':175,'weight':80},{'age':40,'height':165,'weight':55},{'age':50,'height':180,'weight':90},{'age':21,'height':170,'weight':60},{'age':34,'height':178,'weight':85}]

# Convert to native Python list
print(jumped.values())
# [{'age': 31, 'height': 175, 'weight': 80}, {'age': 40, 'height': 165, 'weight': 55}, {'age': 50, 'height': 180, 'weight': 90}, {'age': 21, 'height': 170, 'weight': 60}, {'age': 34, 'height': 178, 'weight': 85}]
```

### Statistical Operations
The `jump` function returns a `Json` object that supports attribute access to collect values into a `StatsList`, enabling statistical operations.
```python
# Get list of ages and compute mean
print(json_obj.jump().age)  # [31, 40, 50, 21, 34]
print(json_obj.jump().age.mean())  # 35.2

# Get list of heights and compute mean
print(json_obj.jump().height)  # [175, 165, 180, 170, 178]
print(json_obj.jump().height.mean())  # 173.6

# Get list of weights and compute median
print(json_obj.jump().weight)  # [80, 55, 90, 60, 85]
print(json_obj.jump().weight.median())  # 80
```

### Error Handling
- **Invalid Attributes**: Accessing a non-existent attribute raises `AttributeError`.
  ```python
  try:
      print(json_obj.jump().invalid)  # Raises AttributeError: 'invalid' not found
  except AttributeError as e:
      print(e)
  ```
- **Non-Dictionary `jump`**: Calling `jump` on a non-dictionary raises `ValueError`.
  ```python
  json_list = jsonstats.load([1, 2, 3])
  try:
      json_list.jump()  # Raises ValueError: jump() can only be called on a Json object wrapping a dictionary
  except ValueError as e:
      print(e)
  ```

## Limitations
- **Key Transformation**: Dictionary keys with spaces or invalid characters are converted to valid Python attribute names (e.g., "John Smith" becomes `John_Smith`).
- **No External Dependencies**: Relies only on the Python standard library, limiting advanced statistical or JSON features.

## Contributing
Contributions are welcome! Please submit issues or pull requests to the repository (if hosted) or contact the maintainer.