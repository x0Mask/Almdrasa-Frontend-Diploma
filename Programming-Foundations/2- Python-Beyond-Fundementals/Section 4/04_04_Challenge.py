import re;

txt = "almdrasa is your way to learn programming the right way. almdrasa badges motivate students to do more. "
txt += "almdrasa quizes help students practice on what they have learned through the course. "
txt += "almdrasa courses are one of a kind because they were made by professionals. "
txt += "almdrasa look and feel is one of a kind, almdrasa wishes you a good learning. thanks."

print(re.sub(r"\balmdrasa\s\b\w{3,}\b", "Almadrasa", txt, 3))