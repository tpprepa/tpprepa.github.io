import matplotlib.pyplot as plt
import math as m
import numpy as np
import random as rd

h = .5* m.sqrt(3)
r = .5

nbC = 50
nbL = 50

def coordCentre(i,j):
    """Coordonnées du sommet sur la ième colonne et la ji_me ligne"""
    if j%2 == 0 :
        return (i , j*h)
    else :
        return (i+.5, j*h)

def separe(listeBoulesRouges,grilleBoules):
    """Renvoie la liste des boules coloriées en noir"""
    nbC, nbL = len(grilleBoules), len(grilleBoules[0])-2
    T = [(i,j) for i in range(nbC) for j in range(nbL)]
    T.append((0,nbL))
    listeBoulesNoires = []
    for (i,j) in T :
        if (grilleBoules[i][j] and (i,j) not in listeBoulesRouges) :
            listeBoulesNoires.append((i,j))
    return listeBoulesNoires

def trace(listeBoulesRouges, grilleBoules):
    """Représente les boules connectées à la plaque du bas
    listeBoulesRouges : liste des sommets coloriés en rouge
    grilleBoules : liste de liste des booléens (cf. exemple)"""
    nbC, nbL = len(grilleBoules), len(grilleBoules[0])-2
    listeBoulesNoires = separe(listeBoulesRouges, grilleBoules)
    plt.clf()
    plt.plot([-1,nbC],[-.5,-.5],"r")
    if (0,nbL) in listeBoulesRouges :
        couleur = "r"
    else :
        couleur = "k"
    plt.plot([-1,nbC],[(nbL-1)*h+.5,(nbL-1)*h+.5],couleur)
    for (i,j) in listeBoulesRouges :
        if 0 <= j < nbL:
            x,y = coordCentre(i,j)
            cercle = plt.Circle((x,y), .5, color='r')
            plt.gca().add_patch(cercle)
    for (i,j) in listeBoulesNoires:
        if 0 <= j < nbL:
            x,y = coordCentre(i,j)
            cercle = plt.Circle((x,y), .5, color='k')
            plt.gca().add_patch(cercle)
    plt.axis("equal")
    plt.show()


