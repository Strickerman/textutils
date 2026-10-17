def reverse(text: str) -> str:
    """Reverse a string.

    Parameters
    ----------
    text : str
        The input string to reverse.

    Returns
    -------
    str
        The string reversed.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return text[::-1]