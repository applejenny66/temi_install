#pip install googletrans==3.1.0a0
import googletrans
from pprint import pprint

class Translator():
    def __init__(self):
        self.translator = googletrans.Translator()

    def translate2chinese(self, sentence):
        # Initial
        #translator = googletrans.Translator()
        # Basic Translate
        results = self.translator.translate(sentence, 'zh-tw')
        #print(results)
        #print(results.text)
        return (results.text)

    def translate2english(self, sentence):
        # Initial
        #translator = googletrans.Translator()
        # Basic Translate
        results = self.translator.translate(sentence, 'en')
        #print(results)
        #print(results.text)
        return (results.text)

    def detectlanguage(self, sentence):
        # Detect
        results = self.translator.detect(sentence)
        #print(results)
        print(results.lang)
        return (results.lang)

    def unknown2chinese(self, sentence, lan):
        lan = str(lan)
        results = self.translator.translate(sentence, lan)
        return results.text

translator = Translator()
sent = translator.translate2chinese("hello world")
print ("sent: ", sent)
sent2 = translator.translate2english(sent)
print ("sent2: ", sent2)
#unknown_sentence = 'おはよう'
#unknown_lan = translator.detectlanguage(unknown_sentence)
#unknown_meaning = translator.unknown2chinese(unknown_sentence, unknown_lan)
#unknown_meaning = translator.translate2chinese(unknown_sentence)
#print ("mean: ", unknown_meaning)