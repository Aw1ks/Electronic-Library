def add_book(count):
    for _ in range(count):
        name_book = input("Имя книги?: ")
        authors = input("Автор книги?: ")
        shelf_number = input("На какую полку необходимо положить книгу?: ")
        book_format = {"name_book": name_book, "authors": authors}
        with open("library.txt", "a") as f:
            f.write(f"\nShelf_{shelf_number} : {book_format}")
    return "Книги добавлены"

def read_file_library():
    with open("library.txt", "r") as f:
        for line in f:
            print(line.strip()) 

def main():
    count = int(input("Сколько книг нужно добавить? "))
    result = add_book(count)
    print(result)
    read_file_library()

if __name__ == '__main__':
    main()
