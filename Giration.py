# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet dynamique moleculaire, Barstar
"""
#Import des modules
import sys
from math import sqrt
#_______________________________________________________________________________________
# 						         RAYON DE GIRATION
#_______________________________________________________________________________________
'''
On calcul la distance maximale entre un residu et le centre de masse d'une conformation
'''
def rayonGiration(dico) :
	'''
	ratio_giration est une cle qui correspond au rapport entre 
	rayon de giration de ref et rayon de giration des conf
	'''
	print "Calcul Rayons de Giration"
	dref = dico[0]
	dconf = dico[1]	
	rayon = maxDistance(dconf)
	ref = maxDistance(dref)[0]
	dconf["ratio_giration"] = [x/ref for x in rayon]

def maxDistance(dprot) :
	'''
	Renvoie la distance maximale parmi toutes les distances calculees precedemment	
	'''
	dprot["rayonGiration"] = list()
	for conf in dprot["conflist"] :
		dprot["rayonGiration"].append(max(dprot[conf]["enfouissement"]))
	return dprot["rayonGiration"]
	
# Fonctions de calcul mathematique

def moyenne(liste) :
	return sum(liste)/len(liste)

def variance(liste) :
	n = len(liste)
	if (n != 0) :
		m = moyenne(liste)**2
		s = sum([x**2 for x in liste])
		return s/n-m
	print "ERROR"
	sys.exit(1)

def ecart_type(liste) :
	return sqrt(variance(liste))
