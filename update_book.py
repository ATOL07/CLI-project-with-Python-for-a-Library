def update_book(library_book):
    try:
        search_term = input("Enter search term (title, author, or ISBN): ").strip().lower()

        if not search_term:
            raise ValueError("Search term cannot be empty.")

        found_books = [
            book for book in library_book
            if not book.get('removed', False) and (
                search_term in book.get('title', '').lower()
                or search_term in book.get('author(s)', '').lower()
                or search_term in book.get('ISBN', '').lower()
            )
        ]

        if not found_books:
            print(f"No book found matching the term '{search_term}'.")
            return

        if len(found_books) == 1:
            print("\nFound book:")
            book = found_books[0]
            print(f"Title: {book['title']}, Author(s): {book['author(s)']}, ISBN: {book['ISBN']}, Available quantity: {book['quantity']}")
        
        elif len(found_books) > 1:
            print("Multiple books found:")
            for i, b in enumerate(found_books, 1):
                print(f"{i}. Title: {b['title']}, Author(s): {b['author(s)']}, ISBN: {b['ISBN']}, Available quantity: {b['quantity']}")
            choice = int(input("Select the book to update (number): "))
            if 1 <= choice <= len(found_books):
                book = found_books[choice - 1]
            else:
                print("Invalid choice. Please select a valid number.")
                return
        else:
            return

        print("Update the book with accordance!")
        title = input("Enter book title: ").strip()
        if not title:
            raise ValueError("Title cannot be empty.")

        author = input("Enter author(s): ").strip()
        if not author:
            raise ValueError("Author(s) cannot be empty.")

        year_published = int(input("Enter year published: "))
        if year_published < 0:
            raise ValueError("Year published cannot be negative.")

        price = float(input("Enter price: "))
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        quantity = int(input("Enter available quantity: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        pages = int(input("Enter number of pages: "))
        if pages <= 0:
            raise ValueError("Number of pages must be greater than zero.")

        ISBN = input("Enter ISBN: ").strip()
        if not ISBN:
            raise ValueError("ISBN cannot be empty.")

        genres = [g.strip() for g in input("Enter genres separated by comma: ").split(",")]
        if not genres:
            raise ValueError("At least one genre must be specified.")

        # Check if any fields are actually updated
        if (book['title'] != title or
            book['author(s)'] != author or
            book['year_published'] != year_published or
            book['price'] != price or
            book['quantity'] != quantity or
            book['pages'] != pages or
            book['ISBN'] != ISBN or
            book['genres'] != genres):
            book['title'] = title
            book['author(s)'] = author
            book['year_published'] = year_published
            book['price'] = price
            book['quantity'] = quantity
            book['pages'] = pages
            book['ISBN'] = ISBN
            book['genres'] = genres
            book['status'] = 'Updated'  # Set the status to "Updated"
            print("Book details updated successfully.")

        update_borrowers = input("Do you want to update the borrowers? (yes/no): ").strip().lower()
        if update_borrowers == "yes":
            borrowers = []
            while True:
                borrower_name = input("Enter borrower's name (leave empty to finish): ").strip()
                if not borrower_name:
                    break
                borrowers.append({"name": borrower_name})
            book['borrowers'] = borrowers
            book['status'] = 'Updated'  # Set the status to "Updated" if borrowers are updated
            print("Borrowers updated successfully.")
        elif update_borrowers == "no":
            print("Borrowers not updated.")
        else:
            print("Invalid input. Borrowers not updated.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return library_book