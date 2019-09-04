import re, string, unicodedata
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

nltk.download('punkt')

aXML=open("feed.xml","r")
sData=aXML.read()

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    return text

texto = denoise_text(sData)

words = nltk.word_tokenize(texto)
print(words)

archivo=open("palabras.txt","w")
palabras=""
for i in words:
    palabras+=i
archivo.write(palabras.encode("UTF-8"))


#print(texto.encode("UTF-8"))