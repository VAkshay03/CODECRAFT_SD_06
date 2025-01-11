import pickle

# Contact class to represent a contact
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Function to save contacts to a file
def save_contacts(contacts, filename="contacts.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(contacts, f)

# Function to load contacts from a file
def load_contacts(filename="contacts.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    
    contact = Contact(name, phone, email)
    contacts.append(contact)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")

# Function to edit an existing contact
def edit_contact(contacts):
    if not contacts:
        print("No contacts available to edit.")
        return

    view_contacts(contacts)
    contact_id = int(input("Enter the contact number to edit: ")) - 1
    
    if 0 <= contact_id < len(contacts):
        print(f"Editing contact: {contacts[contact_id].name}")
        name = input(f"Enter new name (current: {contacts[contact_id].name}): ")
        phone = input(f"Enter new phone number (current: {contacts[contact_id].phone}): ")
        email = input(f"Enter new email (current: {contacts[contact_id].email}): ")

        contacts[contact_id].name = name if name else contacts[contact_id].name
        contacts[contact_id].phone = phone if phone else contacts[contact_id].phone
        contacts[contact_id].email = email if email else contacts[contact_id].email
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Function to delete a contact
def delete_contact(contacts):
    if not contacts:
        print("No contacts available to delete.")
        return

    view_contacts(contacts)
    contact_id = int(input("Enter the contact number to delete: ")) - 1

    if 0 <= contact_id < len(contacts):
        deleted_contact = contacts.pop(contact_id)
        print(f"Contact '{deleted_contact.name}' deleted successfully!")
    else:
        print("Invalid contact number.")

# Main menu
def menu():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
