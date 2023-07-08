def create_book():
    """Create Book"""
    title = input("Book Title: ").title()
    author = input("Book Author: ").title()
    while True:
        isbn = input("Book ISBN: ")
        if isbn.isdigit():
            isbn = int(isbn)
            break
        else:
            print("Please enter a valid ISBN.")
    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
    }
    return book


books = []
while True:
    answer = input("Do you want to add book? y/n: ").lower()
    if answer == "y":
        books.append(create_book())
        print(books)
    else:
        break






