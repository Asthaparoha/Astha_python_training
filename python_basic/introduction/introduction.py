"""
Introduction module.

Contains solutions for:
1. Welcome message
2. Python version
3. User information display
"""

from sys import version


WELCOME_MESSAGE: str = "Welcome to Python Training"


def display_welcome_message() -> None:
    """
    Print welcome message.
    """
    print(WELCOME_MESSAGE)


def get_python_version() -> str:
    """
    Return currently installed Python version.

    Returns:
        str: Python version information.
    """
    return version


def create_user_message(user_name: str, user_age: int) -> str:
    """
    Create formatted user message.

    Args:
        user_name: User name.
        user_age: User age.

    Returns:
        str: Formatted message.
    """
    return (
        f"Hello {user_name}! "
        f"You are {user_age} years old."
    )


def main() -> None:
    """
    Execute introduction examples.
    """
    display_welcome_message()

    print("\nPython Version:")
    print(get_python_version())

    user_name: str = input("Enter your name: ")
    user_age: int = int(input("Enter your age: "))

    print(create_user_message(user_name, user_age))


if __name__ == "__main__":
    main()



