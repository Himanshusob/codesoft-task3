class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = Contact(name, phone, email, address)

    def view_contact_list(self):
        for contact in self.contacts.values():
            print(contact)

    def search_contact(self, query):
        result = [contact for contact in self.contacts.values() if query.lower() in contact.name.lower() or query.lower() in contact.phone.lower()]
        if result:
            for contact in result:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, key, new_value):
        if name in self.contacts:
            setattr(self.contacts[name], key, new_value)
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found.")

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            address_book.add_contact(name, phone, email, address)
        elif choice == "2":
            address_book.view_contact_list()
        elif choice == "3":
            query = input("Enter search query: ")
            address_book.search_contact(query)
        elif choice == "4":
            name = input("Enter name: ")
            key = input("Enter attribute to update (phone, email, address): ")
            new_value = input("Enter new value: ")
            address_book.update_contact(name, key, new_value)
        elif choice == "5":
            name = input("Enter name: ")
            address_book.delete_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()