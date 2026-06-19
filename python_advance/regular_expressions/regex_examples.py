"""
Regular Expression Exercises.

Contains solutions for:
24. Extract numbers from string
25. Validate email
26. Validate mobile number
27. Search word in sentence
28. Extract capitalized words
29. Replace multiple spaces
30. Check alphabets only
31. Password validation
"""

import re


EMAIL_PATTERN: str = (
    r"^[A-Za-z0-9._%+-]+"
    r"@[A-Za-z0-9.-]+"
    r"\.[A-Za-z]{2,}$"
)

MOBILE_PATTERN: str = (
    r"^[0-9]{10}$"
)

ALPHABET_PATTERN: str = (
    r"^[A-Za-z]+$"
)

PASSWORD_PATTERN: str = (
    r"^(?=.*[0-9])"
    r"(?=.*[!@#$%^&*])"
    r".{8,}$"
)


def extract_numbers(
    text: str
) -> list[str]:
    """
    Extract all numbers
    from a string.
    """
    return re.findall(
        r"\d+",
        text
    )


def validate_email(
    email: str
) -> bool:
    """
    Validate email address.
    """
    return (
        re.fullmatch(
            EMAIL_PATTERN,
            email
        )
        is not None
    )


def validate_mobile_number(
    mobile_number: str
) -> bool:
    """
    Validate 10-digit
    mobile number.
    """
    return (
        re.fullmatch(
            MOBILE_PATTERN,
            mobile_number
        )
        is not None
    )


def search_word(
    sentence: str,
    word: str
) -> bool:
    """
    Search word in sentence.
    """
    return (
        re.search(
            word,
            sentence
        )
        is not None
    )


def extract_capitalized_words(
    sentence: str
) -> list[str]:
    """
    Extract words starting
    with a capital letter.
    """
    return re.findall(
        r"\b[A-Z][a-zA-Z]*\b",
        sentence
    )


def replace_multiple_spaces(
    text: str
) -> str:
    """
    Replace multiple spaces
    with a single space.
    """
    return re.sub(
        r"\s+",
        " ",
        text
    )


def contains_only_alphabets(
    text: str
) -> bool:
    """
    Check whether a string
    contains only alphabets.
    """
    return (
        re.fullmatch(
            ALPHABET_PATTERN,
            text
        )
        is not None
    )


def validate_password(
    password: str
) -> bool:
    """
    Validate password.

    Conditions:
    - Minimum length 8
    - At least one digit
    - At least one special character
    """
    return (
        re.fullmatch(
            PASSWORD_PATTERN,
            password
        )
        is not None
    )


def main() -> None:
    """
    Execute regular
    expression exercises.
    """

    print(
        "\n--- Question 24 ---"
    )

    sample_text = (
        "Python 2025 "
        "has 50 modules "
        "and 100 examples."
    )

    print(
        extract_numbers(
            sample_text
        )
    )

    print(
        "\n--- Question 25 ---"
    )

    print(
        validate_email(
            "test@example.com"
        )
    )

    print(
        "\n--- Question 26 ---"
    )

    print(
        validate_mobile_number(
            "9876543210"
        )
    )

    print(
        "\n--- Question 27 ---"
    )

    sentence = (
        "Python is powerful."
    )

    print(
        search_word(
            sentence,
            "Python"
        )
    )

    print(
        "\n--- Question 28 ---"
    )

    capitalized_sentence = (
        "Astha studies "
        "Python at LNCTS "
        "Bhopal."
    )

    print(
        extract_capitalized_words(
            capitalized_sentence
        )
    )

    print(
        "\n--- Question 29 ---"
    )

    print(
        replace_multiple_spaces(
            "Python    is     fun"
        )
    )

    print(
        "\n--- Question 30 ---"
    )

    print(
        contains_only_alphabets(
            "Python"
        )
    )

    print(
        "\n--- Question 31 ---"
    )

    print(
        validate_password(
            "Password@1"
        )
    )


if __name__ == "__main__":
    main()
