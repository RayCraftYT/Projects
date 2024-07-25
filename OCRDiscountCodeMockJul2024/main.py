def checkout():
    price = 1
    while price != 0:
        price = float(input("Please enter a price."))
        code = input("Please enter the discount code")
        print(checkdiscount(price, code))
    print("Thank you for shopping")


def checkdiscount(price, code):
    discount = [["PVFC7", 10], ["CPU5", 5], ["BGF2", 15]]
    newprice = price
    size = len(discount)
    for x in range(size):
        print(size)
        print(discount[x][0])
        if discount[x][0] == code:
            newprice = newprice - discount[x][1]

    return newprice


print(checkout())