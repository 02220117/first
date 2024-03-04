#initialize empty lists,set and dictionary
books_list=[]
author_set=set()
books_dict={}

#add books
books_list.append("python programming")
author_set.add("Joahn Smith")
books_dict["python programming"]="Joahn Smith"

books_list.append("Data Structure and Algorithms")
author_set.add("Jane Doe")
books_dict["Data Structure and Algorithms"]="Jane Doe"

books_list.append("Machine Learning Basics")
author_set.add("Alice Johnson")
books_dict["Machine Learning Basics"]="Alice Johnson"

#search for book
search_title=input("Enter the title of the book to search:")
if search_title in books_list:
    print(f"book found! Author:{books_dict[search_title]}")

else:
    print("book not found!")

#display all books
    print("List of Books:")

for book in books_list:
    print(book)