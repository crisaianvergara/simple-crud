from utils import create_book, read_book, update_book, delete_book


def main(books):
    while True:
        answer = input("Add a book? y/n: ").lower()
        if answer == "y" or answer == "yes":
            create_book(books)
            read_book(books)
            while True:
                answer = input("Update a book? y/n: ").lower()
                if answer == "y" or answer == "yes":
                    books = update_book(books)
                    read_book(books)
                else:
                    break
            while True:
                answer = input("Delete a book? y/n: ").lower()
                if answer == "y" or answer == "yes":
                    books = delete_book(books)
                    read_book(books)
                else:
                    break
        else:
            break
    return books


books = []
main(books)

