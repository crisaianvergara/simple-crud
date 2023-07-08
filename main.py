def create_book():
    """Create Book"""
    title = input("Book Title: ").title()
    author = input("Book Author: ").title()
    isbn = check_isbn()
    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
    }
    return book

def display_book(books):
    """Display Books"""
    book_number = 1
    for book in books:
        print(f"Book {book_number} - Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        book_number += 1


def update_book(books):
    """Update Book"""
    is_book = False
    isbn = check_isbn()
    for book in books:
        if isbn == book["isbn"]:
            # update book here
            book["title"] = input(f"Update Book Title from {book['title']} to: ").title()
            book["author"] = input(f"Update Book author from {book['author']} to: ").title()
            book["isbn"] = check_isbn(is_edit=True, updated_isbn=book['isbn'])
            is_book = True
            break
    if not is_book:
        print("That book doesn't exist.")
    return books

def delete_book(books):
    """Delete Book"""
    is_book = False
    isbn = check_isbn()
    for book in books:
        if isbn == book["isbn"]:
            books.remove(book)
            is_book = True
            break
    if not is_book:
        print("That book doesn't exist.")
    return books
    


def check_isbn(is_edit=False, updated_isbn= ""):
    """Check ISBN"""
    while True:
        if not is_edit:
            isbn = input("Book ISBN: ")
        else:
            isbn = input(f"Update Book author from {updated_isbn} to: ").title()
        if isbn.isdigit():
            isbn = int(isbn)
            break
        else:
            print("Please enter a valid ISBN.")
    return isbn

def main():
    books = []
    while True:
        create_answer = input("Do you want to add a book? y/n: ").lower()
        if create_answer == "y" or create_answer == "yes":
            books.append(create_book())
            display_book(books)
            while True:
                delete_answer = input("Do you want to delete a book? y/n: ").lower()
                if delete_answer == "y" or delete_answer == "yes":
                    books = delete_book(books)
                    display_book(books)
                else:
                    break
            while True:
                update_answer = input("Do you want to update a book? y/n: ").lower()
                if update_answer == "y" or update_answer == "yes":
                    books = update_book(books)
                    display_book(books)
                else:
                    break
        else:
            break
    return books

main()






