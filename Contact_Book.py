# Contact Book
import json
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        for c in self.contacts:
            if c.name.lower() == contact.name.lower():
                print("Already exists")
                return
        self.contacts.append(contact)

    def search(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                print(c)
                return
        print("Not found")

    def delete(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                print("Deleted")
                return
        print("Not found")

    def show_contacts(self):
        for c in self.contacts:
            print(c)

    def save(self, filename):
        data = []
        for c in self.contacts:
            data.append({"name": c.name, "phone": c.phone})
        with open(filename, "w") as f:
            json.dump(data, f)

    def load(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for d in data:
                    contact = Contact(d["name"], d["phone"])
                    self.contacts.append(contact)
        except FileNotFoundError:
            print("No saved contacts yet")

book = ContactBook()
book.load("contacts.json")

while True:
    print("\n1. Add Contact")
    print("2. Search")
    print("3. Delete")
    print("4. Show Contact")
    print("5. Exit")
    choice = input("Choose").strip()
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        book.add_contact(Contact(name, phone))
    elif choice == "2":
        name = input("Name: ")
        book.search(name)
    elif choice == "3":
        name = input("Name: ")
        book.delete(name)
    elif choice == "4":
        book.show_contacts()
    elif choice == "5":
        book.save("contacts.json")
        print("Saved. Bye")
        break
    else:
        print("Invalid choice")