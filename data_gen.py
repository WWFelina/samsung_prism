
import re

#opening file
with open("alexa.txt", "r") as f:
    content = f.read()

#need all text between " "
pattern = r'"([^"]*)"'

m = re.findall(pattern, content)

#Removing the alexa keyword
#Removing periods/commas at the end if there
for i in range(len(m)):
    m[i] = m[i].replace("Alexa, ", "")
    if m[i][-1] == "," or m[i][-1] == ".":
        m[i] = m[i][:-1]
    m[i] = m[i].lower()
print(f"Total number of commands : {len(m)}")
print(f"All commands : {m}")

to_generate = []
pattern2 = r'\[[A-Za-z0-9 \-]*\]'
for item in m:
    placeholders = re.findall(pattern2, item)
    if placeholders:
        to_generate.extend(placeholders)

print(f"Total number of customisable commands : {len(to_generate)}")
print(f"All customisable keywords : {to_generate}")

'''finding number of unique words
word_dict = {}
for command in m:
    for word in command.split():
        if word not in word_dict:
            word_dict[word] = 1

print(word_dict)
print(len(word_dict))'''