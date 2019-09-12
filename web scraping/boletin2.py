#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, string, unicodedata
import nltk
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import os.path

#nltk.download('punkt')
#nltk.download('stopwords')

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def quitar_corchetes(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = quitar_corchetes(text)
    return text

def remove_non_ascii(words):
    #Eliminar caracteres no ASCII de la lista de palabras simbólicas
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    #Convierte todas las mayusculas en minusculas
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    #Elimina la puntuacion
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

#REMPLAZA LOS NUMEROS POR LETRAS
#def replace_numbers(words):
 #   """Replace all interger occurrences in list of tokenized words with textual representation"""
  #  p = inflect.engine()
   # new_words = []
    #for word in words:
     #   if word.isdigit():
      #      new_word = p.number_to_words(word)
       #     new_words.append(new_word)
       # else:
        #    new_words.append(word)
    #return new_words

def remove_stopwords(words):
    #Elimina palabras vacias
    new_words = []
    for word in words:
        if word not in stopwords.words('spanish'):
            number=False
            if len(word)>2:
                if word == "i" or word == "ii" or word == "iii" or word == "iv" or word == "v" or word == "vi" or word == "vii" or word == "viii":
                    number = True
                else:
                    for i in word:
                        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                            number=True
                        if i == " ":
                            word = word.replace(" ", "'")
                if number == False:
                    new_words.append(word)
    return new_words

#def stem_words(words):
 #   """Stem words in list of tokenized words"""
  #  stemmer = LancasterStemmer()
   # stems = []
    #for word in words:
     #   stem = stemmer.stem(word)
      #  stems.append(stem)
    #return stems

#def lemmatize_verbs(words):
 #   """Lemmatize verbs in list of tokenized words"""
  #  lemmatizer = WordNetLemmatizer()
   # lemmas = []
    #for word in words:
     #   lemma = lemmatizer.lemmatize(word, pos='v')
      #  lemmas.append(lemma)
    #return lemmas

def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    return words


x=1
for k in range(341,3810):
    print k
    for j in range(1,17):
        if os.path.exists("proyectos/boletin_sesion_"+str(k)+"-"+str(j)+".txt") == True:
            datos = open("proyectos/boletin_sesion_"+str(k)+"-"+str(j)+".txt","r")
            text = datos.read()

            sample = denoise_text(text)
            words = nltk.word_tokenize(sample)
            words = normalize(words)

            texto = ""
            for i in words:
                texto =texto + i +"\n"

            with open("palabras/boletin_sesion_"+str(k)+"-"+str(j)+".txt","w") as file:
                file.write(texto)
    x=x+1



