with open("strings.txt", "r") as input_file, open("string_output.txt", "w") as output_file:
    phrase = ""
    for line in input_file:
        if line.strip() == "I":
            phrase += " " + line.strip()
        elif line.strip() == "Almdrasa":
            phrase += " " + line.strip()
        else:
            phrase += " " + line.strip().lower()
    print(phrase, file=output_file)
    print(phrase)