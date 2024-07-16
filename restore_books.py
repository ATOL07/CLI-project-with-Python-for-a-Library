# def restore_books(library_book):
#     library_book.clear()
#     with open("books.csv", "r") as file_pointer:
#         book = {}
#         for line in file_pointer.readlines():
#             line = line.strip()
#             if line.startswith("Title:"):
#                 book = {"title": line.split(": ", 1)[1]}
#             elif line.startswith("Author(s):"):
#                 book["author(s)"] = line.split(": ", 1)[1]
#             elif line.startswith("Year Published:"):
#                 book["year_published"] = line.split(": ", 1)[1]
#             elif line.startswith("Price:"):
#                 book["price"] = line.split(": ", 1)[1]
#             elif line.startswith("Available quantity:"):
#                 book["quantity"] = int(line.split(": ", 1)[1])
#             elif line.startswith("Pages:"):
#                 book["pages"] = line.split(": ", 1)[1]
#             elif line.startswith("ISBN:"):
#                 book["ISBN"] = line.split(": ", 1)[1]
#             elif line.startswith("Genres:"):
#                 book["genres"] = line.split(": ", 1)[1].split(", ")
#             elif line.startswith("Borrowers:"):
#                 if "borrowers" not in book:
#                     book["borrowers"] = []
#                 parts = line.split(": ", 1)
#                 if len(parts) > 1:
#                     borrower = parts[1]
#                     if borrower != "None":
#                         book["borrowers"].append({"name": borrower.strip("- ").strip()})
#             elif line.startswith("Status:"):
#                 if line.split(": ", 1)[1] == "Removed":
#                     book["removed"] = True
#                 else:
#                     book["removed"] = False
#             elif line == "-------------------":
#                 if book:
#                     library_book.append(book)

#     print("Contact Restore.")
#     return library_book

# restore_books.py

def restore_books(library_book):
    try:
        # Implement your restoration logic here
        # Example: Read from a backup file and populate library_book
        
        # For demonstration, let's assume we're reading from a CSV file
        with open("books.csv", "rt") as file_pointer:
            # Clear existing library_book to avoid duplicates
            library_book.clear()
            
            for line in file_pointer:
                if line.startswith("Title:"):
                    book = {}
                    book['title'] = line.strip().split(": ")[1]
                    book['author(s)'] = file_pointer.readline().strip().split(": ")[1]
                    book['year_published'] = file_pointer.readline().strip().split(": ")[1]
                    book['price'] = file_pointer.readline().strip().split(": ")[1]
                    book['quantity'] = file_pointer.readline().strip().split(": ")[1]
                    book['pages'] = file_pointer.readline().strip().split(": ")[1]
                    book['ISBN'] = file_pointer.readline().strip().split(": ")[1]
                    book['genres'] = file_pointer.readline().strip().split(": ")[1].split(", ")
                    
                    # Read borrowers if available
                    line = file_pointer.readline().strip()
                    if line.startswith("Borrowers:"):
                        borrowers = []
                        while line.startswith("- "):
                            borrowers.append({"name": line.strip().split("- ")[1]})
                            line = file_pointer.readline().strip()
                        book['borrowers'] = borrowers
                    
                    # Read status or removed if available
                    if line.startswith("Status:"):
                        book['status'] = line.strip().split(": ")[1]
                    elif line.startswith("Status2:"):
                        book['status2'] = line.strip().split(": ")[1]
                    elif line.startswith("Status: Removed"):
                        book['removed'] = True
                    
                    library_book.append(book)
        
        print("Books have been restored successfully.")
    
    except Exception as e:
        print(f"An unexpected error occurred during restoration: {e}")
    
    return library_book
