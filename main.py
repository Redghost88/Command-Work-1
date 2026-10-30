import random

book = 0
history_arr = []

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
        history_arr.append(book)
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


def history():
    global history
    global book
    lenght = len(history_arr)
    print("Ранее выбирались следующие книги: ")
    for i in range(lenght):
        print(history_arr[i])

    print("Нажмите 0 для выхода")
    a = int(input())
    if book == 0:
        menu_no_choice()
    else:
        history_arr.append(book)
        menu(book)


def send():
    err = random.randint(0, 10)
    global book
    if err == 9:
        print("Ошибка отправки заявки. Попробуйте еще раз позже")
        menu(book)
        return 0
    else:
        print("Заявка отправлена, скопируйте код книги для получения")
        print("Код книги: ", random.randint(1111111111, 9999999999))
        menu(book)


def reset():
    global book
    book = 0
    menu_no_choice()

def main():
    menu_no_choice()
if __name__ == '__main__':
    main()