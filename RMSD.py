# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet dynamique moleculaire, Barstar
"""
#Import des modules
import os
from math import sqrt
#Import des fonctions
import Barycentre as bar
import Giration as gir
#___________________________________________________________________________________
# 						        ROOT MEAN SQUARE DEVIATION
#___________________________________________________________________________________
def RMSD(dico) :
	"""
	Calcul la distance moyenne entre les residus
	"""
	print "Calcul RMSD"
	RMSDresglobal(dico[0],dico[1])
	RMSDconf(dico[1])
	RMSDreslocal(dico[0], dico[1])

def RMSDreslocal(dref,dconf) :
	"""
	On calcule les RMSD de maniere locale
	"""
	l_res = dref[dref["conflist"][0]]["liste_n_residus"]
	dref["RMSDres_mean"] = list()
	dref["RMSDres_sd"] = list()
	dref["list_RMSDres"] = list()
	for i in range(len(l_res)) :
		l_rmsd = list() # liste des RMSD d'un residu pour toutes ses conformations
		for conf in dconf["conflist"] :
			l_rmsd.append(dconf[conf]["RMSD"][i])
		dref["list_RMSDres"].append(l_rmsd)
		dref["RMSDres_mean"].append(gir.moyenne(l_rmsd))
		dref["RMSDres_sd"].append(gir.ecart_type(l_rmsd))

def RMSDresglobal(dref, dconf) :
	"""
	entre la position de chaque residu de chaque conformation, on calcule le RMSD
	"""
	global barycentre	
	# conf_ref, une conformation de reference
	conf_ref = dref["conflist"][0] 
	for conf in dconf["conflist"] :
		dconf[conf]["RMSD"] = list()
		for res in dconf[conf]["liste_n_residus"] :
			xref = dref[conf_ref][res][bar.barycentre]["x"]
			yref = dref[conf_ref][res][bar.barycentre]["y"]
			zref = dref[conf_ref][res][bar.barycentre]["z"]

			xconf = dconf[conf][res][bar.barycentre]["x"]
			yconf = dconf[conf][res][bar.barycentre]["y"]
			zconf = dconf[conf][res][bar.barycentre]["z"]
			
			dconf[conf]["RMSD"].append(sqrt((xref-xconf)**2 + (yref-yconf)**2 + (zref-zconf)**2))	

def RMSDconf(dconf) :
	"""
	On calcule la moyenne des RMSD des residus de maniere globale
	"""
	dconf["RMSDmoy"] = list()
	dconf["RMSDmoy_sd"] = list()
	for conf in dconf["conflist"] :
		dconf["RMSDmoy"].append(gir.moyenne(dconf[conf]["RMSD"]))
		dconf["RMSDmoy_sd"].append(gir.ecart_type(dconf[conf]["RMSD"]))
