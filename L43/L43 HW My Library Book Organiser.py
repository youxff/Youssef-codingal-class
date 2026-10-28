# Library Book Organiser

library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")

    book = {
        "title": title,
        "author": author
    }

    library.append(book)
    print("Book added successfully!\n")


def view_books():
    if not library:
        print("No books in the library.\n")
        return

    print("\nLibrary Books:")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} by {book['author']}")
    print()


def search_book():
    title = input("Enter book title to search: ")

    for book in library:
        if book["title"].lower() == title.lower():
            print(f"Found: {book['title']} by {book['author']}\n")
            return

    print("Book not found.\n")


def remove_book():
    title = input("Enter book title to remove: ")

    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return

    print("Book not found.\n")


while True:
    print("=== Library Book Organiser ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")