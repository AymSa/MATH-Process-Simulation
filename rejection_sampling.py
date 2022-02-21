from random import random
from matplotlib.pyplot import plot, show, axis, hist, figure
from math import log, exp, pi, sin, cos

nb_simus = 10000

###### Loi normale par methode du rejet a partir de lois exponentielles #######

C = exp(0.5) # On doit prendre C>=exp(0.5)

nb_rejets = 0
def normale_par_exp():
    global nb_rejets
    while True:
        u = random()
        x = -log(random())
        y = exp(-x)
        if C*y*u<exp(-x**2/2):
            return x
        nb_rejets += 1

figure(1)
simu = [normale_par_exp() for i in range(nb_simus)]
print("Simulation de la loi normale a partir de la loi exponentielle.")
print("On a rejete {0} simulations pour en avoir {1}.".format(nb_rejets, nb_simus))
print("En moyenne, on en rejette {0}.".format((C*(2/pi)**0.5-1)*nb_simus))
print
hist(simu, density=True, bins=30)
x = [i/100. for i in range(400)]
plot(x, [exp(-t**2/2) * (2/pi)**0.5 for t in x], 'r')

# "Explication" de la methode du rejet
figure(2)
bon = []
mauvais = []
for i in range(nb_simus):
    x = -log(random())
    y = C*exp(-x)*random()
    if y>exp(-x**2/2):
        mauvais.append((x,y))
    else:
        bon.append((x,y))
plot([a[0] for a in bon], [a[1] for a in bon], '+g')
plot([a[0] for a in mauvais], [a[1] for a in mauvais], '+r')
x = [i/100. for i in range(800)]
plot(x, [C*exp(-t) for t in x], 'k')
plot(x, [exp(-t**2/2) for t in x], 'k')
show()
