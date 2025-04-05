import re

with open("miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
    book = file.read()

# Extract the paragraphs where "love" was used
pattern = re.compile("[A-Z]{1}[^\n]*[^a-zA-Z]+love[^a-zA-Z]+[^\n]*.")
findings = re.findall(pattern, book)
print(findings)
# Extract the chapter titles
pattern = re.compile("[a-zA-Z ]+\n\n")
findings = re.findall(pattern, book)
print(findings)

# Function that finds the occurrence of any word as input
def find(word):
    pattern = re.compile("[a-zA-Z]+")
    findings = re.findall(pattern, book.lower())
    d = {}
    for word in findings:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1
    try:
        return d[word]
    except:
        return f"The book does not contain the word {word}"

print(find("love"))

# I just need a comit