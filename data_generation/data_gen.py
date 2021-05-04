import re

def get_commands(text):
    # Need all text between " "
    pattern = r'"([^"]*)"'
    m = re.findall(pattern, text)

    # Removing the alexa keyword
    # Removing punctuation
    for i in range(len(m)):
        m[i] = m[i].replace("Alexa, ", "")
        m[i] = re.sub(r"[.!?\-,]", "", m[i])
        m[i] = m[i].lower()
    return m

def unique_words(commands):
    word_dict = {}
    for command in commands:
        command = re.sub(r'\[.*\]', "", command)
        for word in command.split():
            if word not in word_dict:
                word_dict[word] = 1 
    return word_dict

def find_placeholders(commands):
    to_generate = []
    #! Don't have to look for , or . in bracket because those have been
    #! removed already
    pattern2 = r'\[[A-Za-z0-9 \/\-]*\]'
    for item in commands:
        placeholders = re.findall(pattern2, item)
        if placeholders:
            to_generate.extend(placeholders)
    return to_generate

