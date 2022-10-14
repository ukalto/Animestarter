import webbrowser
import os
import pathlib
import sys

# check if the os is windows or different, for different pathing
files = "\Files" if sys.platform.startswith("win") else "/Files"
# gets the directory the software is located in
directory = os.getcwd() + files
options = 7


# if the Files directory doesn't exist it creates one
def createFileDirectory():
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)


# get all files in a list
def getFiles():
    return os.listdir(directory)


# gets a file by its index
def getFileByNumber(number):
    list1 = getFiles()
    return list1[number - 1]


# reads in the input which file should be used and opens the links
def getFileInput():
    printFiles()
    while True:
        try:
            inputnf = input("Enter a number from 1 to " + str(len(getFiles())) + " or the filename: ")
            # if number > getFiles() or number < 1:
            if not checkFiles(inputnf) and not 1 <= int(inputnf) <= len(getFiles()):
                raise ValueError
            else:
                return inputnf
        except ValueError:
            print("This File does not exist.")
            continue


# print all filenames which are in the Files directory
def printFiles():
    for i, j in zip(getFiles(), range(len(getFiles()))):
        print(str(j + 1) + " " + i)


# creates an empty file in the Files directory
def createNewFile():
    fileinput = input("Enter a file name: ")
    if fileinput != "":
        file = os.path.join(directory, fileinput)
        try:
            open(file, 'a').close()
        except OSError:
            print('Failed creating the file')
        else:
            print('File created')


# checks if a File exists with certain String
def checkFiles(checkString):
    return getFiles().__contains__(checkString)


# removes a file
def removeFile():
    printFiles()
    fileinput = input("Enter a number from 1 to " + str(len(getFiles())) + " or the filename you want to remove: ")
    if fileinput != "":
        if (checkFiles(fileinput)):
            path = os.path.join(directory, fileinput)
        else:
            file = getFileByNumber(int(fileinput))
            path = os.path.join(directory, file)
        try:
            os.remove(path)
        except FileNotFoundError:
            print('Failed removing the file')
        else:
            print('File removed')


# opens all Links with a given filename
def openLinks(inputnf):
    filename = inputnf
    if not checkFiles(filename):
        filename = getFileByNumber(int(inputnf))
    path = os.path.join(directory, filename)
    file1 = open(path, 'r')
    lines = file1.readlines()
    for i in lines:
        webbrowser.open(i.strip())


# returns all links existing in the given file that match the given word
def checkFile(file, word):
    path = os.path.join(directory, file)
    file1 = open(path, 'r')
    lines = file1.readlines()
    rows = []
    for i in lines:
        if i.__contains__(word):
            rows.append(i)
    return rows


# goes through all files and calls the checkFile method
def checkLinkExists():
    word = input("Enter a significant word which you want to search for: ")
    list1 = getFiles()
    for i in list1:
        if checkFile(i, word) != []:
            for j in checkFile(i, word):
                print("Link: " + j + "File:" + i)


# clears the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def help():
    print("1 Create File")
    print("By choosing option 1 you are able to create a new file in the Files directory. If the file directory doesn't exist it will be created for you.")
    print("2 Remove File")
    print("By choosing option 2 you are able to remove an existing file.")
    print("3 Show Files")
    print("By choosing option 3 all files existing will be shown.")
    print("4 Open File")
    print("By choosing option 4 the links in the chosen file will be opened.")
    print("5 Print Links")
    print("By choosing option 5 you will enter a key word and all links having this word will be shown. In addition to that the information in which file they are will be shown.")
    print("6 Clear Console")
    print("By choosing option 6 clears the console.")


# Todo: Another Option: Move Link from one file to another file
# Todo: Add Link to File
# Todo: remove Link from File
# displays all options
def displayOptions():
    print("1 Create File | 2 Remove File | 3 Show Files | 4 Open File | 5 Print Links | 6 Clear Console | 7 Help")


# reads in the execute option which is selected
def chooseExecuteOptions():
    while True:
        try:
            number = int(input("Enter a number from 1-" + str(options) + " to choose your option: "))
            if not 1 <= number <= options:
                raise ValueError
            else:
                return number
        except ValueError:
            print("No valid input. Please enter a valid number.")
            continue


# executes the option
def execute(chosenExecuteOptions):
    if chosenExecuteOptions == 1:
        createNewFile()
    elif chosenExecuteOptions == 2:
        removeFile()
    elif chosenExecuteOptions == 3:
        printFiles()
    elif chosenExecuteOptions == 4:
        openLinks(getFileInput())
    elif chosenExecuteOptions == 5:
        checkLinkExists()
    elif chosenExecuteOptions == 6:
        cls()
    elif chosenExecuteOptions == 7:
        help()


# main method which executes all methods
def main():
    global chooseExecuteOptions
    createFileDirectory()
    while True:
        displayOptions()
        execute(chooseExecuteOptions())


if __name__ == "__main__":
    main()
