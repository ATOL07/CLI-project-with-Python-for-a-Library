def book_lent_to_someone(library_book):
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
            return library_book

        if len(found_books) > 1:
            print("Multiple books found:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book['title']}, Author(s): {book['author(s)']}, ISBN: {book['ISBN']}")
            choice = int(input("Select the book to lend (number): "))
            book = found_books[choice - 1]
        else:
            book = found_books[0]

        borrower_name = input("Enter the name of the borrower: ").strip()

        try:
            quantity_to_lend = int(input(f"Enter quantity to lend for '{book['title']}': "))
            if quantity_to_lend <= 0:
                print("Quantity must be a positive integer.")
                return library_book
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return library_book

        book_quantity = int(book['quantity'])

        if book_quantity < quantity_to_lend:
            print(f"Not enough stock for '{book['title']}'. Available quantity: {book_quantity}.")
            return library_book

        # Initialize 'borrowers' list if it doesn't exist
        if 'borrowers' not in book:
            book['borrowers'] = []

        # Check if borrower already exists
        existing_borrowers = {borrower['name'].lower() for borrower in book['borrowers']}
        if borrower_name.lower() in existing_borrowers:
            print(f"{borrower_name} already has a copy of '{book['title']}'")
        else:
            # Add borrower to 'borrowers' list
            for _ in range(quantity_to_lend):
                book['borrowers'].append({"name": borrower_name})
            print(f"Book '{book['title']}' has been lent out successfully to {borrower_name}. Quantity lent: {quantity_to_lend}.")

        # Update book quantity after lending
        book['quantity'] -= quantity_to_lend

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except IndexError:
        print("Invalid selection. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return library_book
