
def catalogue():
    print("Выберите книгу из каталога и напишите ее номер для выбора:")
    print("0. Сброс")
    print("1. Азбука")
    print("2. Математика")
    print("3. История")
    print("4. Биология")
    print("5. География")
    print("6. Информатика")

    choice = int(input())
    return choice

def menu_no_choice():
    print("Выберите функцию:")
    print("Выбор: Книга не выбрана")
    print("1. Каталог")
    print("2. История")

    choice = int(input())
    return choice

def menu(book):
    print("Выберите функцию:")
    print("Выбор: ", book)
    print("1. Каталог")
    print("2. Отправка заявки")
    print("3. История")
    print("4. Сброс")

    choice = int(input())
    return choice

