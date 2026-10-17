def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string.

    Parameters
    ----------
    text : str
        The input string to transform.

    Returns
    -------
    str
        The string with each word capitalized.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split(" ")
    words_capitalised = []

    for word in words:
        words_capitalised.append(word.capitalize())

    return " ".join(words_capitalised)
