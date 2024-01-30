from random import choice
import string


def random_string(len=10) -> str:
    """
    Generate a random string
    Args:
        len (int, optional): length of the random string. Defaults to 10.
    """
    chars = string.ascii_letters + string.digits
    return "".join([choice(chars) for _ in range(len)])
