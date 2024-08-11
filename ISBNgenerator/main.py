numberArray = []
calculationArray = []
def entryCheck():
    addResult = 0
    tenDigitNumber = input("Please enter a ten digit number.")
    x = tenDigitNumber.isnumeric()
    if len(tenDigitNumber) == 10 and x == True:
        for i in range(0,10):
            numberArray.append(tenDigitNumber[i])
            addResult = addResult + (int(tenDigitNumber[i]) * (11 - i)) 
        modResult = addResult % 11 #Get remainer 
        checkDigit = 11 - modResult
        print(checkDigit)
        numberArray.append(checkDigit)
        print(numberArray)
    else:
        print("Sorry, that is not a valid digit.")

print("Welcome to the ISBN generator, please enter a 10 digit number without any other characters and of the correct length to generate the corresponding ISBN!")
entryCheck()