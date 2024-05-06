import random
import string


def generate_random_string():
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=10)
    )


def generate_random_first_name():
    return ''.join(
        random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=5)
    )


def generate_random_last_name():
    return ''.join(
        random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=5)
    )


def generate_random_username():
    return ''.join(
        random.choices(string.ascii_lowercase, k=10)
    )


def generate_random_description():
    return ''.join(
        random.choices(string.ascii_lowercase, k=10)
    )
