from random import random, gauss
from math import sin, pi, cos

##########################################################################
################## Estimation d'une esperance ############################
##########################################################################

## Premier cas : variables de loi N(m,1), avec
## m fixe, mais inconnu.

m = 1.2 # La valeur de m (que l'on cherche a deviner)

def estimation_1(N):
    moy = sum([gauss(m,1) for i in range(N)]) / N # Moyenne empirique de N variables gaussiennes
    largeur = 1.96 * N**-0.5 # La demi-largeur de l'intervalle de confiance a 95%
    return moy-largeur , moy+largeur


print("-----------------------------------------")
print("Methode de Monte Carlo pour des variables\nde loi N(m,1). On cherche m.")
print("-----------------------------------------")
print("Valeur theorique : %f" % m)
for N in [100, 1000, 10000]:
    a,b = estimation_1(N)
    print("Intervalle de confiance pour %d simulations : [ %f , %f ]" % (N,a,b))

N_IC = 1000 # Nombre d'intervalles de confiance calcules
N = 100 # Nombre de variables pour calculer un intervalle de confiance
nb_succes = 0
for i in range(N_IC):
    a,b = estimation_1(N)
    if a<m<b:
        nb_succes += 1
print("Sur %d intervalles de confiance calcules avec %d variables, %f%% contenaient la valeur theorique." % (N_IC, N, nb_succes*N/float(N_IC)))
print

########################################################

## Deuxieme cas : variables de loi B(p), avec
## p fixe, mais inconnu.

p = 0.23 # La valeur de p (que l'on cherche a deviner)

def bernoulli():
    if random()<p:
        return 1
    else:
        return 0

def estimation_2(N):
    moy = sum([bernoulli() for i in range(N)]) / float(N) # Moyenne empirique de N variables gaussiennes
    largeur = 1.96 * N**-0.5 / 2 # La demi-largeur de l'intervalle de confiance a 95%. Le 1/4 est une majoration de sqrt(p(1-p)).
    return moy-largeur , moy+largeur


print("-----------------------------------------")
print("Methode de Monte Carlo pour des variables\nde loi B(p). On cherche p.")
print("-----------------------------------------")
print("Valeur theorique : %f" % p)
for N in [100, 1000, 10000]:
    a,b = estimation_2(N)
    print("Intervalle de confiance pour %d simulations : [ %f , %f ]" % (N,a,b))

N_IC = 1000 # Nombre d'intervalles de confiance calcules
N = 100 # Nombre de variables pour calculer un intervalle de confiance
nb_succes = 0
for i in range(N_IC):
    a,b = estimation_2(N)
    if a<p<b:
        nb_succes += 1
print("Sur %d intervalles de confiance calcules avec %d variables, %f%% contenaient la valeur theorique." % (N_IC, N, nb_succes*N/float(N_IC)))
print

##################################################

## Troisiem cas : variables de loi N(m,sigma^2), avec
## m et sigma fixes, mais inconnus On cherche m.

m = -2.5 # La valeur de m (que l'on cherche a deviner)
s2 = 3.4 # La valeur de sigma^2, inconnue.

def estimation_3(N):
    X = [gauss(m,s2) for i in range(N)]
    moy = sum(X) / N # Moyenne empirique de N variables gaussiennes.
    moy_carres = sum([x**2 for x in X])/N # Moyenne empirique des carres des variables precedentes.
    s2_n = moy_carres - moy**2
    largeur = 1.96 * (s2_n/N)**0.5 # La demi-largeur de l'intervalle de confiance a 95%. On a remplace sigma par son estimation.
    return moy-largeur , moy+largeur


print("-----------------------------------------")
print("Methode de Monte Carlo pour des variables\nde loi N(m,sigma^2). On cherche m.")
print("-----------------------------------------")
print("Valeur theorique : %f" % m)
for N in [100, 1000, 10000]:
    a,b = estimation_3(N)
    print("Intervalle de confiance pour %d simulations : [ %f , %f ]" % (N,a,b))

N_IC = 1000 # Nombre d'intervalles de confiance calcules
N = 100 # Nombres de variables pour calculer un intervalle de confiance
nb_succes = 0
for i in range(N_IC):
    a,b = estimation_3(N)
    if a<m<b:
        nb_succes += 1
print("Sur %d intervalles de confiance calcules avec %d variables, %f%% contenaient la valeur theorique." % (N_IC, N, nb_succes*N/float(N_IC)))
print


###############################################################################
#################### Calcul approche d'integrale ##############################
###############################################################################

## Calcul approche de l'integrale de I=cos(x)/x^1/3 sur [0,1]

print("---------------------------------------")
print("Estimation par methode de Monte Carlo\nde l'integrale de cos(x)/x^(1/3) sur [0,1].")
print("---------------------------------------")

N = 1000 # Nombre de simulation


## Premiere methode : I = E(f(U)), ou U suit une loi uniforme sur [0,1].
def f(x):
    return cos(x) * x**-(1.0/3)

simus = [f(random()) for i in range(N)] # Les simulations des f(U).

# La moyenne et la variance empirique des f(U).
moy = sum(simus)/N
var = sum(s**2 for s in simus)/N - moy**2
print("Intervalle de confiance (premiere methode) :")
print("[ %f , %f ]" % (moy - 1.96*(var/N)**0.5 , moy + 1.96*(var/N)**0.5)) # On affiche un intervalle de confiance a 95%.


## Deuxieme methode : I = E(g(X)), ou X=U^(3/2), et U de loi uniforme sur [0,1].

def g(x):
    return 1.5*cos(x)

simus = [g(random()**1.5) for i in range(N)] # Les simulations de g(X).

moy = sum(simus)/N
var = sum(s**2 for s in simus)/N - moy**2 
print("Intervalle de confiance (deuxieme methode) :")
print("[ %f , %f ]" % (moy - 1.96*(var/N)**0.5 , moy + 1.96*(var/N)**0.5)) # On affiche un intervalle de confiance a 95%.
print


########################################################
#################### En grande dimension ################
########################################################

## Calcul du volume de la boule unite de dimension d.

from math import gamma

d = 10 # La dimension

def X(): # X() suit une loi uniforme sur [-1,1]^d.
    return [2*random()-1 for i in range(d)]

def boule_unite(x):
    if sum([t**2 for t in x])<1:
        return 2.**d # Volume de [-1,1]^d
    else:
        return 0.

N = 1000000 # Nombre de simulations

simus = [boule_unite(X()) for i in range(N)]

moy = sum(simus)/N
var = sum(s**2 for s in simus)/N - moy**2
print("--------------------------------------------------------")
print("Estimation du volume de la boule unite en dimension %d."%d)
print("--------------------------------------------------------")
print("Valeur theorique : %f" % (pi**(0.5*d)/gamma(0.5*d+1)))


print("Intervalle de confiance construit a partir de %d simulations." % N)
print([moy - 1.96*(var/N)**0.5 , moy + 1.96*(var/N)**0.5])
