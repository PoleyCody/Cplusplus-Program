import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def FrequencyList(productFile):
    f = open(productFile, "r")

    fileList = f.readlines()
    productList = []

    for i in fileList:
        productList.append(i.strip())


    product = []
    freqList = []

    for x in productList:
        if x not in product:
            product.append(x)

    for y in product:
        freqList.append(productList.count(y))

    i = 0
    for z in product:
        print(z, freqList[i])
        i = i + 1

    f.close()
    return 0;

def FreqOfItem(valueToFind):
    productFile = "CS210_Project_Three_Input_File.txt"
    f = open(productFile, "r")

    fileList = f.readlines()
    productList = []

    for i in fileList:
        productList.append(i.strip())
    
    f.close()
    return productList.count(valueToFind);

def ProductToFile(productFile):
    f = open(productFile, "r")
    wf = open("frequency.dat", "w")
    
    fileList = f.readlines()
    productList = []

    for i in fileList:
        productList.append(i.strip())

    product = []
    freqList = []

    for x in productList:
        if x not in product:
            product.append(x)

    for y in product:
        freqList.append(productList.count(y))

    i = 0
    for z in product:
        wf.write('{} {}\n'.format(z, freqList[i]))
        i = i + 1

    f.close()
    wf.close()
    return 0;