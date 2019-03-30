# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet Barstar
"""
#Import des modules
import os, sys		
#Import des fonctions
import Giration as gir
#________________________________________________________________________________
# 									BARYCENTRE
#________________________________________________________________________________
def barycentreCalc(dico) :
	"""
	On calcule ici le centre de masse de chaque residu et de chaque conformation 
	"""
	print "\nCalcul barycentres des residus et des proteines"
	barycentreResidus(dico[0])
	barycentreResidus(dico[1])
	barycentreProteine(dico[0])
	barycentreProteine(dico[1])
	
def barycentreProteine(dprot) :
	"""
	On calcule ici la position moyenne des residus constituant une proteine, qui 
	correspond au centre de masse des proteines.
	"""
	global barycentre
	BAR = []  # stockage coordonnees barycentre
	BARx = [] # coordonnees barycentre residus sur l'axe x
	BARy = [] # coordonnees barycentre residus sur l'axe y
	BARz = [] # coordonnees barycentre residus sur l'axe z
	for conf in dprot["conflist"] :
		BAR = [list(),list(),list()] 	
		for res in dprot[conf]["liste_n_residus"] :
			BAR[0].append(dprot[conf][res][barycentre]["x"])
			BAR[1].append(dprot[conf][res][barycentre]["y"])
			BAR[2].append(dprot[conf][res][barycentre]["z"])
		BARx.append(gir.moyenne(BAR[0]))
		BARy.append(gir.moyenne(BAR[1]))
		BARz.append(gir.moyenne(BAR[2]))
	dprot["liste_CM_x"] = BARx
	dprot["liste_CM_y"] = BARy
	dprot["liste_CM_z"] = BARz
	
	return dprot
	
def barycentreResidus(dprot) :
	global barycentre
	if barycentre == "CM_CA" :
		# positon moyenne des carbone alpha
		return barycentreResCa(dprot)
	# position moyenne des residus
	return barycentreResAll(dprot)

def barycentreResCa(dprot) :
	"""
	On calcule le barycentre des residus selon la position des carbones alpha
	"""
	# Pour toutes les conformations de la proteine
	for conf in dprot["conflist"] :
		dprot[conf]["CM_res"] = dict()
		dprot[conf]["CM_res"]["x"] = list()
		dprot[conf]["CM_res"]["y"] = list()
		dprot[conf]["CM_res"]["z"] = list()

		# Pour tous les residus de chaque conformation de la proteine
		for res in dprot[conf]["liste_n_residus"] :
			dprot[conf][res]["CM_CA"] = dict()
			dprot[conf][res]["CM_CA"]["x"] = dprot[conf][res]["CA"]["x"]
			dprot[conf][res]["CM_CA"]["y"] = dprot[conf][res]["CA"]["y"]
			dprot[conf][res]["CM_CA"]["z"] = dprot[conf][res]["CA"]["z"]
			
			dprot[conf]["CM_res"]["x"].append(dprot[conf][res]["CA"]["x"])
			dprot[conf]["CM_res"]["y"].append(dprot[conf][res]["CA"]["y"])
			dprot[conf]["CM_res"]["z"].append(dprot[conf][res]["CA"]["z"])

def barycentreResAll(dprot) :
	"""
	On calcule le barycentre des residus selon la position moyenne des residus
	"""
	# Pour toutes les conformations de la proteine
	for conf in dprot["conflist"] :
		# Pour tous les residus de chaque conformation de la proteine
		for res in dprot[conf]["liste_n_residus"] :
			lcoord = [list(),list(),list()] # coordonnees [x,y,z] pour tous les atomes de chaque residus
			
			dprot[conf]["CM_res"] = dict()
			dprot[conf]["CM_res"]["x"] = list()
			dprot[conf]["CM_res"]["y"] = list()
			dprot[conf]["CM_res"]["z"] = list()

			for atom in dprot[conf][res]["atomlist"] :
				lcoord[0].append(dprot[conf][res][atom]["x"])
				lcoord[1].append(dprot[conf][res][atom]["y"])
				lcoord[2].append(dprot[conf][res][atom]["z"])

			xmoy = gir.moyenne(lcoord[0])
			ymoy = gir.moyenne(lcoord[1])
			zmoy = gir.moyenne(lcoord[2])
			
			dprot[conf][res]["CM_moyAll"] = dict()
			dprot[conf][res]["CM_moyAll"]["x"] = xmoy
			dprot[conf][res]["CM_moyAll"]["y"] = ymoy
			dprot[conf][res]["CM_moyAll"]["z"] = zmoy

			dprot[conf]["CM_res"]["x"].append(xmoy)
			dprot[conf]["CM_res"]["y"].append(ymoy)
			dprot[conf]["CM_res"]["z"].append(zmoy)

def choixMeth() :
	"""
	permet de choisir la methode de calcul utilisant la position du carbone alpha ou la methode  
	calculant la position des residus a partir du barycentre de l'ensemble des atomes
	"""
	global barycentre	
	barycentre = sys.argv[3]
	if sys.argv[3] == "CA" :
		barycentre = "CM_CA"
		return "CM_CA"
	else :
		barycentre = "CM_moyAll"
		return "CM_moyAll"
