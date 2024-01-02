stringsFile = open("strings.txt")
outputFile = open("string_output.txt", "wt")
phrase = ""
for index, line in enumerate(stringsFile):
    if index == 0:
        phrase += " " + line.strip()
    elif index == 2:
        phrase += " " + line.strip()
    else:
        phrase += " " + line.strip().lower()
# for line in stringsFile:
#     if line.strip() == "I":
#         phrase += " " + line.strip()
#     elif line.strip() == "Almdrasa":
#         phrase += " " + line.strip()
#     else:
#         phrase += " " + line.strip().lower()
print(phrase)
print(phrase, file=outputFile)
outputFile.close()