'''
Writing a small script to pull Wikipedia articles directly from Wikipedia and
return the parsed plain text to the user's terminal for quick info retrieval

**Incomplete**
TODO: Filter out semantic tags
'''

from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import urllib2

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

url = "https://en.wikipedia.org/wiki/"
prompt = raw_input("What are you searching for?")
urlPrompt = "_".join(prompt.split())
url = url + urlPrompt
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, features='html.parser')
stripper = MLStripper()
print soup.title.string

paragraphs = soup.find_all("p")
thestrip = stripper.strip_tags(paragraphs[1])
print paragraphs[1]
print thestrip
'''
for p in paragraphs:
    print p
    prompt = raw_input("Should I keep spewing information?")
    if prompt is 'Y' or prompt is 'y' :
        continue
    else:
        break
'''


