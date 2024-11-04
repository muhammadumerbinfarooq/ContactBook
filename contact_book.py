# Step 1: Setting Up the Contact Book
contacts = []

# Step 2: Adding Contacts
def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print(f"Contact {name} added.")

# Step 3: Viewing Contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Step 4: Searching for Contacts
def search_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print(f"No contact found with the name {name}.")

# Step 5: Deleting Contacts
def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} deleted.")
            return
    print(f"No contact found with the name {name}.")

# Example usage
add_contact('Alice', '123-456-7890', 'alice@example.com')
add_contact('Bob', '987-654-3210', 'bob@example.com')
view_contacts()
search_contact('Alice')
delete_contact('Alice')
view_contacts()
