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
    """
    if not text:
        return 0
    
    return len(text)