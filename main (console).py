book = 0
history = []
def catalogue():
    print("Выберите книгу из каталога и напишите ее номер для выбора:")
    print("0. Сброс")
    print("1. Азбука")
    print("2. Математика")
    print("3. История")
    print("4. Биология")
    print("5. География")
    print("6. Информатика")

    global book
    global history
    book = int(input())

    if book == 0:
        menu_no_choice()
    else:
        history.append(book)
        menu(book)

def menu_no_choice():
    print("Выберите функцию:")
    print("Выбор: Книга не выбрана")
    print("1. Каталог")
    print("2. История")

    choice = int(input())
    if choice == 1:
        catalogue()
    if choice == 2:
        history()


def menu(book):
    print("Выберите функцию:")
    print("Выбор: ", book)
    print("1. Каталог")
    print("2. Отправка заявки")
    print("3. История")
    print("4. Сброс")

    choice = int(input())
    if choice == 1:
        catalogue()
    if choice == 2:
        send()
    if choice == 3:
        history()
    if choice == 4:
        reset()


