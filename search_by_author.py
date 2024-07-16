def search_book_by_author(library_book):
    try:
        author = input("Enter author's name: ").strip()
        if not author:
            raise ValueError("Author's name cannot be empty.")
        
        found_books = [book for book in library_book if not book.get('removed', False) and author.lower() in book['author(s)'].lower()]
        
        if not found_books:
            print("No books found by the author.")
            return
        
        if len(found_books) == 1:
            print("\nFound book by the author(s):")
            book = found_books[0]
            print(f"Title: {book['title']}")
            print(f"Author(s): {book['author(s)']}")
            print(f"Year Published: {book['year_published']}")
            print(f"Price: {book['price']}")
            print(f"Available quantity: {book['quantity']}")
            print(f"Pages: {book['pages']}")
            print(f"ISBN: {book['ISBN']}")
            print(f"Genres: {', '.join(book['genres'])}")
        else:
            print("Multiple books found by the author:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book['title']}, Author(s): {book['author(s)']}, ISBN: {book['ISBN']}")
                print(f"Year Published: {book['year_published']}")
                print(f"Price: {book['price']}")
                print(f"Available quantity: {book['quantity']}")
                print(f"Pages: {book['pages']}")
                print(f"Genres: {', '.join(book['genres'])}")
                print("-------------------")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")