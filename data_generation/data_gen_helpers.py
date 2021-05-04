import re

def text_between_quotes(text):
    pattern = r'"([^"]*)"'
    m = re.findall(pattern, text)
    return m

#removing stuff like alexa, hey google, etc.
def remove_keyphrase(command_list ,keyphrase_list):
    for keyphrase in keyphrase_list:
        for i in range(len(command_list)):
            command_list[i] = command_list[i].replace(keyphrase, "")
    return command_list

def change_weird_double_quotes(text):
    text = text.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")
    return text

#makes all text lower case and removes punctuation
def remove_caps_punctuation(command_list):
    for i in range(len(command_list)):
        command_list[i] = re.sub(r"[.!?\-,]", "", command_list[i])
        command_list[i] = command_list[i].lower()
    return command_list

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

