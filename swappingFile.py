def swapFileData():

    file1 = input("Enter 1st file: ")
    file2 = input("Enter 2nd file: ")

    ref1 = open(file1, 'r+')
    fileOneData = ref1.read()

    ref2 = open(file2, 'r+')
    fileTwoData = ref2.read()

    write1 = open(file1, 'w+')
    write1.write(fileTwoData)

    write2 = open(file2, 'w+')
    write2.write(fileOneData)

swapFileData()

