def standardize_phone(phone_number):
    phone_number = phone_number.replace("+", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    if phone_number.startswith("8"):
        phone_number = "+7" + phone_number[1:]
    elif phone_number.startswith("7"):
        phone_number = "+" + phone_number
    elif len(phone_number) == 10:
        phone_number = "+7" + phone_number
    return phone_number[:12]

def standardize_name(name):
    return name.title()

def add_contact(phone_book: dict) -> dict:
    name = input('Введите имя контакта: ')
    phone = input('Введите номер телефона в формате "9*********" : ')
    standartized_name = standardize_name(name)
    standartized_phone = standardize_phone(phone)
    new_phone_book = phone_book.copy()
    new_phone_book[standartized_name] = standartized_phone
    print('Контакт успешно добавлен !')
    return new_phone_book

def delete_contact(phonebook):
    name = input("Введите имя контакта для удаления: ")
    name = standardize_name(name)
    if name in phonebook:
        del phonebook[name]
        print("Контакт удален.")
    else:
        print("Контакт не найден.")

def view_phonebook(phonebook):
    if phonebook:
        print("Список контактов:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Телефонная книга пуста.")

def change_phone(phonebook):
    name = input("Введите имя контакта для изменения номера: ")
    name = standardize_name(name)
    if name in phonebook:
        while True:
            phone = input("Введите новый номер телефона: ")
            phone = standardize_phone(phone)
            if len(phone) == 12 and phone.startswith("+7"):
              break
            else:
              print("Неверный формат номера. Попробуйте еще раз.")
        phonebook[name] = phone
        print("Номер телефона изменен.")
    else:
        print("Контакт не найден.")

phonebook = {}

while True:
    print("Выберите функцию:")
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Просмотреть телефонную книгу")
    print("4. Изменить номер")
    print("5. Выход")
    choice = input("Введите номер функции: ")
    if choice == '1':
        add_contact(phonebook)
    elif choice == '2':
        delete_contact(phonebook)
    elif choice == '3':
        view_phonebook(phonebook)
    elif choice == '4':
        change_phone(phonebook)
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

print("Программа завершена.")