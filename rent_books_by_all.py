def all_lent_books(library_book):
    lent_books = []
    for book in library_book:
        if book.get('borrowers') and len(book['borrowers']) > 0:
            lent_books.append(book)

    if not lent_books:
        print("No books are currently lent out.")
        return library_book

    print("All lent books:")
    for book in lent_books:
        print("-------------------")
        print(f"Title: {book['title']}")
        print(f"Author(s): {book['author(s)']}")
        print(f"Year Published: {book['year_published']}")
        print(f"Price: {book['price']}")
        print(f"Pages: {book['pages']}")
        print(f"ISBN: {book['ISBN']}")
        print(f"Genres: {', '.join(book['genres'])}")
        print("Borrowers:")
        for borrower in book['borrowers']:
            print(f"- {borrower['name']}")

    return library_book

