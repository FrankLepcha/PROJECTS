def wordStats(inFile):
    # open file in read mode
    fptr = open(inFile, 'r')

    # read the contents of the file
    x = fptr.read()

    # no of characters is the no of xharacters in x
    character_count = len(x)

    word_count = 0;

    line_count = 0

    # read the file contents line by line by splitting the

    # string x using \n as delimeter

    for line in x.split('\n'):

        # read line word by word

        for word in line.split(' '):

            # if current word is not empty

            if word != '':
                word_count += 1

        line_count += 1

    print("The file contains ", line_count, "line", word_count, "words, and", character_count, "characters")


def main():
    fname = input("Enter filename: ")


    wordStats(fname)

main()