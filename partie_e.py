############################################
# INFORMATIONS / DESCRIPTION:
# Titre : DM 8 Mathématiques Partie E
# Programme Python 3.8 (compatilité des versions antérieures non assurée)
# Auteurs: Antoine CHEUCLE
# Encodage: UTF-8
# Licence: GNU General Public License 3.0 (licence libre)
# Version: Release 1.0.0
#
# Description: Ce fichier contient les fonctions et les résultats de la
# partie E du DM 8 de mathématiques. Toutes les explications sont données
# en commentaire.
# DM par Julie BOUGLE et Antoine CHEUCLE
############################################

#On importe les modules nécessaires
import random as rd #Module random pour générer des nombres pseudos aléatoire
from math import ceil #Fonction ceil du module math pour arrondir des nombres au supérieur (pour la dernière question)

#QUESTION 1)a)

def randomize_list(input_list):
    """Fonction qui retourne la liste en paramètre avec les éléments désordonnés aléatoirements. Trie la liste aléatoirement"""
    #On copie d'abord la liste de départ pour ne pas la modifier
    list_copy = list(input_list)
    new_list = [] #Variable qui contiendra la nouvelle liste aléatoire

    #On boucle dans que la liste copiée contient encore des éléments à placer dans la nouvelle liste
    while len(list_copy) > 0:
        #On choisit l'index d'un élément aléatoire parmi la liste copiée
        random_element = rd.randint(0, len(list_copy) - 1)
        #On ajoute cet élément à la nouvelle liste
        new_list.append(list_copy[random_element])
        #On supprime cet élément (via son index) de la liste copiée pour ne pas qu'il puisse être re-choisit
        list_copy.pop(random_element)

    return new_list #On retourne la nouvelle liste

#Question 1)b)

def check_order(list_1, list_2):
    """Fonction qui renvoie 1 si deux listes n'ont exactement aucun éléments à la même place dans les deux listes, renvoie 0 sinon."""
    #D'abord, on élimine le cas où les deux listes n'ont pas la même taille, puisque on ne pourra pas les comparer
    assert len(list_1) == len(list_2), "Les listes doivent avoir le même nombre d'éléments"

    #On boucle sur les index des deux listes
    for index in range(len(list_1)):
        #On vérifie que les deux listes n'ont pas la même valeur pour un même index
        if list_1[index] == list_2[index]:
            #On peut directement renvoyer 0 puisqu'il y a un élément à la même place dans les deux listes
            #Il est inutile de poursuivre la boucle
            return 0
    #Si on arrive à la fin de la boucle, alors aucun élément n'est à la même place dans les deux listes, on renvoie 1
    return 1

#Question 1)c)

#Pour retrouver le réultat de la fonction C)4), on calcule le ratio de dérangements parmi le nombre total de distributions aléatoires générées
#Ainsi, on obtient une approximation de la limite de la question C)4) avec une liste à n élément et en générant n listes.
def limit_derangements(list_size, repetitions):
    """Calcule et renvoie une approximation de la limite en +∞ du nombre de dérangement sur le nombre de distributions total calculées"""
    #D'abord, on génère une liste ordonnée à n élément qui servira de base pour générer des listes aléatoires
    list = [k for k in range(list_size)]
    #On initialise une variable qui compte le nombre de dérangements parmi le nombre total de listes générées
    number_derangements = 0

    #On répère n fois la génération :
    for loop in range(repetitions):
        #On génère une liste aléatoire avec la fonction prédéfinie
        #Puis on utilise check_order pour vérifier si cette nouvelle liste est un dérangement ou non
        #En effet, en comparant avec une liste ordonnée de 1 à n, on vérifie bien que chaque élément n'a pas pour
        #valeur sa position dans la liste, ce qui revient à vérifier si c'est un dérangment.
        #On ajoute le résultat au nombre de dérangements (puisque la fonction renvoie 0 si ça n'en est pas un)
        number_derangements += check_order(list, randomize_list(list))

    #On fait le quotient pour approcher la limite
    result = number_derangements/repetitions
    #On renvoie le résultat
    return result

#On affiche le résultat
print("Question 1)c)\nVoici une approximation du résultat de la question C)4) :")
#On évalue la fonction avec une grande valeur de n pour s'approcher de la limite en +∞
#On constate que le résultat s'approche de e^-1
print(limit_derangements(1000, 1000))

#Question 2)a)

def factorial(n):
    """Calcule et renvoie la factirielle de n (n!)"""
    number = 1
    #On effectue le produit en multipliant par les entiers successifs de 1 jusqu'à n
    for loop in (range(1, n+1)):
        number *= loop
    #On retourne le résultat
    return number

def Dn(n):
    """Renvoie le nombre de dérangements que l'on peut former avec une liste à n éléments"""
    #On élimine le cas où l'on demande le nombre de dérangment d'une liste qui à un nombre d'éléments négatif, cela n'a pas de sens
    assert n >= 0, "La taille de la liste doit être positif"

    sum = 0
    #On applique la formule démontrée en sommant le résultat de la somme actuelle avec le résultat précédent
    for sum_index in range(n+1):
        sum += (-1)**sum_index * (1/factorial(sum_index))
    #Enfin, on multiplie par la factorielle hors de la somme, on convertit en entier (la division a transformé
    #le résultat en flottant) et on renvoie le résultat
    return int(factorial(n) * sum)

#Question 2)b)

#La probabilité correspond au nombre de cas qui vérifient la condition (Dn(48) renvoie le nombres de combinaisons qui
#conviennent (d'après énonncé question B)2))), divisé par le nombre total de distributions donnée par 48! (d'après question B)1))
#On arrondi le résultat a 3 chiffres après la virgule avec la fonction round.
probability = round(Dn(48)/factorial(48), 3)

#On affiche le résultat
print("Question 2)c)\nVoici la probabilité que chaque élève reparte avec un cadeau différent du sien :")
print(probability)

#Question 2)c)

#On affiche simplement la valeur souhaitée avec la fonction prédéfinie.
print("Question 2)c)\nVoici la valeur de d5 :")
print(Dn(5))

#Question 2)d)

def calculate_derangements(size):
    """Renvoie la liste de tous les dérangements possibles d'une liste à n éléments qui contient les entiers de 1 à n"""

    #D'abord, on créer les listes des valeurs que peut prendre chaque élément de la liste dans les dérangments.
    #Par exemple, le premier élément ne peut pas prendre la valeur 1, mais toutes les autres.

    #On fait une liste de liste avec toutes les valeurs possibles
    possible_numbers = [[k for k in range(1, size + 1)] for elem in range(size)]
    #Pour chaque sous-liste, on retire la valeur que cet élément ne pourra pas prendre dans le dérangement.
    #Par exemple, on enlève "1" à la première liste, qui correspond au premier élément des dérangements.
    for number_index in range(1, size + 1):
        possible_numbers[number_index - 1].pop(number_index - 1)

    #Ensuite, on veut générer touts dérangements possibles.
    result_list = [] #On initialise la liste finale qui contiendra touts les dérangements

    #On boucle toutes les possibilités de listes possibles (en ayant éléminé les valeurs qui ferait que la liste ne serait pas un dérangement)
    #"index" contient le numéro de la possibilité en cours de traitement
    index = 0
    #On cherche les dérangmements tant que l'on ne les a pas tous trouvés
    #(On s'arrête quand le nombre de résultats est égal au nombre de dérangements donné par la fonction Dn)
    while len(result_list) < Dn(size):
        index += 1
        new_list = [] #new_liste correspond à une possibilité de liste possible

        #On boucle chaque élément de la liste pour les ajouter 1 par 1
        for occurence in range(size):
            #On calcule la valeur que l'on veut ajouter à la liste en cours, avec une formule intuitée qui donne les combinaisons
            #des valeurs de la liste en fonction du numéro de la liste (index). Cette formule permet de générer toutes les
            #combinaisons de liste possibles sans utiliser des boucles imbriquées (ici on ne connait pas la taille de la liste, c'est le paramètre de la fonction)
            number_to_add = possible_numbers[occurence][int((index/(size-1)**(size-occurence-1)) % (size - 1))]

            #Avant d'ajouter le nombre, on vérifie qu'il n'est pas déjà dans la liste.
            #S'il n'y est pas, alors on ajoute le nombre dans la liste
            if number_to_add not in new_list:
                new_list.append(number_to_add)
            #S'il y est déjà, alors ce n'est pas un dérangement puisque il y a deux fois le même élément dans la liste.
            #On décide d'arrêter de générer cette liste puiqu'elle ne convient pas quoiqu'il arrive par la suite
            else:
                break

        #On vérifie que la liste est bien complète (pour le pas prendre en compte le cas précédent
        #où l'on a décidé d'arrêter de générer une liste puisqu'elle ne convient pas)
        if len(new_list) == size:
            #Cette liste convient. En effet, elle ne prend pas une valeur qui est la même que sa position (on a éléiminé les cas)
            #Et on a vérifié qu'elle ne contient pas plusieurs fois le même élément. On l'ajoute à la liste des résultats finaux.
            result_list.append(new_list)
    return result_list

#Enfin, on calcule les dérangements de la liste [1, 2, 3, 4, 5], qui est la liste qui contient les entiers de 1 à 5
#On applique donc la fonction de calcul des dérangements avec comme paramètre "5"
print("Question 2)d)\nVoici tous les dérangements de la liste [1, 2, 3, 4, 5] :")
print(calculate_derangements(5))
