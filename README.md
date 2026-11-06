# textutils

A lightweight Python library providing common text-processing and manipulation utilities.
Developed as part of the *Open Source Development* course at ENSISA, Université de Haute-Alsace.

## Features

This initial version provides essential string manipulation tools:
* `word_count(text)`: Counts the number of words in a given text string.
* `character_count(text)`: Returns the total number of characters in the string.
* `reverse(text)`: Returns the string reversed character by character.
* `capitalize_words(text)`: Capitalizes the first letter of each word in the string.

*(Planned features for upcoming versions: `snake_case()`, `camel_case()`, and `slugify()`)*

## Installation

### For Users
Install the package directly via `pip`:
```bash
pip install textutils
```

### For Development / Contributors
Clone the repository and install it in editable mode with development dependencies:
```bash
git clone https://github.com/<your-username>/textutils.git
cd textutils
pip install -e .[dev]
```

## Usage

Here is a quick example demonstrating how to import and use the functions:

```python
from textutils import (
    capitalize_words,
    character_count,
    reverse,
    word_count,
)

sample_text = "hello open source world"

# 1. Count words
print(word_count(sample_text))         # Output: 4

# 2. Count characters
print(character_count(sample_text))    # Output: 23

# 3. Capitalize words
print(capitalize_words(sample_text))   # Output: "Hello Open Source World"

# 4. Reverse text
print(reverse(sample_text))            # Output: "dlrow ecruos nepo olleh"
```

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a dedicated branch for your feature or fix:
   ```bash
   git switch -c feature/my-new-feature
   ```
3. Commit your changes with clear, descriptive commit messages:
   ```bash
   git commit -m "Add unit tests for capitalize_words"
   ```
4. Push your branch to your fork:
   ```bash
   git push origin feature/my-new-feature
   ```
5. Open a Pull Request on GitHub describing your modifications.

## Author

**Esteban Stricker**

## License

This project is licensed under the MIT License.