# automate file opening and closing
def main():
    print("This program automates file opening and closing.")
    filename = input("Please enter the filename: ")
    infile = open(filename, 'r')
    print(infile.read())
    infile.close()
    print("\nFile closed.")
