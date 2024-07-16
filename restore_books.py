
def restore_books(library_book):
    try:
        with open("books.csv", "rt") as file_pointer:
            
            library_book.clear()
            
            book = None
            for line in file_pointer:
                if line.startswith("Title:"):
                    if book:
                        library_book.append(book)
                    book = {}
                    book['title'] = line.strip().split(": ")[1]
                elif line.startswith("Author(s):"):
                    book['author(s)'] = line.strip().split(": ")[1]
                elif line.startswith("Year Published:"):
                    book['year_published'] = int(line.strip().split(": ")[1])
                elif line.startswith("Price:"):
                    book['price'] = float(line.strip().split(": ")[1])
                elif line.startswith("Available quantity:"):
                    book['quantity'] = int(line.strip().split(": ")[1])
                elif line.startswith("Pages:"):
                    book['pages'] = int(line.strip().split(": ")[1])
                elif line.startswith("ISBN:"):
                    book['ISBN'] = line.strip().split(": ")[1]
                elif line.startswith("Genres:"):
                    book['genres'] = line.strip().split(": ")[1].split(", ")
                elif line.startswith("Borrowers:"):
                    borrowers = []
                    while True:
                        line = file_pointer.readline().strip()
                        if line.startswith("- "):
                            borrowers.append({"name": line.split("- ")[1]})
                        else:
                            break
                    book['borrowers'] = borrowers
                    continue  # Skip the line that was just read
                elif line.startswith("Status: Removed"):
                    book['removed'] = True
                elif line.startswith("Status:"):
                    book['status'] = line.strip().split(": ")[1]
                elif line.startswith("Status2:"):
                    book['status2'] = line.strip().split(": ")[1]
                elif line == "-------------------":
                    if book:
                        library_book.append(book)
                    book = None
        
        
        if book:
            library_book.append(book)
        
        print("Books have been restored successfully.")
    
    except Exception as e:
        print(f"An unexpected error occurred during restoration: {e}")
    
    return library_book

