# -*- coding: utf-8 -*-

import Sets 

dict1 = [None]*16
dict1[0] = Sets.Economia_fomento_y_turismo
dict1[1] = Sets.Desarrollo_social
dict1[2] = Sets.Cultura_y_Educacion
dict1[3] = Sets.justicia_y_derechos_humanos
dict1[4] = Sets.trabajo_y_prevision_social
dict1[5] = Sets.obras_publicas
dict1[6] = Sets.salud
dict1[7] = Sets.vivienda_y_urbanismo
dict1[8] = Sets.agricultura
dict1[9] = Sets.mineria_y_energia
dict1[10] = Sets.transporte_y_telecomunicaciones
dict1[11] = Sets.medio_ambiente_y_bienes_nacionales
dict1[12] = Sets.deporte
dict1[13] = Sets.mujer_y_la_equidad_de_genero
dict1[14] = Sets.Defensa
dict1[15] = Sets.Hacienda_y_relaciones_exteriores




palabras = []
palabras1 = []
datos = open ("boletin_sesion_61-1.txt","r")
result = open ("resultados.txt","a")

for i in datos:
	x= i.split("\n")
	palabras.append(x[0])

for j in range (len (dict1)):
	for i in palabras:
			if i in dict1[j]:
				if i not in palabras1:
					palabras1.append(i)
	print len (palabras1)
	for line in palabras1:
		result.write(line)
		result.write(" ")
	result.write ("\n")
	


