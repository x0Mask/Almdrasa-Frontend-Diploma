def calculateInstallment(apparmentPrice, precentage):
    return ((precentage/100) * apparmentPrice) - ((10/100) * apparmentPrice)

apparmentPrice = 200000

installmentAmount = calculateInstallment(apparmentPrice, 15)

if(installmentAmount < 0):
    print("The company owns me " + str(installmentAmount * -1))
else:
    print("I owe money to the company " + str(installmentAmount))