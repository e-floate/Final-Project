import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import re
import swifter
import lxml



def get_links(row):

    try:

        url2 = urllib.request.urlopen(str(row['URL']))
        print("Webpage opened")
    except:
        print('Webpage not responding')

        return None
    
    soup = BeautifulSoup(url2, 'lxml')
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    return len(links)

if __name__ == "__main__":
    db = pd.read_csv('pre_thread_db.csv')
    db['hyperlinks'] = db.swifter.apply(lambda row: get_links(row),axis=1)
    db.to_csv('post_thread_db.csv')