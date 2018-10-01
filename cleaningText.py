import glob
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import sent_tokenize
import string

def main():
    txt_files = glob.glob("*.txt")

    for i in txt_files:
        print(i)
        if i == 'updatedurls.txt' or i == 'urls.txt':
            continue
        else:
            with open(i, "r") as f:
                text = f.read()
                text = text.replace('\n', '')
                text = text.replace('\t', '')

                text = text.lower()
                sentTokenize = sent_tokenize(text)
                # print(sentTokenize)

                with open(i, "w") as f2:
                    for j in sentTokenize:
                        f2.write("hi")








        # with open(i, "w") as f2:



if __name__ == '__main__':
    main()