def character_count(text: str) -> int:
    """Count the total number of characters in a string.

    Parameters
    ----------
    text : str
        The input string to analyze.

    Returns
    -------
    int
        The number of characters in the string.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return 0

    return len(text)
