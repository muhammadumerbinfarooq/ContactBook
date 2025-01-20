# Contact Book

A simple contact book application written in Python. This project allows users to add, view, search, and delete contacts.

## Description

The Contact Book is an interactive Python script where users can manage their contacts by adding, viewing, searching, and deleting them. It's a great way to practice Python programming and manage contact information efficiently.

## Features

- **Add Contact**: Add a new contact with name, phone number, and email.
- **View Contacts**: View all contacts in the contact book.
- **Search Contact**: Search for contacts by name.
- **Delete Contact**: Delete a contact by name.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**
    ```bash
    https://github.com/muhammadumerbinfarooq/ContactBook.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd contact-book
    ```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please feel free to submit an issue or a pull request. Here are some ways you can contribute:

- Report bugs and issues.
- Suggest new features or enhancements.
- Improve documentation.
- Submit pull requests with improvements or fixes.

## Usage

1. Run the script:
    ```bash
    python contact_book.py
    ```

2. Use the following functions to interact with the contact book:

    - **Add a Contact**:
        ```python
        add_contact('Alice', '123-456-7890', 'alice@example.com')
        ```

    - **View All Contacts**:
        ```python
        view_contacts()
        ```

    - **Search for a Contact**:
        ```python
        search_contact('Alice')
        ```

    - **Delete a Contact**:
        ```python
        delete_contact('Alice')
        ```

## Example

```python
# Example usage
add_contact('Alice', '123-456-7890', 'alice@example.com')
add_contact('Bob', '987-654-3210', 'bob@example.com')
view_contacts()
search_contact('Alice')
delete_contact('Alice')
view_contacts()
