def view_all_books(library_book):
    if not library_book:
        print("The library is currently empty. No books to display.")
        return
    
    print("All books in the library:")
    for book in library_book:
        if not book.get('removed', False):
            print("-------------------")
            print(f"Title: {book['title']}")
            print(f"Author(s): {book['author(s)']}")
            print(f"Year Published: {book['year_published']}")
            print(f"Price: {book['price']}")
            print(f"Available quantity: {book['quantity']}")
            print(f"Pages: {book['pages']}")
            print(f"ISBN: {book['ISBN']}")
            print(f"Genres: {', '.join(book['genres'])}")
    