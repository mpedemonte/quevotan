#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, string, unicodedata
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import os.path
from os import listdir
from os.path import isfile, join

def ls(ruta = '.'):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]
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

def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    return words


lista_arq = ls("/home/marco/Escritorio/quevotan/web scraping/proyectos") 


#x=1
#nume=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]
#for k in range(520,3816):
 #   print k
  #  for num in range(1,13000):
   #     for j in nume:
    #        if os.path.exists("proyectos/boletin_sesion_"+str(k)+"-"+str(num)+"-"+j+".txt") == True:
for i in lista_arq:
    datos = open("proyectos/"+i,"r")
    print i
    text = datos.read()
    sample = denoise_text(text)
    words = nltk.word_tokenize(sample)
    words = normalize(words)

    texto = ""
    for j in words:
        texto =texto + j +"\n"

    with open("palabras/"+i,"w") as file:
        file.write(texto)
    #x=x+1



