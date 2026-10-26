from org import classify_text

examples = [
    "Calculus and algebra revision",
    "Introduction to thermodynamics",
    "My biology notes",
]

for example in examples:
    print (example, "->", classify_text(example))
