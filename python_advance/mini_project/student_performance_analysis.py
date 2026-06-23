"""
Student Performance Analysis Project.

Tasks:
1. Load student data into Pandas
2. Add performance column
3. Create line chart
4. Create scatter plot
5. Create seaborn barplot
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


STUDENT_DATA: dict[str, list] = {
    "Name": [
        "Rahul",
        "Priya",
        "Siri",
        "Anuj"
    ],
    "Marks": [
        70,
        80,
        90,
        60
    ],
    "Hours_Studied": [
        2,
        3,
        5,
        1
    ]
}

PASS_MARKS: int = 65


def create_student_dataframe() -> pd.DataFrame:
    """
    Create student DataFrame.

    Returns:
        pd.DataFrame:
            Student DataFrame.
    """
    return pd.DataFrame(
        STUDENT_DATA
    )


def add_performance_column(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Add performance column.

    Args:
        dataframe:
            Student DataFrame.

    Returns:
        pd.DataFrame:
            Updated DataFrame.
    """
    updated_dataframe = (
        dataframe.copy()
    )

    updated_dataframe[
        "Performance"
    ] = updated_dataframe[
        "Marks"
    ].apply(
        lambda marks:
        "Pass"
        if marks > PASS_MARKS
        else "Fail"
    )

    return updated_dataframe


def create_line_chart(
    dataframe: pd.DataFrame
) -> None:
    """
    Create Hours vs Marks line chart.
    """
    plt.figure(
        figsize=(8, 5)
    )

    plt.plot(
        dataframe["Hours_Studied"],
        dataframe["Marks"],
        marker="o"
    )

    plt.title(
        "Hours Studied vs Marks"
    )

    plt.xlabel(
        "Hours Studied"
    )

    plt.ylabel(
        "Marks"
    )

    plt.show()


def create_scatter_plot(
    dataframe: pd.DataFrame
) -> None:
    """
    Create scatter plot.
    """
    plt.figure(
        figsize=(8, 5)
    )

    plt.scatter(
        dataframe["Hours_Studied"],
        dataframe["Marks"]
    )

    plt.title(
        "Study Hours vs Marks"
    )

    plt.xlabel(
        "Hours Studied"
    )

    plt.ylabel(
        "Marks"
    )

    plt.show()


def create_performance_barplot(
    dataframe: pd.DataFrame
) -> None:
    """
    Create performance barplot.
    """
    plt.figure(
        figsize=(8, 5)
    )

    sns.barplot(
        data=dataframe,
        x="Performance",
        y="Marks"
    )

    plt.title(
        "Performance vs Marks"
    )

    plt.show()


def main() -> None:
    """
    Execute mini project.
    """

    student_dataframe = (
        create_student_dataframe()
    )

    student_dataframe = (
        add_performance_column(
            student_dataframe
        )
    )

    print(
        "\n--- Student Dataset ---"
    )

    print(
        student_dataframe
    )

    create_line_chart(
        student_dataframe
    )

    create_scatter_plot(
        student_dataframe
    )

    create_performance_barplot(
        student_dataframe
    )


if __name__ == "__main__":
    main()
