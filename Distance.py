# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet dynamique moleculaire, Barstar
"""
#Import des modules
import sys, os
from math import sqrt
#Import des fonctions
import Barycentre as bar
import Giration as gir
#____________________________________________________________________________________
# 						       	CALCUL DE LA DISTANCE
#____________________________________________________________________________________
def distance(dico) :
	print "Calcul distances Residus-Barycentre"
	distanceConf(dico[0])
	distanceConf(dico[1])
	distanceRes(dico[0], dico[1])
	
def distanceConf(dconf) :
	"""
	On calcule la distance entre un residus et le centre de masse de sa conformation.
	Plus sa distance est petite, plus le residu est enfoui.
	"""
	global barycentre
	# pour chaque conformation, son centre de masse :
	xconf = dconf["liste_CM_x"]
	yconf = dconf["liste_CM_y"]
	zconf = dconf["liste_CM_z"]
	dconf["distance_moy"] = list()
	dconf["distance_sd"] = list()
	for conf in dconf["conflist"] :
		dist = []
		for res in dconf[conf]["liste_n_residus"] :
			i=0
			xres = dconf[conf][res][bar.barycentre]["x"]
			yres = dconf[conf][res][bar.barycentre]["y"]
			zres = dconf[conf][res][bar.barycentre]["z"]
			
			distance = sqrt((xres-xconf[i])**2 + (yres-yconf[i])**2 + (zres-zconf[i])**2)
			dist.append(distance)
			i += 1
		
		dconf[conf]["enfouissement"] = dist
		dconf["distance_moy"].append(gir.moyenne(dist))
		dconf["distance_sd"].append(gir.ecart_type(dist))

def distanceRes(dref, dconf) :
	"""
	On calcule la distance moyenne de chaque residu au barycentre de la proteine
	"""
	res = dref[dref["conflist"][0]]["liste_n_residus"]
	dref["enfRes_mean"] = list()
	dref["enfRes_sd"] = list()
	dref["list_enfRes"] = list()
	for i in range(len(res)) :
		enf = list()
		for conf in dconf["conflist"] :
			enf.append(dconf[conf]["enfouissement"][i])
		dref["list_enfRes"].append(enf)
		dref["enfRes_mean"].append(gir.moyenne(enf))
		dref["enfRes_sd"].append(gir.ecart_type(enf))
