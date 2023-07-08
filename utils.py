from book import Book


def create_book(books):
    title = input("Enter book title: ").title()
    author = input("Enter book author: ").title()
    isbn = check_isbn()
    new_book = Book(title, author, isbn)
    books.append(new_book)
    print("Book successfully added.")
    return books


def read_book(books):
    if books:
        book_num = 1
        for book in books:
            print(f"Book {book_num} - Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
            book_num += 1
    else:
        print("Empty.")


def update_book(books):
    isbn = check_isbn()
    is_book = False
    for book in books:
        if book.isbn == isbn:
            book.title = input(f"Update book title from {book.title} to: ").title()
            book.author = input(f"Update book author from {book.author} to: ").title()
            book.isbn = input(f"Update book isbn from {book.isbn} to: ")
            print("Book successfully updated.")
            is_book = True
            break
    if not is_book:
        print("That book doesn't exist.")
    return books
    

def delete_book(books):
    isbn = check_isbn()
    is_book = False
    for book in books:
        if book.isbn == isbn:
            books.remove(book)
            is_book = True
            print("Book successfully deleted.")
            break
    if not is_book:
        print("That book doesn't exist.")
    return(books)


def check_isbn():
    while True:
        isbn = input("Enter book isbn: ")
        if isbn.isdigit():
            isbn = int(isbn)
            break
        else:
            print("Please enter a valid isbn.")
    return isbn
