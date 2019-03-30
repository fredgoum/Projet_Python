# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet dynamique moleculaire, Barstar
"""
#Import des modules
import os, csv, sys
#_____________________________________________________________________________________________________________________
# 														ECRITURE
#_____________________________________________________________________________________________________________________
def write(dico,methode) :
	'''
	On cree le dossier de sortie qui va contenir les deux fichiers excels pour l'analyse globale et l'analyse locale
	''' 
	print "Ecriture dans Resulats_des_Analyses"
	sortie1 = verification("Resulats_des_Analyses"+methode+"/res_barstar_globaux_"+methode+".csv") 
	sortie2 = verification("Resulats_des_Analyses"+methode+"/res_barstar_locaux_"+methode+".csv")	
	nb_deci = raw_input("\nVeuillez indiquer le nombre de chiffre apres la virgule :\t")

	sortie_Res_Globaux(sortie1, dico[0], dico[1], int(nb_deci))
	sortie_Res_Locaux(sortie2, dico[0], int(nb_deci))
	
def sortie_Res_Globaux(output, dref, dconf, nb_deci) :
	#On ecrit dans un fichier excel les valeurs des parametres de l'analyse globale 
	try:
		with open(output, "w") as f:
			fieldnames = ['Conf', 'Rayon Giration','Distance','ecart-type Distance','RMSD',
						  'ecart-type RMSD','Ratio Giration','Correlation','p-value Correlation']
			writer = csv.DictWriter(f, fieldnames=fieldnames)

			writer.writeheader()
			writer.writerow({'Conf':'REF','Rayon Giration': round(dref["rayonGiration"][0],nb_deci), 'Distance': 0})
			for i in range(len(dconf["conflist"])) :
				num = dconf["conflist"][i].strip()
				rayonG = dconf["rayonGiration"][i]
				d_moy = dconf["distance_moy"][i]
				d_sd = dconf["distance_sd"][i]
				rmsd = dconf["RMSDmoy"][i]
				rmsd_sd = dconf["RMSDmoy_sd"][i]
				ratio_gir = dconf["ratio_giration"][i]
				cor = dconf["CorEnfFlexConf"][0][i]
				pvalue = dconf["CorEnfFlexConf"][1][i]
				writer.writerow({'Conf': num, 'Rayon Giration': round(rayonG,nb_deci), 'Distance': round(d_moy,nb_deci), 
				'ecart-type Distance': round(d_sd,nb_deci), 'RMSD': round(rmsd,nb_deci), 'ecart-type RMSD': round(rmsd_sd,nb_deci), 
				'Ratio Giration': round(ratio_gir,nb_deci), 'Correlation': round(cor,nb_deci),'p-value Correlation': round(pvalue,nb_deci)})	
	except:
		print("Erreur chargement fichier"+output+"\n")
		sys.exit(0)

def sortie_Res_Locaux(output, dref, nb_deci) :
	#On ecrit dans un fichier excel les valeurs des parametres de l'analyse locale
	try:
		with open(output, "w") as f:
			fieldnames = ['Residus', 'Nom','RMSD', 'ecart-type RMSD','Distance residu/CdM','ecart-type Distance residu/CdM']
			writer = csv.DictWriter(f, fieldnames=fieldnames)
		
			writer.writeheader()
			conf_ref = dref["conflist"][0]
			lres = dref[conf_ref]["liste_n_residus"]
			for i in range(len(lres)) :
				res = lres[i]
				nom = dref[dref["conflist"][0]]["liste_seq_residus"][i]
				rmsd = dref["RMSDres_mean"][i]
				rmsd_sd = dref["RMSDres_sd"][i]
				d = dref["enfRes_mean"][i]
				d_sd = dref["enfRes_sd"][i]
				writer.writerow({'Residus': res, 'Nom': nom, 'RMSD': round(rmsd,nb_deci),'ecart-type RMSD': round(rmsd_sd,nb_deci), 
								 'Distance residu/CdM': round(d,nb_deci), 'ecart-type Distance residu/CdM' : round(d_sd,nb_deci)})	
	except:
		print("Erreur chargement fichier"+output+"\n")
		sys.exit(0)

def verification(output) :
	#demander a l'utilisateur s'il veut supprimer le fichier deja existants, sinon il cree un nouveau fichier.
	if (os.path.exists(output)) :
		wish = raw_input("\n"+str(output)+" deja existant : Voulez vous le remplacer ? O/N\n")
		while ((wish != 'O') & (wish != 'o') & (wish != 'N')  & (wish != 'n')) :
			print "Erreur : Repondre O pour oui ou N pour non" 
			wish = raw_input("Voulez vous le remplacer ? O/N\n")			
		if ((wish == 'N') | (wish == 'n')) :
			while os.path.exists(output) :
				output = raw_input("Entrer le nom du nouveau fichier : \n")
		elif ((wish == 'O') | (wish == 'o')) :
			rm = 'rm '+output
			os.popen(rm)	
	return output
