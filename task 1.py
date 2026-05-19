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


if __name__ == "__main__":
    records = []

    try:
        # Получаем путь к файлу
        file_path = input("Введите полный путь к файлу с данными: ")
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}, попробуйте еще раз")
        exit()
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                # Читаем данные
                records = file.readlines()
                print(records)
        except FileNotFoundError as ex:
            print(f"Файл не найден: {ex}")
            exit()
        except Exception as ex:
            print(f"Неизвестная ошибка: {ex}")
            exit()

    if len(records) == 0:
        print("В файле нет данных")
        exit()
    if type(records) is not list:
        print("Неверный формат данных")
        exit()

    process_grades(records)
