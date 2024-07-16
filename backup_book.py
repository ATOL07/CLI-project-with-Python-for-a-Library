
def backup_book(library_book):
    try:
        with open("books.csv", "wt") as file_pointer:
            for book in library_book:
                line = (f"Title: {book['title']}\n"
                        f"Author(s): {book['author(s)']}\n"
                        f"Year Published: {book['year_published']}\n"
                        f"Price: {book['price']}\n"
                        f"Available quantity: {book['quantity']}\n"
                        f"Pages: {book['pages']}\n"
                        f"ISBN: {book['ISBN']}\n"
                        f"Genres: {', '.join(book['genres'])}\n")
                
                if book.get('borrowers'):
                    line += "Borrowers:\n"
                    for borrower in book['borrowers']:
                        line += f"- {borrower['name']}\n"
                else:
                    line += "Borrowers: None\n"
                
                if book.get('removed', False):
                    line += "Status: Removed\n"
                elif book.get('status'):
                    line += f"Status: {book['status']}\n"
                elif book.get('status2'):
                    line += f"Status: {book['status2']}\n"
                
                line += "-------------------\n"
                file_pointer.write(line)
        
        print("Books are backed up successfully.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return library_book
