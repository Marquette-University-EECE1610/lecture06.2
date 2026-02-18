"""
Refactoring example: Grade analysis program
This program reads student grades and performs various analyses.
Add a main method. Move the computation into a separate file (my_module.py).
Keep the input/output in the main file (refactor.py). Test via import.
"""


def get_grades() -> list[int]:
    """Prompt the user for student grades (comma-separated)."""
    grades_input = input("Enter grades separated by commas: ")
    grades = [int(g.strip()) for g in grades_input.split(",")]
    return grades


def calculate_average(grades: list[int]) -> float | int:
    """Calculate the average of a list of grades."""
    if len(grades) == 0:
        return 0
    total = sum(grades)
    average = total / len(grades)
    return average


def find_highest(grades: list[int]) -> int | None:
    """Find the highest grade in the list."""
    if len(grades) == 0:
        return None
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    return highest


def find_lowest(grades: list[int]) -> int | None:
    """Find the lowest grade in the list."""
    if len(grades) == 0:
        return None
    lowest = grades[0]
    for grade in grades:
        if grade < lowest:
            lowest = grade
    return lowest


def count_passing(grades: list[int], threshold: int = 60) -> int:
    """Count how many grades are at or above the threshold."""
    count = 0
    for grade in grades:
        if grade >= threshold:
            count += 1
    return count


def count_failing(grades: list[int], threshold: int = 60) -> int:
    """Count how many grades are below the threshold."""
    count = 0
    for grade in grades:
        if grade < threshold:
            count += 1
    return count


def letter_grade(numeric_grade: int) -> str:
    """Convert a numeric grade to a letter grade."""
    if numeric_grade >= 90:
        return "A"
    elif numeric_grade >= 80:
        return "B"
    elif numeric_grade >= 70:
        return "C"
    elif numeric_grade >= 60:
        return "D"
    else:
        return "F"


def convert_to_letters(grades: list[int]) -> list[str]:
    """Convert a list of numeric grades to letter grades."""
    letters = []
    for grade in grades:
        letter = letter_grade(grade)
        letters.append(letter)
    return letters


def display_statistics(grades: list[int]) -> None:
    """Display a summary of grade statistics."""
    average = calculate_average(grades)
    highest = find_highest(grades)
    lowest = find_lowest(grades)
    passing = count_passing(grades)
    failing = count_failing(grades)

    print("\nGrade Statistics:")
    print(f"  Average: {average:.2f}")
    print(f"  Highest: {highest}")
    print(f"  Lowest: {lowest}")
    print(f"  Passing (60+): {passing}")
    print(f"  Failing (<60): {failing}")


def display_letter_grades(grades: list[int]) -> None:
    """Display numeric and letter grades side by side."""
    letters = convert_to_letters(grades)
    print("\nNumeric to Letter Conversion:")
    for i in range(len(grades)):
        print(f"  {grades[i]} -> {letters[i]}")


# Main program
grades = get_grades()
display_statistics(grades)
display_letter_grades(grades)
