import create_book
import view_all_books
import remove_book
import search_books
import search_by_author
import return_book
import rent_books_by_all
import update_book
import backup_book
import restore_books

        
library_book = []

def book_lent_to_someone():
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
            choice = int(input("Select the book to lend (number): "))
            book = found_books[choice - 1]
        
        borrower_name = input("Enter the name of the borrower: ")
        
        try:
            quantity_to_lend = int(input(f"Enter quantity to lend for '{book['title']}': "))
            if quantity_to_lend <= 0:
                print("Quantity must be a positive integer.")
                return
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return
        
        if book['quantity'] >= quantity_to_lend:
            book['quantity'] -= quantity_to_lend
            book['borrowers'].append({"name": borrower_name})
            print(f"Book '{book['title']}' has been lent out successfully to {borrower_name}. Quantity lent: {quantity_to_lend}.")
        else:
            print(f"Not enough stock for '{book['title']}'. Available quantity: {book['quantity']}.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
          

 
print("Welcome to the Library management System")

menu_text="""
Your options:
1. Add a new book
2. View all books
3. Search for a book
4. Search for a book by author
5. Remove Book
6. Lend a book to someone
7. Return a book
8. View all lent books
9. Update a book
10. Backup Books
11. Restore Books
0.Exit

Please enter your choice (1-11): """


while True:
 print(menu_text)
 choice=input("Enter your choice: ")

 if choice =="1":
    library_book=create_book.create_book(library_book)
 elif choice=="2":
    view_all_books.view_all_books(library_book)  
 elif choice=="3":
    search_books.search_books(library_book)
 elif choice=="4":
    search_by_author.search_book_by_author(library_book)
 elif choice=="5":
    library_book= remove_book.remove_book(library_book)
 elif choice=="6":
   book_lent_to_someone()
 elif choice=="7":
    library_book=return_book.return_book(library_book)
 elif choice=="8":
    library_book=rent_books_by_all.all_lent_books(library_book)
 elif choice=="9":
    library_book=update_book.update_book(library_book)
 elif choice=="10":
    backup_book.backup_book(library_book)
 elif choice=="11":
    library_book = restore_books.restore_books(library_book)
 elif choice=="0":
     break   
 else:
    print("Wrong choice!!!Please select the right one.")
          
        
    




    





  
  
  
        
    
      
       
   
            
     

          