"""
File Handling Exercises.

Contains solutions for:
35. Create a file and write your name into it.
36. Read a file and count words, lines, and characters.
37. Append data to existing file.
38. Copy content from one file to another.
39. Search a word in a file.
"""

from pathlib import Path


SOURCE_FILE_NAME: str = "student_data.txt"
COPY_FILE_NAME: str = "student_data_copy.txt"
USER_NAME: str = "Astha"


def create_file_and_write_name(
    file_path: str,
    user_name: str
) -> None:
    """
    Create a file and write a name into it.

    Args:
        file_path: File name.
        user_name: User name.
    """
    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(user_name)


def read_file_statistics(
    file_path: str
) -> dict[str, int]:
    """
    Read file and count words,
    lines, and characters.

    Args:
        file_path: File name.

    Returns:
        dict[str, int]: Statistics.
    """
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        content: str = file.read()

    return {
        "lines": len(
            content.splitlines()
        ),
        "words": len(
            content.split()
        ),
        "characters": len(
            content
        )
    }


def append_data_to_file(
    file_path: str,
    content: str
) -> None:
    """
    Append data to a file.

    Args:
        file_path: File name.
        content: Data to append.
    """
    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:
        file.write(
            f"\n{content}"
        )


def copy_file_content(
    source_file: str,
    destination_file: str
) -> None:
    """
    Copy content from one file to another.

    Args:
        source_file: Source file.
        destination_file: Destination file.
    """
    with open(
        source_file,
        "r",
        encoding="utf-8"
    ) as source:
        content: str = source.read()

    with open(
        destination_file,
        "w",
        encoding="utf-8"
    ) as destination:
        destination.write(
            content
        )


def search_word_in_file(
    file_path: str,
    search_word: str
) -> bool:
    """
    Search for a word in a file.

    Args:
        file_path: File name.
        search_word: Word to search.

    Returns:
        bool: True if found.
    """
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        content: str = file.read()

    return (
        search_word.lower()
        in content.lower()
    )


def main() -> None:
    """
    Execute file handling exercises.
    """

    print(
        "\n--- Question 35: Create File and Write Name ---"
    )

    create_file_and_write_name(
        SOURCE_FILE_NAME,
        USER_NAME
    )

    print(
        f"File '{SOURCE_FILE_NAME}' created successfully."
    )

    print(
        "\n--- Question 37: Append Data ---"
    )

    append_data_to_file(
        SOURCE_FILE_NAME,
        "Python Training Assignment"
    )

    print(
        "Data appended successfully."
    )

    print(
        "\n--- Question 36: File Statistics ---"
    )

    statistics = (
        read_file_statistics(
            SOURCE_FILE_NAME
        )
    )

    for key, value in (
        statistics.items()
    ):
        print(
            f"{key}: {value}"
        )

    print(
        "\n--- Question 38: Copy File Content ---"
    )

    copy_file_content(
        SOURCE_FILE_NAME,
        COPY_FILE_NAME
    )

    print(
        f"Content copied to '{COPY_FILE_NAME}'."
    )

    print(
        "\n--- Question 39: Search Word ---"
    )

    word_to_search: str = input(
        "Enter word to search: "
    )

    if search_word_in_file(
        SOURCE_FILE_NAME,
        word_to_search
    ):
        print(
            f"'{word_to_search}' found in file."
        )
    else:
        print(
            f"'{word_to_search}' not found in file."
        )


if __name__ == "__main__":
    main()