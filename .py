
PhoneBook = {
    "050123456": "Dana",
    "050456780": "Ahmed",
    "050018273": "Fahad",
    "050678954": "Lulu",
    "050987654": "Sara",
    "0530678785": "Bayan",
    "0566733919": "Ahlam"

}

def find_number_by_name():
    name = input("Enter the name:")
    for number, owner in PhoneBook.items():
        if owner == name:
            print(owner+"'s Number is "+ number)
            break
    else:
        print("invalid Name")

def find_name_by_number():
    PhoneNumber = input("Enter the phone number: ")
    for number, owner in PhoneBook.items():
        if PhoneNumber == number :
            print(owner+"'s Number")
            break
    else:
        print("invalid Number")

def addContact():
    newName = input("Add new Name: ")
    newNum = input("Add new number")
    PhoneBook[newNum]=newName
    print("Contact added successfully .")


def deleteByNumber():
    num = input("Enter number to delete: ")
    if num in PhoneBook:
        del PhoneBook[num]
        print("Contact deleted successfully.")
    else:
        print("Number not found.")


def deleteByName():
    name = input("Enter name to delete: ")
    for num, stored_name in list(PhoneBook.items()):
        if stored_name == name:
            del PhoneBook[num]
            print("Contact deleted successfully.")
            return
    print("Name not found.")

def printAllNames():
    print("Contact Names:")
    for name in PhoneBook.values():
        print(name)


def menu():
    print()

    print("--- Phone Book Menu ---")
    print(" 1- Find Name By Number. ")
    print(" 2- Find Numer By Name. ")
    print(" 3- Add New Contact. ")
    print(" 4- Delete contact By Number. ")
    print(" 5- Delete contact By Name. ")
    print(" 6- Show All Contact Names. ")
    print()
    choice =  input("--- Enter your choice --- ")

    if choice == "1":
        find_name_by_number()

    elif choice == "2":
        find_number_by_name()

    elif choice == "3":
        addContact()

    elif choice == "4":
        deleteByNumber()

    elif choice == "5":
        deleteByName()

    elif choice == "6":
        printAllNames()


    else:
        print("Invalid choice")


    again = input("\nDo you want another operation? (y/n): ")
    if again.lower() == "y":
        menu()
    else:
        print("Program closed")

menu()

