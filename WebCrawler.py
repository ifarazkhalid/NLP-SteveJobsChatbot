from bs4 import BeautifulSoup
import requests
from itertools import islice

def main():
    starter_url = "https://www.google.com/search?ei=F1ywW6fFLIWqtQWkhp-ABw&q=steve+paul+jobs&oq=steve+paul+jobs&gs_l=psy-ab.12...0.0..34508...0.0..0.0.0.......0......gws-wiz.5di4CNjmvmY"

    r = requests.get(starter_url)

    data = r.text
    soup = BeautifulSoup(data)

    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            print(link_str)
            if 'Steve' in link_str or 'steve' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    f.write(link_str + '\n')

    print('---------------------------------------------------')


    with open("urls.txt", "r") as myfile:
        head = list(islice(myfile, 25))

    with open("updatedurls.txt", "w") as f2:
        for item in head:
            f2.write(item)


    # with open('urls.txt', 'r') as f:
    #     urls = f.read().splitlines()
    # for u in urls:
    #     print(u)

if __name__ == "__main__":
    main()


