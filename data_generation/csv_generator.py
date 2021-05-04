
from data_gen_helpers import *


if __name__ == "__main__":
    #Opening file
    files = ["google.txt", "alexa.txt"]
    for myfile in files:
        with open(myfile, "r", encoding='utf8') as f:
            content = f.read()

        m = change_weird_double_quotes(content)
        m = text_between_quotes(m)
        m = remove_keyphrase(m, ["Hey Google, ", "Hey Google ", "OK, Google, ", "OK Google, ", "Alexa, "])
        m = remove_caps_punctuation(m)
        print(f"Total number of commands : {len(m)}")
        with open('data.csv', 'a') as csvfile:
            for command in m:
                csvfile.write(command+"\n")
        #print(f"All commands : {m}")

        '''word_dict = unique_words(m)
        print(word_dict)
        print(len(word_dict))

        customisable = find_placeholders(m)
        print(f"Total number of customisable commands : {len(customisable)}")
        print(f"All customisable keywords : {set(customisable)}")'''
