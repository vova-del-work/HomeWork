def get_numbers():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            return num1, num2
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числа.")


def get_operation():
    operations = {
        '1': 'Сложение',
        '2': 'Вычитание',
        '3': 'Умножение',
        '4': 'Деление',
        '5': 'Возведение в степень',
        '6': 'Извлечение квадратного корня'
    }

    print("\nВыберите операцию:")
    for key, value in operations.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Введите номер операции: ")
        if choice in operations:
            return choice
        else:
            print("Некорректный выбор. Пожалуйста, выберите номер операции из списка.")


def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 == 0:
            return "Ошибка: деление на ноль."
        return num1 / num2
    elif operation == '5':
        return num1 ** num2
    elif operation == '6':
        if num1 < 0:
            return "Ошибка: извлечение квадратного корня из отрицательного числа."
        return num1 ** 0.5


def main():
    while True:
        num1, num2 = get_numbers()
        operation = get_operation()
        result = calculate(num1, num2, operation)
        print(f"Результат: {result}")

        again = input("Хотите выполнить еще одну операцию? (да/нет): ").strip().lower()
        if again != 'да':
            break


if __name__ == "__main__":
    main()