def menu():
    print("Welcome to the simple addressbook system.")
    print("")
    print("1.Add Address")
    print("2.Search Address")
    print("3.Quit")
    choice = input("Please enter your choice.")
    if choice == "1":
        print("Option 1 selected.")
        addAddress()
    elif choice == "2":
        print("Option 2 selected.")
        searchMenu()
    elif choice == "3":
        print("Option 3 selected. Thank you for using our service.")
    else:
        print("Sorry, we do not support that.")
        menu()


def addAddress():
    surname = input("Surname:")
    firstname = input("Firstname:")
    addressL1 = input("First line of address:")
    addressL2 = input("Second line of address:")
    postcode = input("Postcode:")
    telephone = input("Telephone number:")
    dob = input("Date of birth:")
    email = input("Email:")
    record = surname + "," + firstname + "," + addressL1 + "," + addressL2 + "," + postcode + "," + telephone + "," + dob + "," + email + "\n"
    with open("addressbook.csv", "a") as file:
        file.write(record)
        file.close()


def searchMenu():
    print("1.Search by surname")
    print("2.Search by date of birth")
    print("3.Quit")
    choice = input("Please enter your choice:")
    if choice == "1":
        print("Option 1 selected.")
        sur()
    elif choice == "2":
        print("Option 2 selected.")
        date()
    elif choice == "3":
        print("Option 3 selected.")
        menu()
    else:
        print("Sorry, we do not support that.")
        op2()


menu()