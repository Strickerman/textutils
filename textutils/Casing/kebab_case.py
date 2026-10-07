def kebab_case(text: str) -> str:
    """Converts a string to kebab-case (lowercase words separated by hyphens).

    Handles leading/trailing whitespace and multiple consecutive spaces.

    Args:
        text (str): The input string to convert.

    Returns:
        str: The kebab-cased string.
    """
    return "-".join(text.strip().lower().split())