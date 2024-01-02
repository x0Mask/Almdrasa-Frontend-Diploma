import re

txt = "almdrasa is your way to learn programming the right way. almdrasa badges motivate students to do more.\n"
txt += "almdrasa quizes help students practice on what they have learned through the course.\n"
txt += "almdrasa courses are one of a kind because they were made by professionals.\n"
txt += "almdrasa look and feel is one of a kind, almdrasa wishes you a good learning. thanks."

txt = re.sub(r"\balmdrasa\s\b\w{3,}\b", "Almdrasa", txt, 3)

print(txt)

print('mouw ' * 5)

name = "Ali" * 2 *3
print(name)
