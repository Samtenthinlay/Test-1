books_list = []
authors_set = set()
books_dict = {}

books_list.append("Python programming")
authors_set.add("John Smith")
books_dict["Python programming"] = "John Smith"

books_list.append("Data Structure and Algorithum")
authors_set.add("Jane Doe")
books_dict["Data Structure and Algorithum"] = "Jane Doe"

books_list.append("Machine Learing Basic")
authors_set.add("Alice")
books_dict["Machine Learing Basic"] = "Alice"

search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Autor: {books_dict[search_title]}")
else:
    print("Book not found")

print("List of Books: ")
for book in books_list:
    print(book)

remove_title = input("Enter the title of the book to remove or else enter the skip:")
if remove_title in books_list:
   remove_autor = books_dict[remove_title]
   books_list.remove(remove_title) 
   authors_set.remove(remove_author)
   del books_dict[remove_title]
   print("Book removed successfully!")
   print("Books available;", books_list)
else:
    print("Book not found!")