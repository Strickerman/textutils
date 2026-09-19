def word_count(text: str) -> int:
    """Count the total number of words in a string.

    Parameters
    ----------
    text : str
        The input string to analyze.

    Returns
    -------
    int
        The number of words in the string.
    """
    if not text:
        return 0

    return len(text.split())

