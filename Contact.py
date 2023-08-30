class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' removed successfully.")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
                print("------------------------")


# Create a ContactManager object
manager = ContactManager()

# Loop to allow the user to add multiple contacts
while True:
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Search for a contact")
    print("4. Display all contacts")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Get contact details from the user
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        # Create a Contact object and add it to the ContactManager
        contact = Contact(name, phone, email)
        manager.add_contact(contact)
        print("Contact added successfully.")

    elif choice == "2":
        # Get the name of the contact to remove
        name = input("Enter the name of the contact to remove: ")
        manager.remove_contact(name)

    elif choice == "3":
        # Get the name of the contact to search for
        name = input("Enter the name of the contact to search for: ")
        search_result = manager.search_contact(name)
        if search_result:
            print("Contact found:")
            print(search_result)
        else:
            print("Contact not found.")

    elif choice == "4":
        # Display all contacts
        manager.display_contacts()

    elif choice == "5":
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")