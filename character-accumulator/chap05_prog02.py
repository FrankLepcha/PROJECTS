print("This program counts the number of words in a sentence entered by the user")
def main():
    sentence =(input("Enter a sentence: ")) #ask for input
    words = sentence.split() #sentence is split
    wordCount = 0 #accumulator
    for i in words:
        wordCount = wordCount + 1 #word is being compilied
    print("The sentence from earlier input: ",sentence)
    print("The total word count is: ", wordCount)

main()
