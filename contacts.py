contacts = {
    "Jordan": "08012345678",
    "Ada": "08087654321"
}

def add_contact(name, number):
    contacts[name] = number
    save_contacts()
    print(f"{name} added!")

def find_contact(name):
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print(f"{name} not found.")

import json

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        pass

load_contacts()

while True:
    print("\n1. Add contact\n2. Find contact\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == "2":
        name = input("Enter name to find: ")
        find_contact(name)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")