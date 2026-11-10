def kebab_case(text: str) -> str:
    """Convert a string to kebab-case format.

    Parameters
    ----------
    text : str
        The input string to transform.

    Returns
    -------
    str
        The input string converted to kebab-case.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    clean_text = text.replace("_", " ").strip()
    words = clean_text.split()
    return "-".join(words).lower()