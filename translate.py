"""
This file has been written with by Serkan Erip (serkanerip) for translate texts via Python 3.5.
Feel free to cloning, sharing, editing and committing some new examples.
I have tried to explain each part basicly as I can.
For communicating with me:
mail: serkanerip@gmail.com
github: github.com/serkanerip
"""

import requests

class Translate():
    KEY_API = 'trnsl.1.1.20160914T190012Z.bba0cb3c0d74686a.368f6665226161cc052c656b2f00af0ae1b872d1' # yandex key api for using translate api
    API_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate?lang={}-{}&key={}"
    def __init__(self, word, source, target):
        self.source = source
        self.target = target
        self.word = word

    def translate(self):
        self.API_URL = self.API_URL.format( self.source, self.target, self.KEY_API )
        payload =  {'text': self.word}
        response = requests.post(self.API_URL, data = payload)
        response = response.json()
        if(response['code'] == 200):
            return response['text'][0]
        else:
           raise Exception( response )



