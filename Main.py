#########################################################################################################
################################### EXECUTION DU PROGRAMME ##############################################
#
# 					python Main.py start_prot_only.pdb md_prot_only_skip100.pdb all
#
#########################################################################################################

# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet Barstar
"""
#Import des modules
import os, sys
#Import des fonctions
import ParserPDB as parse
import Giration as gir
import Barycentre as bar
import RMSD as rmsd
import Distance as dist 
import Enfouissement as enfoui
import Graphes as graph
import Write as w
#_________________________________________________________________________________________________
# 												MAIN
#_________________________________________________________________________________________________
def dictionnaire() :
	global argv
	
	# Transformation des fichiers pdb en dictionnaires
	dico1 = parse.parsePDBMultiChains(sys.argv[1])
	dico2 = parse.parsePDBMultiChains(sys.argv[2])
	
	return [dico1, dico2]		
	
if __name__ == '__main__':
	
	dico = dictionnaire()
	
	#choisir la methode de calcul du barycentre des residus a partir de la position 
	#du carbone alpha "CM_CA" ou de la distance moyenne separant les atomes "CM_moyall"
	barycentre = bar.choixMeth()			

	#Calcul des differentes valeurs de parametres
	bar.barycentreCalc(dico)
	rmsd.RMSD(dico)
	dist.distance(dico)
	gir.rayonGiration(dico)
	enfoui.enfouissement(dico)	

	#on donne le bon nom aux dossiers en fonction du nombre de conformations analysees type_analyse= "CA_200"
	type_analyse=barycentre+"_"+str(len(dico[1]["conflist"])-1)			

	#~ w.write(dico,type_analyse)
	w.write(dico,type_analyse)
	
	#Representation graphique des resultats et stockage dans un dossier.
	graph.plotRes(dico) 						

	#Suppression des fichiers .pyc apres execution.
	cwd = os.getcwd()
	for file in os.listdir(cwd):
		if file.endswith('.pyc'):
			print "suppression de "+file+" avec succes"
			rm = 'rm '+file; os.popen(rm)
	
print "\nOn vous souhaite une bonne analyse !\n"
