sentence = input("Enter a sentence")
space_count = 0
for x in sentence:
    if x == " ":
        space_count = space_count + 1
number_of_words = space_count + 1
print("The sentence entered from earlier: ", sentence)
print()