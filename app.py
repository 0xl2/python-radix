from urllib import request
import re
from Radix import *

class AppClient:
    def __init__(self, url):
        self.url = url
        self.radix = Radix()
        self.radix_root = self.radix.root

    def main(self):
        cnt = 0

        # get txt data from url
        with request.urlopen(self.url) as response:
            line = response.read().decode('utf-8')
            for word in line.split():
                # remove special characters from word and covert to lower
                word = (re.sub(r'\W+','', word)).lower()

                if len(word) > 0:
                    # cnt += 1
                    # if cnt > 100: break

                    # check word exists in radix
                    existing = self.radix.search(word, self.radix_root, "", word)
                    # print(word, existing)
                    if existing == False:
                        print("adding new word '" + word + "'")
                        # add string to radix
                        self.radix.addString(word, self.radix_root, word)
                        # self.radix.printAll()

        # self.radix.printAll()
        self.radix.listAllNodes(self.radix_root, "")


appClient = AppClient('https://www.gutenberg.org/cache/epub/100/pg100.txt')
appClient.main()
