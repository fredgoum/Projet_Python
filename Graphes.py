# -*- coding: utf-8 -*-
"""
Author: Alfred GOUMOU & Audrey DEHAULLON
Description: Projet dynamique moleculaire, Barstar
"""
#Import des modules
import sys, os
import matplotlib.pyplot as plt
#Import des fonctions
import Barycentre as bar

#_________________________________________________________________________________________________
# 											GRAPHES
#_________________________________________________________________________________________________
def plotRes(dico) :
	'''
	On affiche les resultats de l'analyse globale et on les enregistre dans le dossier de sortie.
	'''
	global type_analyse, wish
	barycentre = bar.choixMeth()
	type_analyse=barycentre+"_"+str(len(dico[1]["conflist"])-1)
	wish = raw_input("\nVoulez-vous afficher les resultats ? O/N\n")
	
	plotGlobal(dico[1])
	plotLocal(dico[0]) 

	print "Resultats enregistres dans Resulats_des_Analyses"+type_analyse+"/\n"

def plotGlobal(dconf) :
	#Analyse globale
	plotGiration(dconf)
	plotDistance(dconf)
	plotRMSDGlobal(dconf)
	plotFlexibiteEnfouissement(dconf)
	
def plotGiration(dconf) :
	plt.title('Rayon de Giration en fonction des conformations')
	plt.plot(dconf["rayonGiration"])
	plt.axhline(y=dconf["rayonGiration"][0],ls='--',color='red')
	plt.xlabel('Conformations')
	plt.ylabel('Rayon de Giration')
	global type_analyse
	plt.savefig("Resulats_des_Analyses"+type_analyse+"/Rayon_de_Giration.png")
	global wish
	if ((wish == 'O') | (wish == 'o')) :
		plt.show()

def plotDistance(dconf) :
	#distance moyenne des residus au centre de masse en fonction des conformations
	plt.title('Distance moyenne et/ou ecart_type des residus \n en fonction des conformations par rapport au centre de masse')
	plt.xlabel('Conformations')
	plt.ylabel('Distance moyenne')
	moyonne = dconf["distance_moy"]
	ecart_type = dconf["distance_sd"]
	moy_s = [x+y for (x,y) in zip(moyonne,ecart_type)]
	moy_i = [x-y for (x,y) in zip(moyonne,ecart_type)]
	plt.plot(moyonne, "b", label = "Distance moyenne")
	plt.plot(moy_s, "r--", label = "+/- ecart_type")
	plt.plot(moy_i, "r--",)
	global type_analyse
	plt.savefig("Resulats_des_Analyses"+type_analyse+"/Distance_conformation.png")
	global wish
	if ((wish == 'O') | (wish == 'o')) :
		plt.show()

def plotRMSDGlobal(dconf) :
	#plot du RMSD moyen en fonction des conformations par rapport a la reference.
	plt.title('RMSD moyen et/ou ecart_type des residus \n en fonction des conformations par rapport a la reference')
	plt.xlabel('Conformations')
	plt.ylabel('RMSD moyen')
	moyonne = dconf["RMSDmoy"]
	ecart_type = dconf["RMSDmoy_sd"]
	moy_s = [x+y for (x,y) in zip(moyonne,ecart_type)]
	moy_i = [x-y for (x,y) in zip(moyonne,ecart_type)]
	plt.plot(moyonne, "b", label = "RMSD moyen")
	plt.plot(moy_s, "r--", label = "+/- ecart_type")
	plt.plot(moy_i, "r--",)
	global type_analyse
	plt.savefig("Resulats_des_Analyses"+type_analyse+"/RMSd_Global.png")
	global wish
	if ((wish == 'O') | (wish == 'o')) :
		plt.show()

def plotFlexibiteEnfouissement(dconf) :
	#correlation entre la flexibilite et l'enfouissement moyens des residus, en fonction des conformations
	plt.subplot(211)
	plt.plot(dconf["CorEnfFlexConf"][0])
	plt.title('Correlation Flexibilite/Enfouissement moyens en fonction des conformations')
	plt.xlabel('Conformations')
	plt.ylabel('Correlation')
	plt.subplot(212)
	plt.plot(dconf["CorEnfFlexConf"][1])
	plt.title('Correlation Flexibilite/Enfouissement moyens \n en fonction des conformations : p-value')
	plt.xlabel('Conformations')
	plt.ylabel('p-valeur')
	plt.tight_layout()

	global type_analyse
	plt.savefig("Resulats_des_Analyses"+type_analyse+"/Correlation_conf.png")
	global wish
	if ((wish == 'O') | (wish == 'o')) :
		plt.show()


def plotLocal(dref) :
	#Analyse locale
	plotDistanceLocal(dref)
	plotRMSDLocal(dref)
	plotFlexibiteEnfouissement_residus(dref)

def plotDistanceLocal(dref) :
	#distance moyenne des residus au centre de masse en fonction des residus
	moy = dref["enfRes_mean"]
	sd = dref["enfRes_sd"]
	moy_s = [x+y for (x,y) in zip(moy,sd)]
	moy_i = [x-y for (x,y) in zip(moy,sd)]
 	plt.subplot(211)
 	plt.plot(dref["enfRes_sd"])
 	plt.title("L'ecart-Type de la distance moyenne des residus en fonction du residu \n par rapport au centre de masse pour chaque conformation")
 	plt.xlabel('Residus')
 	plt.ylabel('ecart type')
 	plt.subplot(212)
	plt.plot(moy, "b", label = "Distance moyenne")
	plt.plot(moy_s, "r--", label = "+/- ecart-type")
	plt.plot(moy_i, "r--",)
	plt.title('Distance moyenne et/ou ecart-type des residus en fonction du residu\n par rapport au centre de masse pour chaque conformation')
	plt.xlabel('Residus')
	plt.ylabel('Distance')
	plt.tight_layout()

	global type_analyse
	plt.savefig("Resulats_des_Analyses"+type_analyse+"/Distance_residu.png")
	global wish
	if ((wish == 'O') | (wish == 'o')) :
		plt.show()

def plotRMSDLocal(dref) :
	#RMSD moyen en fonction des residus
	moy = dref["RMSDres_mean"]
	sd = dref["RMSDres_sd"]
	moy_s = [x+y for (x,y) in zip(moy,sd)]
	moy_i = [x-y for (x,y) in zip(moy,sd)]
 	plt.subplot(211)
 	plt.plot(dref["RMSDres_sd"])
 	plt.title("L'ecart-Type du RMSD moyen en fonction du residu, par rapport a la reference, \nde la position des residus pour chaque conformation")
 	plt.xlabel('Residus')
 	plt.ylabel('ecart type')
 	plt.subplot(212)
	plt.plot(moy, "b", label = "RMSD moyen")
	plt.plot(moy_s, "r--", label = "+/- ecart-type")
	plt.plot(moy_i, "r--",)
	plt.title('RMSD moyen et/ou ecart-type en fonction du residu par rapport a la reference, \nde la position des residus pour chaque conformation')
	plt.xlabel('Residus')
	plt.ylabel('RMSD')
	plt.tight_layout()

	global type_analyse
	plt.savefig("Resulats_des_Analyses"+type_analyse+"/RMSD_residu.png")
	global wish
	if ((wish == 'O') | (wish == 'o')) :
		plt.show()

def plotFlexibiteEnfouissement_residus(dref) :
	#correlation entre la flexibilite et l'enfouissement moyens des residus, en fonction des residus
	plt.subplot(211)
	plt.plot(dref["CorEnfFlexRef"][0])
	plt.title("Correlation entre Flexibilite et Enfouissement de chaque residu \nde chaque conformation, en fonction des residus")
	plt.xlabel('Residus')
	plt.ylabel('Correlation')
	plt.subplot(212)
	plt.plot(dref["CorEnfFlexRef"][1])
	plt.axhline(y=0.05,ls='--',color='red')
	plt.title('Correlation Flexibilite/Enfouissement \n en fonction des residus: pvalue')
	plt.xlabel('Residus')
	plt.ylabel('p-valeur')
	plt.tight_layout()

	global type_analyse
	plt.savefig("Resulats_des_Analyses"+type_analyse+"/Correlation_residu.png")
	global wish
	if ((wish == 'O') | (wish == 'o')) :
		plt.show()
		
