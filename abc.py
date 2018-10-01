from nltk import sent_tokenize
string1 = str(b'Hello \n \n \n \n World')
tmp = string1.split()
string2 = ' '.join(tmp)

print(tmp)
print(string2)

with open('text1.txt', "r") as f:
    text = f.read()
    text = text.replace('\\n', '')
    #print(text)

    # for i in sentence:
    #
    #     i = i.replace('\\n', '+++++++++++')
    #     #print(i)
    #
    #     #print("------------------------------------------------------------------")

