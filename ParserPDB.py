# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet dynamique moleculaire, Barstar
"""
#Importation des modules
import sys
#_______________________________________________________________________
# 						PARSER PDB
#_______________________________________________________________________
def parsePDBMultiChains(infile) :
	"""
	parsePDBMultiChains permet de parser un un fichier PDB
	"""
	# stores PDB 
	try:
		f = open(infile, "r")
		lines = f.readlines()
		f.close()
	except:
		print("Erreur: veuilez reessayer\n")
		sys.exit(0) # Arret execution programme

	print "\nParsage de "+infile
	dPDB = dict()
	dPDB["conflist"] = list()
	
	# reads the lines  
	for line in lines :		
		if line[0:5] == "MODEL" :
			conf = line[10:14]
			dPDB["conflist"].append(conf)
			dPDB[conf] = dict()
			dPDB[conf]["liste_n_residus"] = list()
			dPDB[conf]["liste_seq_residus"] = list()
			dPDB[conf]["reslist"] = list()
        
		if line[0:4] == "ATOM" :
			residus = line[17:20]
			n_res = line[23:26].strip() 
			atomtype = line[13:16].strip() 
			identifiant = line[7:11].strip() 
			x = float(line[30:38])
			y = float(line[38:46])
			z = float(line[46:54])
			
			if not n_res in dPDB[conf]["liste_n_residus"] :
				dPDB[conf]["liste_n_residus"].append(n_res)
				dPDB[conf]["liste_seq_residus"].append(residus)
				
				if not residus in dPDB[conf]["reslist"] :
					dPDB[conf]["reslist"].append(residus)
				
				dPDB[conf][n_res] = dict()
				dPDB[conf][n_res]["atomlist"] = list()
			
			dPDB[conf][n_res]["atomlist"].append(atomtype)
			dPDB[conf][n_res][atomtype] = dict()
			dPDB[conf][n_res][atomtype]["x"] = x
			dPDB[conf][n_res][atomtype]["y"] = y
			dPDB[conf][n_res][atomtype]["z"] = z
			dPDB[conf][n_res][atomtype]["id"] = identifiant

	return dPDB
