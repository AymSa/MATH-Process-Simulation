# Inclusion des bibliotheques
from random import random
from matplotlib.pyplot import hist, show, plot, title, axis
from math import log, exp, pi, tan, sin, cos


def expo(lambd):
    """Simule une variable aleatoire de loi exponentielle de parametre lambda"""
    return -log(random())/lambd

def cauchy():
        """Simule une variable aleatoire de loi de Cauchy"""
        return tan(pi*(random()-0.5))
    
def pareto(theta):
        """Simule une variable aleatoire de loi de Pareto de parametre theta"""
        return random()**(-1/theta)
    
def arcsinus():
        """Simule une variable aleatoire de loi de l'arcsinus"""
        return sin(pi*(random()-0.5))

def BM():
    """Simule le couple (X,Y) issu de la methode de Box-Muller"""
    R = (-2*log(random()))**0.5
    theta = 2*pi*random()
    return R*cos(theta), R*sin(theta)

def geom(p):
        """Simule une loi geometrique de parametre p"""
        return int( log(random()) / log(p) )

def poisson(lambd):
        """Simule une loi de Poisson de parametre lambd"""
        x = exp(-lambd)
        U = random()
        n = 0
        while U>x:
            U *= random()
            n += 1
        return n


if __name__ == "__main__":
    
    nb_simus = 10000
    n = 1000
    ##################### Loi exponentielle #####################
    
    l = 0.5
    tirages = [expo(l) for i in range(nb_simus)]

    # On trace l'histogramme
    hist(tirages, bins=30, normed=True)

    # On trace la densite (sur l'intervalle [0,L])
    L = max(tirages)
    x = [L*i/float(n) for i in range(n+1)]
    plot(x, [l*exp(-l*x) for x in x], 'r')
    title("Loi exponentielle : histogramme et densite theorique")
    show()

    ##################### Loi de Cauchy #####################


    tirages = [cauchy() for i in range(nb_simus)]

    # On trace l'histogramme (sur l'intervalle [-L,L])
    L = 6
    hist(tirages, bins=30, normed=True, range=(-L,L))

    # La densite
    x = [L*i/float(n) for i in range(-n,n+1)]
    plot(x, [(1+x**2)**-1/pi for x in x], 'r')
    axis([-L,L,0,1.5/pi])
    title("Loi de Cauchy : histogramme et densite theorique")
    show()




    ##################### Loi de Pareto #####################

    

    theta=1.5
    tirages = [pareto(theta) for i in range(nb_simus)]

    # On trace l'histogramme sur [0,L]
    L = 10
    hist(tirages, bins=30, normed=True, range=(0,L))

    # La densite
    x = [1+L*i/float(n) for i in range(n)]
    plot(x, [theta*x**(-1-theta) for x in x], 'r')
    axis([1,L,0,0.5])
    title("Loi de Pareto : histogramme et densite theorique")
    show()




    ##################### Loi de l'arcsinus #####################

    
    tirages = [arcsinus() for i in range(nb_simus)]

    # Trace de l'histogramme
    hist(tirages, bins=30, normed=True)

    # ... et de la densite
    x = [i/float(n) for i in range(-n+1,n)]
    plot(x, [(1-x**2)**-0.5/pi for x in x], 'r')
    axis([-1,1,0,1])
    title("Loi de l'arcsinus : histogramme et densite theorique")
    show()



    ################## Methode de Box-Muller #################

   

    # Tirages contient les couples (X,Y)
    tirages = [BM() for i in range(nb_simus)]
    x = [t[0] for t in tirages] # On stocke dans x les premieres coordonnees...
    y = [t[1] for t in tirages] # ... et dans y les secondes

    plot(x, y, 'x')
    title("10000 points obtenus par la methode de Box-Muller")
    axis([-4,4,-4,4])
    show()

    # L'histogramme, obtenu a partir de x
    hist(x, normed=True, bins=30)
    t = [i/float(n) for i in range(-4*n,4*n)]
    plot(t, [exp(-t**2/2)*(2*pi)**-0.5 for t in t], 'r') # La densite
    title("Histogramme et densite d'une variable gaussienne")
    axis([-4,4,0,0.5])
    show()





    ################## Loi geometrique #################

    p = 0.5
    kmax = 10
    tirages = [geom(p) for i in range(nb_simus)]
    # L'histogramme simule
    hist(tirages, normed=True, bins=kmax, range=(-0.5,kmax-0.5))

    # On affiche l'histogramme theorique
    plot(range(kmax), [p**k*(1-p) for k in range(kmax)], 'or')
    axis([-0.5,kmax-0.5,0,1])
    title("Histogramme de la loi geometrique et valeurs theoriques")
    show()


    ################## Loi de Poisson ################# 

    l = 3
    kmax = 10
    tirages = [poisson(l) for i in range(nb_simus)]
    # L'histogramme simule
    hist(tirages, normed=True, bins=kmax, range=(-0.5,kmax-0.5))

    # On calcule l'histogramme theorique
    poisson_theorique = []
    prob = exp(-l) # pour chaque i, prob vaut exp(-l) * l^i/i!
    for i in range(kmax):
        poisson_theorique.append(prob)
        prob *= l/float(i+1)
    plot(range(kmax), poisson_theorique, 'or')
    axis([-0.5,kmax-0.5,0,0.4])
    title("Histogramme de la loi de Poisson et valeurs theoriques")
    show()