from random import random
from matplotlib.pyplot import hist, show, plot
from math import tan, pi, exp

######### Loi des grands nombres #########

nb_simus = 10000

def LGN(X):
    somme = 0.
    moyennes = []
    for i in range(nb_simus):
        somme += X() 
        moyennes.append( somme/(i+1.) )
    plot(moyennes, 'g')
    

def cauchy():
    return tan(pi*random())
    
def pareto0_5():
    return random()**-2

def pareto2():
    return random()**-0.5

#### Variables uniformes ####
# Par la loi des grands nombres, on a convergence vers E[U] = 1/2
plot([0,nb_simus], [0.5, 0.5], 'r')
for i in range(5):
    LGN(random)
show()

#### Variables de loi de Pareto de parametre 2 ####
# Par la loi des grands nombres on a convergence vers E[1/sqrt(U)] = 2
plot([0,nb_simus], [2, 2], 'r')
for i in range(5):
    LGN(pareto2)
show()

#### Loi de Cauchy #####
# La suite n'est presque sûrement pas bornée (car la loi de Cauchy n'est pas intégrable)
for i in range(5):
    LGN(cauchy)
show()

#### Loi de Pareto de parametre 0.5 #####
# La suite tend vers +oo (car la loi de Pareto de parametre 0.5 est positive et non integrable) 
for i in range(5):
    LGN(pareto0_5)
show()

############ Theoreme limite central ##########


def somme(N): # Somme de N variables uniformes sur [2,3]
    x = 0.
    for i in range(N):
        x += (2+random())
    return x

for N in range(1,12):
    x = []
    for k in range(10000):
        x.append( somme(N) )
    hist(x, bins=5*N, normed=True, color=((N-1)/10., 0, (11-N)/10.))
show()



############# Histogramme / loi normale ###########

def moyenne(N):
    x = 0.
    for i in range(N):
        x += random()
    return (12*N)**0.5 * (x/N - 0.5)


x = [moyenne(100) for k in range(10000)]
hist(x, normed=True, bins=40)
t = [i/100. for i in range(-300, 300)]
plot(t, [exp(-u**2/2)*(2*pi)**-0.5 for u in t], 'r')
show()
