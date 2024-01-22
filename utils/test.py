from typing import Any


def dict_to_str(d: dict[str, Any]) -> str:
    """Convert a dictionary into a string.
    Used to compare dictionnaries containing NumPy arrays.

    Args:
        d (dict): a dictionary.

    Returns:
        str: string encoded dictionary.
    """
    encoded = ""

    for k, v in d.items():
        encoded += f"{k}{v}"

    return encoded
