import glob
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import sent_tokenize
import string
import re

def main():
    txt_files = glob.glob("*.txt")


    dict = {}
    dict40 = {}
    for i in txt_files:
        print(i)
        if i == 'updatedurls.txt' or i == 'urls.txt':
            continue
        else:
            with open(i, "r") as f:
                text = f.read()
                text = text.replace('\\n', '')
                text = text.replace('\\t', '')

                text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text)
                text = re.sub(r'[^\w\s]', ' ', text)

                text = text.lower()
                sentTokenize = sent_tokenize(text)

                # word_tokens = word_tokenize(text)  # Word Tokenizing
                # uniq_word_tokens = set(word_tokens)

                # word_tokens2 = [word for word in uniq_word_tokens if word not in stopwords.words('english') and
                #                 word not in string.punctuation]  # Removing stop words.


                # for t in word_tokens2:
                #     if t in dict.keys():
                #         dict[t] += 1
                #     else:
                #         dict[t] = 1

                # count = 0
                # for k in sorted(dict, key=lambda k: dict[k], reverse=True):  # Sorting, looping till 40th entry
                #     # and storing in new dictionary.
                #     dict40[k] = dict[k]
                #     #THIS IS WHERE I'M MAKING CHANGES
                #     count += 1
                #     if count == 40:
                #         break

                # for dt in dict40:
                #     print(dt, "\n")

                # print("40 most common terms: ")
                # # for k, v in dict40.items():
                # #     print(k, " ", v, "\n")


                with open(i, "w") as f2:
                    for j in sentTokenize:
                        f2.write(j)

    # print(dict40)


if __name__ == '__main__':
    main()