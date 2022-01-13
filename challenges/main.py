vowels = ['a', 'e', 'i', 'o', 'u']
main_text = "Have you ever read a webpage or document that used this text without paying much attention to it? The lorem ipsum is a placeholder text used in publishing and graphic design. This filler text is a short paragraph that contains all the letters of the alphabet. The characters are spread out evenly so that the reader’s attention is focused on the layout of the text instead of its content. Many software programs and applications have made it their default dummy text. Since the lorem ipsum is always used as a placeholder text, its use indicates that this is not a final version of a document, thus helping to avoid unnecessary printing."

words = main_text.split()

sorted = sorted(words, key=len, reverse=True)

fiveWords = sorted[0:5]
print("The words sorted in reverse are : ", fiveWords)

for index, word in enumerate(fiveWords):
    for vowel in vowels:
        word = word.replace(vowel, "")
        fiveWords[index] = word

print("The five longest words from text without vowels are: ", fiveWords)
