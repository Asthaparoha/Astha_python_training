"""
Object-Oriented Programming Exercises.

Contains solutions for:
40. Student class
41. Car class with constructor
42. Person and Employee inheritance
43. Bank encapsulation
44. Polymorphism
"""


class Student:
    """
    Represents a student.
    """

    def __init__(
        self,
        student_id: int,
        name: str,
        course: str
    ) -> None:
        """
        Initialize student object.

        Args:
            student_id: Student identifier.
            name: Student name.
            course: Course name.
        """
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_details(self) -> None:
        """
        Display student details.
        """
        print(
            f"Student ID: {self.student_id}"
        )
        print(
            f"Name: {self.name}"
        )
        print(
            f"Course: {self.course}"
        )


class Car:
    """
    Represents a car.
    """

    def __init__(
        self,
        brand: str,
        model: str,
        year: int
    ) -> None:
        """
        Initialize car object.

        Args:
            brand: Car brand.
            model: Car model.
            year: Manufacturing year.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self) -> None:
        """
        Display car details.
        """
        print(
            f"Brand: {self.brand}"
        )
        print(
            f"Model: {self.model}"
        )
        print(
            f"Year: {self.year}"
        )


class Person:
    """
    Represents a person.
    """

    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        """
        Initialize person object.

        Args:
            name: Person name.
            age: Person age.
        """
        self.name = name
        self.age = age

    def display_details(self) -> None:
        """
        Display person details.
        """
        print(
            f"Name: {self.name}"
        )
        print(
            f"Age: {self.age}"
        )


class Employee(Person):
    """
    Represents an employee.
    """

    def __init__(
        self,
        name: str,
        age: int,
        employee_id: int
    ) -> None:
        """
        Initialize employee object.

        Args:
            name: Employee name.
            age: Employee age.
            employee_id: Employee identifier.
        """
        super().__init__(
            name,
            age
        )

        self.employee_id = (
            employee_id
        )

    def display_details(self) -> None:
        """
        Display employee details.
        """
        super().display_details()

        print(
            f"Employee ID: "
            f"{self.employee_id}"
        )


class Bank:
    """
    Represents a bank account.
    """

    def __init__(
        self,
        account_holder: str,
        balance: float
    ) -> None:
        """
        Initialize bank account.

        Args:
            account_holder:
                Account holder name.
            balance:
                Initial balance.
        """
        self.account_holder = (
            account_holder
        )

        self.__balance = balance

    def deposit(
        self,
        amount: float
    ) -> None:
        """
        Deposit amount.

        Args:
            amount:
                Deposit amount.
        """
        if amount > 0:
            self.__balance += amount

    def withdraw(
        self,
        amount: float
    ) -> None:
        """
        Withdraw amount.

        Args:
            amount:
                Withdrawal amount.
        """
        if (
            amount > 0
            and amount <= self.__balance
        ):
            self.__balance -= amount

    def get_balance(
        self
    ) -> float:
        """
        Return current balance.

        Returns:
            float:
                Account balance.
        """
        return self.__balance


class Dog:
    """
    Dog class for polymorphism.
    """

    def speak(self) -> str:
        """
        Return dog sound.
        """
        return "Bark"


class Cat:
    """
    Cat class for polymorphism.
    """

    def speak(self) -> str:
        """
        Return cat sound.
        """
        return "Meow"


def main() -> None:
    """
    Execute OOP exercises.
    """

    print(
        "\n--- Question 40: Student Class ---"
    )

    student = Student(
        101,
        "Astha",
        "Engineering"
    )

    student.display_details()

    print(
        "\n--- Question 41: Car Class ---"
    )

    car = Car(
        "Toyota",
        "Corolla",
        2024
    )

    car.display_details()

    print(
        "\n--- Question 42: Inheritance ---"
    )

    employee = Employee(
        "Astha",
        21,
        1001
    )

    employee.display_details()

    print(
        "\n--- Question 43: Encapsulation ---"
    )

    bank_account = Bank(
        "Astha",
        10000
    )

    bank_account.deposit(
        2000
    )

    bank_account.withdraw(
        1500
    )

    print(
        f"Current Balance: "
        f"{bank_account.get_balance()}"
    )

    print(
        "\n--- Question 44: Polymorphism ---"
    )

    animals = [
        Dog(),
        Cat()
    ]

    for animal in animals:
        print(
            animal.speak()
        )


if __name__ == "__main__":
    main()