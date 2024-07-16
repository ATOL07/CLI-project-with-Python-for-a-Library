def return_book(library_book):
    try:
        search_term = input("Enter search term (title, author, or ISBN): ").strip().lower()
        
        found_books = [
            book for book in library_book 
            if not book.get('removed', False) and (
                search_term in book['title'].lower() 
                or search_term in book['author(s)'].lower() 
                or search_term in book['ISBN'].lower()
            )
        ]
        
        if not found_books:
            print(f"No book found matching the term '{search_term}'.")
            return
        
        if len(found_books) == 1:
            book = found_books[0]
            print(f"Found book:\nTitle: {book['title']}\nAuthor(s): {book['author(s)']}\nISBN: {book['ISBN']}\nAvailable quantity: {book['quantity']}")
        else:
            print("Multiple books found:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book['title']}, Author(s): {book['author(s)']}, ISBN: {book['ISBN']}")
            choice = int(input("Select the book to return (number): "))
            book = found_books[choice - 1]
        
        borrower_name = input("Enter the name of the borrower: ")
        
        try:
            quantity_to_return = int(input(f"Enter quantity to return for '{book['title']}': "))
            if quantity_to_return <= 0:
                print("Quantity must be a positive integer.")
                return
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return
        
        borrower_record = next((borrower for borrower in book['borrowers'] if borrower['name'] == borrower_name), None)
        
        if not borrower_record:
            print(f"No record of {borrower_name} borrowing '{book['title']}'.")
            return
        
        book['quantity'] += quantity_to_return
        print(f"Book '{book['title']}' has been returned successfully by {borrower_name}. Quantity returned: {quantity_to_return}.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return library_book