meine_liste = ['Apfel', 'Banane', 'Kirsche', 'Dattel']

for index, element in enumerate(meine_liste):
    print(f"Index: {index}, Element: {element}")

# using the len of the list

meine_liste = ['Apfel', 'Banane', 'Kirsche', 'Dattel']

for index in range(len(meine_liste)):
    print(f"Index: {index}, Element: {meine_liste[index]}") # the len assigns automatically a number to each element