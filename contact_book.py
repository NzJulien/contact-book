


contact_book = {}
def add_contact(name,number,address):
    if name in contact_book:
        raise Exception("Contact exists!")
    else:
        contact_book[name] = {"number": number, "address": address}
def edit_contact(name,number,address):
    if name not in contact_book:
        raise Exception("Name not Found!")
    else:
        contact_book[name]["number"] = number
        contact_book[name]["address"] = address
def list_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        for name, info in contact_book.items():
            print(f"Name: {name}")
            print(f"Number: {info['number']}")
            print(f"Address: {info['address']}")
            print("-" * 20)
add_contact("Julien","680380156","C8")
list_contacts()