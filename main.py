import random

Admin_Rights = 0
booklist = ["Азбука", "Математика", "История", "Биология", "География", "Информатика"]
book = 0
history_arr = []

def catalogue():
    print("Выберите книгу из каталога и напишите ее номер для выбора:")
    print("0. Сброс")
    for i in range(len(booklist)):
        print(f"{i+1}. {booklist[i]}")



    global book
    global history
    book = int(input())

    if book == 0:
        menu_no_choice()
    else:
        book -= 1
        history_arr.append(booklist[book])
        menu(book)

def menu_no_choice():
    global Admin_Rights
    print("Выберите функцию:")
    print("Выбранная книга: Книга не выбрана")
    print("1. Каталог")
    print("2. История")
    if (Admin_Rights == 0):
        print("3. Выдача админ прав")
    else:
        print("3. Изменить каталог книг")
    choice = int(input())
    if choice == 1:
        catalogue()
    if choice == 2:
        history()
    if choice == 3 and Admin_Rights == 0:
        print("Введите пароль:")
        if (int(input()) != 777):
            print("Неверный пароль!")
            if (book != 0):
                menu(book)
            if (book == 0):
                menu_no_choice()
        else:
            Admin_Rights = 1
    if choice == 3 and Admin_Rights == 1:
        editor()


def menu(book):
    global Admin_Rights
    print("Выберите функцию:")
    print("Выбранная книга:", booklist[book])
    print("1. Каталог")
    print("2. Отправка заявки")
    print("3. История")
    print("4. Сброс")
    if (Admin_Rights == 0):
        print("5. Выдача админ прав")
    else:
        print("5. Изменить каталог книг")



    choice = int(input())
    if choice == 1:
        catalogue()
    if choice == 2:
        send()
    if choice == 3:
        history()
    if choice == 4:
        reset()
    if choice == 5 and Admin_Rights == 0:
        print("Введите пароль:")
        if (int(input()) != 777):
            print("Неверный пароль!")
            if (book != 0):
                menu(book)
            if (book == 0):
                menu_no_choice()
        else:
            Admin_Rights = 1
    if choice == 5 and Admin_Rights == 1:
        editor()

def edit_book():
    print("Введите номер книги:")
    num = int(input())
    num -= 1
    print("Введите новое название книги:")
    booklist[num] = input()
    editor()

def delete_book():
    print("Введите номер книги:")
    num = int(input())
    num -= 1
    del booklist[num]
    editor()

def add_book():
    print("Введите название книги:")
    booklist.append(input())
    editor()

def editor():
    global book
    print("Выберите функцию:")
    print("1. Изменение лота")
    print("2. Удаление лота")
    print("3. Добавление лота")
    print("0. Выход из редактора")

    choice = int(input())
    if (choice == 0 and book != 0):
        menu(book)
    if (choice == 0 and book == 0):
        menu_no_choice()
    if choice == 1:
        edit_book()
    if choice == 2:
        delete_book()
    if choice == 3:
        add_book()



def history():
    global history
    global book
    print("Ранее выбирались следующие книги: ")
    for i in range(len(history_arr)):
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