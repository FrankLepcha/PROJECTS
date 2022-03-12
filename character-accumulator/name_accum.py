
print("This program will take take a user's name and spit out the sum of values based on the letter \n")

def main():
    name = input("Enter a name:") #Ask the user for name
    low = name.lower() #changes the input from "name" into all lower case letters
    accum = 0 #acuumulator to compile
    for x in low:
        accum = accum + ord(x) - 96 # used ord(x) so the program reads in Unicode, subtracted  96 of bc the letter "a" starts of at 96.
    print("The name entered earlier: ",name)
    print("The following name total numeric value: ",accum)
main()
