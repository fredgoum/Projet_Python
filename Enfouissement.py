# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet dynamique moleculaire, Barstar
"""
#Import des modules
import os
from scipy.stats.stats import pearsonr
#__________________________________________________________________________________________________
# 							    			ENFOUISSEMENT
#__________________________________________________________________________________________________
def enfouissement(dico) :
	enfouissementConf(dico[1])
	enfouissementRes(dico[0])

def enfouissementConf(dconf) :
	"""
	correlation entre enfouissement des residus et flexibilite des regions pour chaque conformation.
	"""
	dconf["CorEnfFlexConf"] = [list(), list()] # pvaleur et correlation
	for conf in dconf["conflist"] :
		if(dconf[conf]["RMSD"] == [0] * len(dconf[conf]["RMSD"])) :
			cor = [1,0]
		else :
			cor = pearsonr(dconf[conf]["enfouissement"],dconf[conf]["RMSD"])
		dconf["CorEnfFlexConf"][0].append(cor[0])
		dconf["CorEnfFlexConf"][1].append(cor[1])
	return dconf["CorEnfFlexConf"]

def enfouissementRes(dref) :
	"""
	correlation entre enfouissement de residu et sa flexibilite
	"""
	dref["CorEnfFlexRef"] = [list(), list()] # correlation et pvaleur
	for i in range(len(dref["list_enfRes"])) :
		cor = pearsonr(dref["list_enfRes"][i],dref["list_RMSDres"][i])
		dref["CorEnfFlexRef"][0].append(cor[0])
		dref["CorEnfFlexRef"][1].append(cor[1])
	return dref["CorEnfFlexRef"]
