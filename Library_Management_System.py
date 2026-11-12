log_in_details = {}
books = []

def lib_portal(full_name):
    global log_in_details, books

    while True:
        print(f"\nWelcome {full_name}, to the library registration portal")

        option = input(
            "What would you like to do?\n"
            "1. Sign Up\n"
            "2. Sign In\n"
            "3. Exit\n: "
        )

        # SIGN UP
        if option == "1":
            user_name = input("Enter your username: ").lower()

            password = input(
                "Enter a unique password:\n"
                "(Must contain uppercase, lowercase, symbol, and be at least 8 characters long)\n: "
            )

            upper = False
            lower = False
            symbol = False
           
            for char in password:
                if char.isupper():
                    upper = True
                if char.islower():
                    lower = True
                if not char.isalnum():
                    symbol = True

            if user_name in log_in_details:
                print("Username already exists!")
                print("Try again.")

            elif upper and lower and symbol and len(password) >= 8:
                log_in_details[user_name] = password
                print("Sign up successful!")
                print(log_in_details)

            else:
                print("Password requirements not met.")
                print("Sign up failed.")

        # SIGN IN
        elif option == "2":
            print("\nLog In")

            user_name = input("Enter username: ").lower()
            lib_password = input("Enter password: ")

            if (
                user_name in log_in_details
                and log_in_details[user_name] == lib_password
            ):

                print(f"Welcome {user_name}")
                print("Login successful.")

                while True:
                    choice = input(
                        "\nWhat would you like to do?\n"
                        "1. Add a Book\n"
                        "2. Remove a Book\n"
                        "3. View Books\n"
                        "4. Logout\n: "
                    )

                    # ADD BOOK
                    if choice == "1":
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")

                        books.append({
                            "Title": title,
                            "Author": author
                        })

                        print("Book added successfully.")

                    # REMOVE BOOK
                    elif choice == "2":
                        title = input(
                            "Enter the title of the book to remove: "
                        )

                        found = False

                        for book in books:
                            if book["Title"].lower() == title.lower():
                                books.remove(book)
                                print(f"{title} removed successfully.")
                                found = True
                                break

                        if not found:
                            print("Book not found.")

                    # VIEW BOOKS
                    elif choice == "3":
                        if not books:
                            print("No books available.")
                        else:
                            print("\nAvailable Books:")
                            for book in books:
                                print(
                                    f"Title: {book['Title']} | "
                                    f"Author: {book['Author']}"
                                )

                    # LOGOUT
                    elif choice == "4":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid option.")

            else:
                print("Username or password incorrect.")

        # EXIT
        elif option == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

def user_portal(full_name):
    global log_in_details, books

    while True:
        print(f"\nWelcome {full_name}, to the user registration portal")

        option = input(
            "What would you like to do?\n"
            "1. Sign Up\n"
            "2. Sign In\n"
            "3. Exit\n: "
        )

        # SIGN UP
        if option == "1":
            user_name = input("Enter your username: ").lower()

            password = input(
                "Enter a unique password:\n"
                "(Must contain uppercase, lowercase, symbol, and be at least 8 characters long)\n: "
            )

            upper = False
            lower = False
            symbol = False
                       
            for char in password:
                if char.isupper():
                    upper = True
                if char.islower():
                    lower = True
                if not char.isalnum():
                    symbol = True

            if user_name in log_in_details:
                print("Username already exists!")
                print("Try again.")

            elif upper and lower and symbol and len(password) >= 8:
                log_in_details[user_name] = password
                print("Sign up successful!")

            else:
                print("Password requirements not met.")
                print("Sign up failed.")

        # SIGN IN
        elif option == "2":
            print("\nLog In")

            user_name = input("Enter username: ").lower()
            password = input("Enter password: ")

            if (
                user_name in log_in_details
                and log_in_details[user_name] == password
            ):

                print("Login successful!")

                while True:
                    choice = input(
                        "\nWhat would you like to do?\n"
                        "1. View all books\n"
                        "2. Borrow a book\n"
                        "3. Search for a book\n"
                        "4. Return a book\n"
                        "5. Logout\n: "
                    )

                    # VIEW ALL BOOKS
                    if choice == "1":
                        if not books:
                            print("No books available.")
                        else:
                            print("\nAvailable Books:")
                            for book in books:
                                print(
                                    f"Title: {book['Title']} | "
                                    f"Author: {book['Author']}"
                                )

                    # BORROW BOOK
                    elif choice == "2":
                        title = input("Enter title of book to borrow: ")

                        found = False
                        for book in books:
                            if book["Title"].lower() == title.lower():
                                books.remove(book)
                                print(f"You borrowed '{title}'.")
                                found = True
                                break

                        if not found:
                            print("Book not found.")

                    # SEARCH BOOK
                    elif choice == "3":
                        title = input("Enter book title to search: ")

                        found = False
                        for book in books:
                            if title.lower() in book["Title"].lower():
                                print(
                                    f"Found: {book['Title']} "
                                    f"by {book['Author']}"
                                )
                                found = True

                        if not found:
                            print("Book not found.")

                    # RETURN BOOK
                    elif choice == "4":
                        title = input("Enter book title: ")
                        author = input("Enter author name: ")

                        books.append({
                            "Title": title,
                            "Author": author
                        })

                        print("Book returned successfully.")

                    # LOGOUT
                    elif choice == "5":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid option.")

            else:
                print("Username or password incorrect.")

        # EXIT
        elif option == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")
        
def LMS():
    while True:
        print("""
Welcome to the Library Management System

Enter your full name and select your role:
1. Librarian
2. User
3. Exit
        """)

        full_name = input("Enter full name (surname first): ").lower()
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Welcome {full_name}, to the library.")
            lib_portal(full_name)

        elif choice == "2":
            print(f"Welcome {full_name}.")
            user_portal(full_name)

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
LMS()