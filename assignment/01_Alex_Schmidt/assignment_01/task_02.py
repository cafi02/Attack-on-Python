word = input() 
i = len(word) # i is lenght of word

while i > 0:
    print(word[i-1], end = "") # Prints the word in reversed order, starting with the last index and then counting down to the first
    i = i - 1
