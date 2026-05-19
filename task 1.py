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
                raise ValueError("Неправильная оценка")

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


def emergency_exit(message):
    print(message)
    exit()


if __name__ == "__main__":
    records = []

    try:
        # Получаем путь к файлу
        file_path = input("Введите полный путь к файлу с данными: ")
    except Exception as ex:
        emergency_exit(f"Неизвестная ошибка: {ex}, попробуйте еще раз")
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                # Читаем данные
                records = file.readlines()
                print(records)
        except FileNotFoundError as ex:
            emergency_exit(f"Файл не найден: {ex}")
        except Exception as ex:
            emergency_exit(f"Неизвестная ошибка: {ex}")

    if len(records) == 0:
        emergency_exit("В файле нет данных")
    if type(records) is not list:
        emergency_exit("Неверный формат данных")

    process_grades(records)
