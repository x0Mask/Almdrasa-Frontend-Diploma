# with open("strings.txt", "r") as strings, open("string_output.txt", "w") as output:
#     for line in strings:
#         words = line.strip().split()
#         modified_words = []

#         for word in words:
#             if word.lower() == 'i':
#                 modified_words.append('I')
#             elif word.lower() == 'almdrasa':
#                 modified_words.append('Almdrasa')
#             else:
#                 modified_words.append(word.lower())

#         modified_line = " ".join(modified_words)
#         output.write(modified_line + " ")





# Open the file in read mode
# اسم الملف الذي سيتم قراءته
input_file_name = 'input.txt'  # قم بتغيير 'input.txt' بإسم ملف الإدخال الخاص بك
output_file_name = 'output.txt'  # اسم الملف الذي سيتم حفظ النتائج فيه

try:
    with open(input_file_name, 'r', encoding='utf-8') as input_file:
        # قائمة لتخزين النصوص المعدلة
        modified_lines = []

        # قراءة كل سطر وتعديل النص وإضافته إلى القائمة
        for line in input_file:
            words = line.strip().split()
            modified_words = []
            for word in words:
                if word.lower() == 'i':
                    modified_words.append('I')
                elif word.lower() == 'almdrasa':
                    modified_words.append('Almdrasa')
                else:
                    modified_words.append(word.lower())
            modified_line = ' '.join(modified_words)
            modified_lines.append(modified_line)

    # حفظ النصوص المعدلة في ملف جديد
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        for line in modified_lines:
            output_file.write(line + '\n')

    print(f"تم حفظ النتائج في '{output_file_name}'")

except FileNotFoundError:
    print(f"الملف '{input_file_name}' غير موجود.")

