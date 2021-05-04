from sklearn.feature_extraction.text import CountVectorizer
from data_gen import *
import pandas as pd
from sklearn.cluster import KMeans

if __name__ == "__main__":
    #Opening file
    with open("alexa.txt", "r", encoding='utf8') as f:
        content = f.read()

    m = get_commands(content)
    #print(f"Total number of commands : {len(m)}")
    #print(f"All commands : {m}")

    '''word_dict = unique_words(m)
    print(word_dict)
    print(len(word_dict))'''

    customisable = find_placeholders(m)
    print(f"Total number of customisable commands : {len(customisable)}")
    print(f"All customisable keywords : {set(customisable)}")

    '''vectorizer = CountVectorizer()
    dataset = vectorizer.fit_transform(m)
    labels = vectorizer.get_feature_names()
    df = pd.DataFrame(dataset.todense())
    df.to_csv('test.csv', index = False, header = labels)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df)
    print(kmeans.labels_)
    print(len(kmeans.labels_))'''
