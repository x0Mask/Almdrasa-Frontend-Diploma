with open("strings.txt", "r") as strings, open("string_output.txt", "w") as output:
    for line in strings:
        words = line.strip().split()
        modified_words = []

        for word in words:
            if word.lower() == 'i':
                modified_words.append('I')
            elif word.lower() == 'almdrasa':
                modified_words.append('Almdrasa')
            else:
                modified_words.append(word.lower())

        modified_line = " ".join(modified_words)
        output.write(modified_line + " ")