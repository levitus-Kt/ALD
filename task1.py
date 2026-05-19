import re


def process_grades(records: list[str]) -> dict:
    valid_count = 0
    total_sum = 0
    passed = []
    skipped = 0

    for record in records:
        parts = record.split(":")
        # Проверка на двоеточие
        if len(parts) != 2:
            skipped += 1
            continue

        if len(parts[0]) < 2 or len(parts[1]) < 1:
            skipped += 1
            continue

        surname, grade_str = parts
        grade_str = grade_str.strip()
        if re.match(r"\d+", surname):
            skipped += 1
            continue

        # Проверка, что оценка - число
        try:
            grade = int(grade_str)
            # Проверка на диапазон оценек
            if not (0 <= grade <= 100):
                raise ValueError("Неправильная оценка")

            valid_count += 1
            total_sum += grade

            if grade >= 60:
                passed.append(surname)
        except (ValueError, TypeError):
            skipped += 1

    average = round(total_sum / valid_count, 1) if valid_count > 0 else 0.0
    passed = list(set(passed))
    passed.sort()

    return {
        "valid_count": valid_count,
        "average": average,
        "passed": passed,
        "skipped": skipped,
    }


def read_data() -> list[str]:
    try:
        # Получаем путь к файлу
        file_path = input("Введите путь к файлу с данными: ")
    except Exception as ex:
        emergency_exit(f"Неизвестная ошибка: {ex}, попробуйте еще раз")
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                # Читаем данные
                grades = file.readlines()
        except FileNotFoundError as ex:
            emergency_exit(f"Файл не найден: {ex}")
        except Exception as ex:
            emergency_exit(f"Неизвестная ошибка: {ex}")
    return grades


def emergency_exit(message):
    print(message)
    exit()


if __name__ == "__main__":
    grades = read_data()

    if len(grades) == 0:
        emergency_exit("В файле нет данных")
    if type(grades) is not list:
        emergency_exit("Неверный формат данных")

    process_grades(grades)
