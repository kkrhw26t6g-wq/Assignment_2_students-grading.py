def get_grade(score):
    """
    Validates the score and returns the corresponding letter grade.
    Returns None if the score is outside the range [0, 100].
    """
    # Range validation
    if score < 0 or score > 100:
        return None

    # Grade calculation using if / elif / else
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    try:
        score_input = float(input("Enter student score (0-100): "))
        grade = get_grade(score_input)

        if grade is None:
            print("Error: Score must be between 0 and 100.")
        else:
            print(f"Grade: {grade}")
    except ValueError:
        print("Error: Please enter a valid numerical score.")


if __name__ == "__main__":
    main()