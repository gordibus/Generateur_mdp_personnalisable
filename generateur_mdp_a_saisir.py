#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:26:45 2023

@author: gordibus
"""

import random
import string

def generer_mots_de_passe(mots, nombre_de_mdp):
    liste_mdp = []
    
    for _ in range(nombre_de_mdp):
        mots_de_passe = []
        
        for mot in mots:
            caractere_special = random.choice(string.punctuation)
            chiffre = random.choice(string.digits)
            mot_de_passe = mot + caractere_special + chiffre
            mots_de_passe.append(mot_de_passe)
            
        mot_de_passe_final = ''.join(mots_de_passe)
        liste_mdp.append(mot_de_passe_final)
    
    return liste_mdp
### Changer les trois chaines de caracère suivant et les personaliser pour obtenir un mot de passe personalisé. 
mots = ['mot1', 'mot2', 'mot3']  # Remplacez ceci par vos propres mots
nombre_de_mdp = 5  # Choisissez le nombre de mots de passe à générer

mdp_list = generer_mots_de_passe(mots, nombre_de_mdp)

for mdp in mdp_list:
    print(mdp)
