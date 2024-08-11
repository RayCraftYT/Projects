def convertToISBN(number, length):
    numberArray = []
    newNumber = ""
    addResult = 0
    checkDigit = ""
    x = number.isnumeric()
    if len(number) == length and x == True:
        for i in range(0,length):
            numberArray.append(number[i])
            addResult = addResult + (int(number[i]) * (11 - i))
        modResult = addResult % 11 #Get remainer
        if modResult == 0:
            checkDigit = "0"
        elif modResult == 1:
            checkDigit = "X"
        else:
            checkDigit = str(11 - modResult)
            numberArray.append(checkDigit)
        print("Result: " + str(addResult))
        print("Check Digit: " + str(checkDigit))
        print("Number Array: " + str(numberArray))
        for i in range(0, len(numberArray)):
            newNumber = newNumber + str(numberArray[i])
        print("ISBN: " + newNumber)
        return(newNumber)
    else:
        print("Sorry, that is not a valid digit.")

print("Welcome to the ISBN generator, please enter a 10 digit number without any other characters and of the correct length to generate the corresponding ISBN!")
tenDigitNumber = input("Please enter a ten digit number.")
number = entryCheck(tenDigitNumber, 10)

print ("ISBN:" + number)
newNumber = convertToISBN(number, 11)