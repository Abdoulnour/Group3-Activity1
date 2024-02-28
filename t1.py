def print_lines(file1):
    totalChars=0
    file = open(file1)
    for line in file:
        size= len(line)
        totalChars=totalChars+size
    file.close()

def main():
    fileName= input("Enter the file name with file path")
    returnChars= print_lines(fileName)
    print_lines(returnChars)

if __name__=="__main__":
    main()
