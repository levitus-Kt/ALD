def process_grades(records: list[str]) -> dict:
    valid_count = 0
    total_sum = 0
    passed_students = []
    skipped = 0

    for record in records:
        parts = record.split(":")
        if len(parts) != 2:
            skipped += 1
            continue

        surname, grade_str = parts
        grade_str = grade_str.strip()

        try:
            grade = int(grade_str)
            if not (0 <= grade <= 100):
                raise ValueError("Invalid grade")

            valid_count += 1
            total_sum += grade

            if grade >= 60:
                passed_students.append(surname)
        except (ValueError, TypeError):
            skipped += 1

    average = round(total_sum / valid_count, 1) if valid_count > 0 else 0.0
    passed_students.sort()

    return {
        "valid_count": valid_count,
        "average": average,
        "passed": passed_students,
        "skipped": skipped,
    }


if __name__ == "__main__":
    choose = input("""
        Выберите вариант ввода (цифрой):
            1. Ввести с клавиатуры
            2. Открыть файл и считать данные

""")
    if "1" in choose:
        process_grades()
    elif "2" in choose:
        open_file_and
    process_grades()
