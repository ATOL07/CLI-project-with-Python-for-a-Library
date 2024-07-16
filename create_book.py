# def create_book(library_book):
#     try:
#         title = input("Enter book title: ").strip()
#         if not title:
#             raise ValueError("Title cannot be empty.")
        
#         author = input("Enter author(s): ").strip()
#         if not author:
#             raise ValueError("Author(s) cannot be empty.")
        
#         year_published = int(input("Enter year published: "))
#         if year_published < 0:
#             raise ValueError("Year published cannot be negative.")
        
#         price = float(input("Enter price: "))
#         if price <= 0:
#             raise ValueError("Price must be greater than zero.")
        
#         quantity = int(input("Enter available quantity: "))
#         if quantity < 0:
#             raise ValueError("Quantity cannot be negative.")
        
#         pages = int(input("Enter number of pages: "))
#         if pages <= 0:
#             raise ValueError("Number of pages must be greater than zero.")
        
#         ISBN = input("Enter ISBN: ").strip()
#         if not ISBN:
#             raise ValueError("ISBN cannot be empty.")
        
#         genres = [g.strip() for g in input("Enter genres separated by comma: ").split(",")]
#         if not genres:
#             raise ValueError("At least one genre must be specified.")
        
#         book = {
#             "title": title,
#             "author(s)": author,
#             "year_published": year_published,
#             "price": price,
#             "quantity": quantity,
#             "pages": pages,
#             "ISBN": ISBN,
#             "genres": genres,
#             "borrowers": [],
#             "removed": False
#         }

     
#         library_book.append(book)
        
#         print("New book created successfully.")
        
        
#         book['status'] = "This is newly arrived book!!"

#     except ValueError as ve:
#         print(f"ValueError: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return library_book       

def create_book(library_book):
    try:
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
        
        book = {
            "title": title,
            "author(s)": author,
            "year_published": year_published,
            "price": price,
            "quantity": quantity,
            "pages": pages,
            "ISBN": ISBN,
            "genres": genres,
            "borrowers": [],
            "removed": False
        }
     
        library_book.append(book)
        
        print("New book created successfully.")
        book['status'] = "This is a newly arrived book!!"

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return library_book  # Ensure the updated list is returned






