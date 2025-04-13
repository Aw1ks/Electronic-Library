def add_book(num_books):
    for _ in range(num_books):
        book_title = input("Введите название книги: ")
        book_author = input("Введите автора книги: ")
        shelf_location = input("Укажите номер полки: ")
        book_data = {"name_book": book_title, "author": book_author}
        with open("library.txt", "a") as file:
            file.write(f"\nShelf_{shelf_location} : {book_data}")
    return "Книги добавлены."

def display_library():
    try:
        with open("library.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Файл библиотеки не найден.")

def main():
    try:
        book_count = int(input("Сколько книг вы хотите добавить? "))
        result_message = add_book(book_count)
        print(result_message)
        display_library()
    except ValueError:
        print("Ошибка: Введите целое число для количества книг.")

if __name__ == '__main__':
    main()
