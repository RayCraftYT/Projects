dollar = 0
euro = 0
yen = 0
pound = 1


def entry():
    global dollar
    global euro
    global yen
    dollar = float(input("Please enter the value of the dollar with respect to the pound."))
    euro = float(input("Please enter the value of the euro with respect to the pound."))
    yen = float(input("Please enter the value of the yen with respect to the pound."))


def conversion():
    cFrom = input("What currency are you converting from?")
    if cFrom == "pound":
        Pound()
    elif cFrom == "dollar":
        Dollar()
    elif cFrom == "euro":
        Euro()
    elif cFrom == "yen":
        Yen()
    else:
        print("We do not support that.")


def Pound():
    amount = float(input("How much money are you converting?"))
    cTo = input("To which currency would you like to convert?")
    if cTo == "pound":
        print(amount)
    elif cTo == "dollar":
        newVal = amount / dollar
        print(newVal)
    elif cTo == "euro":
        newVal = amount / euro
        print(newVal)
    elif cTo == "yen":
        newVal = amount / yen
        print(newVal)
    else:
        print("We do not support that.")


def Dollar():
    amount = float(input("How much money are you converting?"))
    cTo = input("To which currency would you like to convert?")
    if cTo == "pound":
        newVal = amount * pound
        print(newVal)
    elif cTo == "dollar":
        print(amount)
    elif cTo == "euro":
        val = amount * dollar
        newVal = val / euro
        print(newVal)
    elif cTo == "yen":
        val = amount * dollar
        newVal = val / yen
        print(newVal)
    else:
        print("We do not support that.")


def Euro():
    amount = float(input("How much money are you converting?"))
    cTo = input("To which currency would you like to convert?")
    if cTo == "pound":
        newVal = amount / pound
        print(newVal)
    elif cTo == "dollar":
        val = amount * euro
        newVal = val / dollar
        print(newVal)
    elif cTo == "euro":
        print(amount)
    elif cTo == "yen":
        val = amount * euro
        newVal = val / yen
        print(newVal)
    else:
        print("We do not support that.")


def Yen():
    amount = float(input("How much money are you converting?"))
    cTo = input("To which currency would you like to convert?")
    if cTo == "pound":
        newVal = amount / yen
        print(newVal)
    elif cTo == "dollar":
        val = amount * yen
        newVal = val / dollar
        print(newVal)
    elif cTo == "euro":
        val = amount * yen
        newVal = val / euro
        print(newVal)
    elif cTo == "yen":
        print(amount)
    else:
        print("We do not support that.")


entry()
conversion()