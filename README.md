# Library Management System

A command-line Library Management System built with Python. The application provides separate librarian and library-user portals for account registration, authentication, and basic book-catalogue operations.

The project is being developed as a practical application of Python fundamentals, with an emphasis on translating real library workflows into clear program logic.

> **Project status:** Early working prototype. The current implementation supports basic account and catalogue workflows. Borrowing and return records, persistent storage, and stronger account controls are planned improvements and are not yet fully implemented.

## Table of Contents

- [Overview](#overview)
- [Current Features](#current-features)
- [Technology and Concepts](#technology-and-concepts)
- [Getting Started](#getting-started)
- [Using the Application](#using-the-application)
- [Current Limitations](#current-limitations)
- [Planned Improvements](#planned-improvements)
- [Project Structure](#project-structure)
- [Contributing and Feedback](#contributing-and-feedback)
- [Author](#author)

## Overview

The Library Management System simulates two types of users:

- **Librarians**, who can register, sign in, add books, remove books, and view the catalogue.
- **Library users**, who can register, sign in, view the catalogue, search for books, borrow books, and return books.

The application currently stores account and book information in Python dictionaries and lists while the program is running.

## Current Features

### Account registration and sign-in

- Separate librarian and library-user entry points.
- Username input is converted to lowercase.
- Password validation checks for:
  - At least eight characters.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one non-alphanumeric character.
- Basic username and password authentication.

### Librarian portal

- Add a book title and author to the catalogue.
- Remove a book by title.
- View books in the catalogue.
- Log out of the librarian menu.

### Library-user portal

- View books in the catalogue.
- Search for a book by title, including partial-title searches.
- Borrow a book.
- Return a book.
- Log out of the user menu.

## Technology and Concepts

- **Language:** Python 3
- **Data structures:** Lists and dictionaries
- **Control flow:** Conditional statements and `while` loops
- **Iteration:** `for` loops
- **Functions:** Separate functions for the main menu and role-specific portals
- **Input and output:** `input()` and `print()`
- **String operations:** Lowercase conversion and case-insensitive comparisons
- **Boolean logic:** Password validation and search-result tracking

No third-party packages are required for the current version.

## Getting Started

### Prerequisites

- Python 3 installed on your computer.
- A terminal or code editor.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Victor1tu/library-management-system.git
   ```

2. Change into the project directory:

   ```bash
   cd library-management-system
   ```

3. Run the Python script:

   ```bash
   python master.py
   ```

## Using the Application

When the program starts:

1. Enter your full name when prompted.
2. Select a role:
   - `1` — Librarian
   - `2` — Library user
   - `3` — Exit
3. Register an account using the relevant portal.
4. Sign in with the account credentials.
5. Follow the menu options for the selected role.

### Password requirements

A valid password must contain at least eight characters, including an uppercase letter, a lowercase letter, and a symbol.

For example, `Library@2026` satisfies the current validation rules. Do not use this example as a real password.

## Current Limitations

The following limitations apply to the implementation currently represented by this repository:

- **In-memory storage:** Account and book data are held in Python variables and are lost when the program exits.
- **Shared account storage:** Librarian and user accounts are stored in the same account dictionary. Role-specific account separation has not yet been implemented.
- **Borrowing records:** Borrowing currently removes the matching book from the catalogue instead of retaining the record and changing its availability.
- **Return verification:** Returning a book currently adds a book record from the details entered by the user. The application does not yet verify that the user borrowed that book.
- **Book-copy identification:** Books are identified by title rather than by unique copy IDs. Multiple copies of the same title are not tracked independently.
- **Security:** Passwords are stored as plain text in memory. This is a learning prototype, not a production authentication system.
- **Validation and testing:** Additional validation, automated tests, and more comprehensive error handling are still needed.

These limitations are documented so that the current capabilities are clear; they should not be interpreted as completed functionality.

## Planned Improvements

The next development stages are intended to address the limitations above:

1. **Book availability tracking:** Keep borrowed books in the catalogue and update an availability field instead of deleting their records.
2. **Borrower tracking:** Associate each borrowed book copy with the username of the borrower.
3. **Return validation:** Allow only the original borrower to return a borrowed copy.
4. **Unique book IDs:** Track individual copies so multiple copies of the same title can be managed correctly.
5. **Role-based account separation:** Maintain separate librarian and user account records and apply appropriate permissions.
6. **Input validation:** Handle blank values, invalid menu selections, duplicate records, and unexpected input.
7. **Persistent storage:** Save account and catalogue data between application runs, initially using files and potentially a database later.
8. **Code organisation:** Extract repeated operations into reusable functions and organise the application into appropriate modules.
9. **Testing:** Add test cases for normal workflows, invalid inputs, borrowing conflicts, and return rules.
10. **Improved security:** Replace plain-text password storage with an appropriate password-hashing approach before treating authentication as more than a demonstration.

Planned items are future work and are not claimed as features of the current version.

## Project Structure

The current project can be kept simple:

```text
library-management-system/
├── Library_Management_System.py
├── README.md
└── .gitignore
```

As the application grows, its code and tests can be separated into modules and folders.

## Contributing and Feedback

This is an actively developing project. Constructive feedback, bug reports, and suggestions for improving the design and functionality are welcome.

If you identify an issue, please include the steps to reproduce it and the expected behaviour.

## Author

**Akinwale Abayomi Victor**


