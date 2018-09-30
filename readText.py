from bs4 import BeautifulSoup
import urllib.request
import re

def main():
    url_list = open("updatedurls.txt", "r").read().split("\n")
    a = 1
    for url in url_list:
        filename = "text" + str(a) + ".txt"
        my_url = url
        html = urllib.request.urlopen(my_url)
        soup = BeautifulSoup(html)
        data = soup.findAll(text=True)
        result = filter(visible, data)
        temp_list = list(result)      # list from filter
        temp_str = ' '.join(temp_list)
        # print(temp_str)

        with open(filename, "w") as f2:
            f2.write(str((temp_str).encode("utf-8")))

        a += 1

# function to determine if an element is visible
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

if __name__ == '__main__':
    main()