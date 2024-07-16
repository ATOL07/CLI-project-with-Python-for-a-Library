def search_books(library_book):
    try:
        search_query = input("Enter book title or ISBN: ").strip().lower()
        if not search_query:
            raise ValueError("Search query cannot be empty.")
        
        found_books = []
        for book in library_book:
            if not book.get('removed', False):  # Skip removed books
                if (search_query in book['title'].lower()) or (search_query in book['ISBN'].lower()):
                    found_books.append(book)
        
        if not found_books:
            print("No books found matching the search query.")
            return
        
        print("Found book(s):")
        for book in found_books:
            print("-------------------")
            print(f"Title: {book['title']}")
            print(f"Author(s): {book['author(s)']}")
            print(f"Year Published: {book['year_published']}")
            print(f"Price: {book['price']}")
            print(f"Available quantity: {book['quantity']}")
            print(f"Pages: {book['pages']}")
            print(f"ISBN: {book['ISBN']}")
            print(f"Genres: {', '.join(book['genres'])}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
