import math

def triangulo(m1, m2):
	area = (m1 * m2) / 2
	return area

def rectangulo(m1, m2):
	area = m1 * m2
	return area

def circulo(m1, m2):
	area = math.pi * (m1 ** 2)
	return area
