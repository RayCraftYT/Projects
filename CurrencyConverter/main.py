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
        amount = newVal
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "dollar":
        newVal = amount / dollar
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "euro":
        newVal = amount / euro
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "yen":
        newVal = amount / yen
        newerVal = round(newVal, 2)
        print(newerVal)
    else:
        print("We do not support that.")


def Dollar():
    amount = float(input("How much money are you converting?"))
    cTo = input("To which currency would you like to convert?")
    if cTo == "pound":
        newVal = amount * pound
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "dollar":
        newerVal = round(amount, 2)
        print(newerVal)
    elif cTo == "euro":
        val = amount * dollar
        newVal = val / euro
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "yen":
        val = amount * dollar
        newVal = val / yen
        newerVal = round(newVal, 2)
        print(newerVal)
    else:
        print("We do not support that.")


def Euro():
    amount = float(input("How much money are you converting?"))
    cTo = input("To which currency would you like to convert?")
    if cTo == "pound":
        newVal = amount / pound
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "dollar":
        val = amount * euro
        newVal = val / dollar
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "euro":
        newerVal = round(amount, 2)
        print(newerVal)
    elif cTo == "yen":
        val = amount * euro
        newVal = val / yen
        newerVal = round(newVal, 2)
        print(newerVal)
    else:
        print("We do not support that.")


def Yen():
    amount = float(input("How much money are you converting?"))
    cTo = input("To which currency would you like to convert?")
    if cTo == "pound":
        newVal = amount / yen
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "dollar":
        val = amount * yen
        newVal = val / dollar
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "euro":
        val = amount * yen
        newVal = val / euro
        newerVal = round(newVal, 2)
        print(newerVal)
    elif cTo == "yen":
        newerVal = round(amount, 2)
        print(newerVal)
    else:
        print("We do not support that.")


entry()
conversion()
