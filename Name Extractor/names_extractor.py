names = []

with open('names.txt', 'r') as names_file:  # Opening file in read mode
    for name in names_file:
        names.append(name.strip().title())  # .title() to capitalise only first letter of every word in string

print(names)
