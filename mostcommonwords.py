import glob
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

def main():
    txt_files = glob.glob("*.txt")

    dict = {}
    dict40 = {}
    textupdated = ''

    for i in txt_files:

        if i == 'updatedurls.txt' or i == 'urls.txt':
            continue
        else:
            with open(i, "r") as f:
                text = f.read()

            textupdated = textupdated + text

    print("-------------------------------------------------------------------------------------------------------------")
    print(textupdated)

    textupdated = textupdated.replace('\\n', '')
    textupdated = textupdated.replace('\\t', '')

    textupdated = re.sub(r'\b\d+(?:\.\d+)?\s+', '', textupdated)
    textupdated = re.sub(r'[^\w\s]', ' ', textupdated)

    word_tokens = word_tokenize(textupdated)  # Word Tokenizing
    uniq_word_tokens = set(word_tokens)

    word_tokens2 = [word for word in word_tokens if word not in stopwords.words('english') and
                    word not in string.punctuation]  # Removing stop words.

    for t in word_tokens2:
        if t in dict.keys():
            dict[t] += 1
        else:
            dict[t] = 1

    count = 0
    for k in sorted(dict, key=lambda k: dict[k], reverse=True):  # Sorting, looping till 40th entry
        # and storing in new dictionary.
        dict40[k] = dict[k]
        # THIS IS WHERE I'M MAKING CHANGES
        count += 1
        if count == 40:
            break

    print("40 most common terms: ")
    for k, v in dict40.items():
        print(k, " ", v, "\n")

if __name__ == '__main__':
    main()