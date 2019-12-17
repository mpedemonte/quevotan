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

#nltk.download('punkt')
#nltk.download('stopwords')

#FUNCION QUE BUSCA TODOS LOS ARCHIVOS EN UNA CARPETA
def ls(ruta = '.'):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]

#ELIMINA EL MARCADO HTML
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

#ELIMINA TODOS LOS CORCHETES (SI ES QUE HAY ALGUNO)
def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

#ELIMINACION DE RUIDO
def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    return text

#ELIMINA CARACTERES NO ASCII DE LA LISTA DE PALABRAS
def remove_non_ascii(words):
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

#CONVIERTE TODASA LAS MAYUSCULAS EN MINUSCULAS
def to_lowercase(words):
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

#ELIMINA LA PUNTUACION
def remove_punctuation(words):
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

#ELIMINA LAS PALABRAS VACIAS
def remove_stopwords(words):
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

#FUNCION DE NORMALIZACION
def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    return words

#CARPERTA DONDE ESTAN LO PROYECTOS DE LOS BOLETINES
lista_arq = ls("/home/marco/Escritorio/quevotan/web scraping/proyectos") 

#RECORRE TODOS LOS PROYECTOS Y EXTRAE LAS PALABRAS DE ELLOS
for i in lista_arq:
    datos = open("Proyectos/"+i,"r")
    print i
    text = datos.read()
    sample = denoise_text(text)
    words = nltk.word_tokenize(sample)
    words = normalize(words)

    texto = ""
    for j in words:
        texto =texto + j +"\n"

    with open("Palabras/"+i,"w") as file:
        file.write(texto)



