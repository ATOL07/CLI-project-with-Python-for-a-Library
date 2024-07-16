def remove_book(library_book):
    try:
        if not library_book:
            print("The library is currently empty. No books to remove.")
            return
        
        search_query = input("Enter book title or ISBN: ").strip().lower()
        if not search_query:
            raise ValueError("Search query cannot be empty.")
        
        found_books = []
        for book in library_book:
            if (search_query in book['title'].lower()) or (search_query in book['ISBN'].lower()):
                found_books.append(book)
        
        if not found_books:
            print("No books found matching the search query.")
            return
        
        if len(found_books) == 1:
            book = found_books[0]
            book['removed'] = True
            print(f"Book '{book['title']}' has been removed.")
        else:
            print("Multiple books found:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book['title']}, Author(s): {book['author(s)']}, ISBN: {book['ISBN']}")
            
            while True:
                try:
                    choice = int(input("Select the book to remove (number): "))
                    if 1 <= choice <= len(found_books):
                        book = found_books[choice - 1]
                        book['removed'] = True
                        print(f"Book '{book['title']}' has been removed.")
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(found_books)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return library_book