#!/usr/bin/python3
import re

array = []

with open("frases1.txt") as fichero:
	lineas = fichero.read().split('\n')
	for linea in lineas:
	# Escapamos las lineas en blanco
		if not linea.strip(): continue
	# Si no tiene punto al final se añade
		if not (re.match(".*\.$", linea)):
			linea = linea + '.'
	# Comprueba si ya está insertado, case insensitive activado
		if linea.lower() not in map(str.lower, array):
			array.append(linea)
			print(linea)
