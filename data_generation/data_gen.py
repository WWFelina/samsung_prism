import re

def get_commands(text):
    #need all text between " "
    pattern = r'"([^"]*)"'
    m = re.findall(pattern, content)

    #Removing the alexa keyword
    #Removing punctuation
    for i in range(len(m)):
        m[i] = m[i].replace("Alexa, ", "")
        m[i] = re.sub(r"[.!?\-,]", "", m[i])
        m[i] = m[i].lower()
    return m

def unique_words(commands):
    word_dict = {}
    for command in commands:
        for word in command.split():
            if word not in word_dict:
                word_dict[word] = 1
    
    return word_dict

def find_placeholders(commands):
    to_generate = []
    pattern2 = r'\[[A-Za-z0-9 \-]*\]'
    for item in commands:
        placeholders = re.findall(pattern2, item)
        if placeholders:
            to_generate.extend(placeholders)
    return to_generate

if __name__ == "__main__":
    #opening file
    with open("alexa.txt", "r") as f:
        content = f.read()

    m = get_commands(content)
    print(f"Total number of commands : {len(m)}")
    print(f"All commands : {m}")

    word_dict = unique_words(m)
    print(word_dict)
    print(len(word_dict))

    customisable = find_placeholders(m)
    print(f"Total number of customisable commands : {len(customisable)}")
    print(f"All customisable keywords : {set(customisable)}")
