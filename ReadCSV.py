import csv
def readcsv(csvFile):
    try:
        with open(csvFile, 'r') as file1:
            csv_reader= csv.reader(file1)

            for line in csv_reader:
                print(line)
            
    except FileExistsError:
        print("File not found, try again later: ")


def main():
    csvFile = input("Enter a csv file with its path: ")
    readcsv(csvFile)

if __name__=="__main__":
    main()
