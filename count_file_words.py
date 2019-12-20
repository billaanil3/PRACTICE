s_word = input("Enter word to be searched:")
count = 0

with open("/home/anil/PRACTICE/Practices/PYTHON/Programs/count_words_file.txt", "r") as f:
    for line in f:
        words = line.split()
        print words
        for word in words:
            if word == s_word:
                count += 1
print("Occurrences of the word:", count)
