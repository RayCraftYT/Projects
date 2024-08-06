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
    date = input("Date of birth (day)")
    month = input("Date of birth (month)")
    year = input("Date of birth (year)")
    email = input("Email:")
    record = surname + "," + firstname + "," + addressL1 + "," + addressL2 + "," + postcode + "," + telephone + "," + date + "," + month + "," + year + "," + email + "\n"
    with open("addressbook.csv", "a") as file:
        file.write(record)
        file.close()


def searchMenu():
    records = []
    with open("addressbook.csv", "r") as file:
        for line in file:
            line = line.strip()
            record = line.split(",")
            records.append(record)
    # print(records)
    # load contents of address file into a indexed array
    # index looks like
    # record['sharar']['sep'] = [firstname, lastname, add1, add2, postcode, dob. email]
    # while end if file
    # add content to records array
    print("1.Search by surname")
    print("2.Search by date of birth")
    print("3.Quit")
    choice = input("Please enter your choice:")
    if choice == "1":
        print("Option 1 selected.")
        search(records, "surname")
    elif choice == "2":
        print("Option 2 selected.")
        search(records, "Month of birth")
    elif choice == "3":
        print("Option 3 selected.")
        menu()
    else:
        print("Sorry, we do not support that.")
        searchMenu()
def search(records, field):
    print(records)
    inputSearchTerm = input("Please enter the " + field + " you would like to search by.")
    found = []
    for i in range(len(records)):
        if inputSearchTerm in records[i]:
            found.append(records[i])

    print(found)

menu()