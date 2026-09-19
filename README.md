textutils

A lightweight Python library providing common text-processing and manipulation utilities.
Developed as part of the Open Source Development course at ENSISA, Université de Haute-Alsace.

Features
This initial version provides essential string manipulation tools:
word_count(text): Counts the number of words in a given text string.
character_count(text): Returns the total number of characters in the string.
reverse(text): Returns the string reversed character by character.
capitalize_words(text): Capitalizes the first letter of each word in the string.
(Planned features for upcoming versions: snake_case(), camel_case(), and slugify())

Installation
Clone the repository to your local machine:
git clone https://github.com/<your-username>/textutils.git
cd textutils

Ensure you have Python 3 installed. You can verify your setup by running:
python3 --version


Usage
Here is a quick example demonstrating how to import and use the functions:
from textutils.transform import (
    capitalize_words,
    character_count,
    reverse,
    word_count,
)

sample_text = "hello open source world"

# 1. Count words
print(word_count(sample_text))
# Output: 4

# 2. Count characters
print(character_count(sample_text))
# Output: 23

# 3. Capitalize words
print(capitalize_words(sample_text))
# Output: "Hello Open Source World"

# 4. Reverse text
print(reverse(sample_text))
# Output: "dlrow ecruos nepo olleh"


Contributing

Contributions are welcome! To contribute to this project, please follow these steps:
Fork the repository.

Create a dedicated branch for your feature or fix:
git checkout -b feature/my-new-feature

Commit your changes with clear, descriptive commit messages:
git commit -m "Add unit tests for capitalize_words"


Push your branch to your fork:
git push origin feature/my-new-feature


Open a Pull Request on GitHub describing your modifications.

Author
Esteban Stricker

License
This project is licensed under the MIT License.