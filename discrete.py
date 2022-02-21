# On inclut la bibliotheque permettant de manipuler de l'aleatoire.
from random import random

# On inclut la bibliotheque graphique
from matplotlib.pyplot import hist, show, plot, title, axis

def unif(a,b):
    """ Simule une variable aleatoire uniforme sur [a,b]."""
    return a+(b-a)*random()

def unif(N):
    """Renvoie une variable uniforme sur l'ensemble {0,1,...,N-1}"""
    return int(N*random())

def bernoulli(p):
        """Renvoie une la valeur 0 avec probabilite 1-p, et la valeur 1 avec probabilite p. 
        Il s'agit d'une variable de Bernoulli de parametre p."""
        if random()<p:
            return 1
        else:
            return 0

def binomiale(n,p):
        """Renvoie une realisation d'une variable aleatoire de loi binomiale de parametres n et p."""
        return sum( [bernoulli(p) for i in range(n)] )
        
def simu_X():
        """Simule une variable aleatoire a valeurs dans {0,1,2,3}, avec le probabilites suivantes :
        p_0 = 1/2   ;   p_1 = 1/4   ;   p2 = 1/6   ;   p3 = 1/12"""
        U = random()
        if U<1./2:
            return 0
        elif U<1./2 + 1./4:
            return 1
        elif U<1./2 + 1./4 + 1./6:
            return 2
        else:
            return 3
        
def loi_discrete(pi):
    """Renvoie une simulation de la loi (p_0,...,p_N).
    L'argument a fournir a la fonction est le vecteur (p_0,...,p_{N-1}) (la valeur de p_N est calculee).
    Ce vecteur doit etre positif, et la somme de ses coefficients inferieure a 1."""
    if min(pi)<0 or sum(pi)>1:
        print("pi n'est pas une probabilite")
        return
    x = random()
    somme = 0
    for i in range(len(pi)):
        somme += pi[i]
        if x<somme:
            return i
    return len(pi)

if __name__ == "__main__":
    
    ##### Uniforme #####
    
    n = 30
    hist([unif(n) for k in range(100)], bins=30, range=(-0.5,29.5))
    title("100 simulations d'une variable uniforme sur {0,1,...,29}")
    axis([-0.5,29.5,0,10])
    show()

    hist([unif(n) for k in range(1000)], bins=30, range=(-0.5,29.5))
    title("1000 simulations d'une variable uniforme sur {0,1,...,29}")
    axis([-0.5,29.5,0,100])
    show()

    hist([unif(n) for k in range(10000)], bins=30, range=(-0.5,29.5))
    title("10000 simulations d'une variable uniforme sur {0,1,...,29}")
    axis([-0.5,29.5,0,1000])
    show()

    ##### Bernoulli #####

    p = 0.3
    print("Dix variables de Bernoulli de parametre %f" % p)
    for i in range(10):
        print(bernoulli(p))
    print


    ##### Binomiale #####

    n = 20
    p = 0.3
    nb_simus = 10000
    hist([binomiale(n,p) for i in range(nb_simus)], normed=True, bins=21, range=(-0.5,20.5))
    p_theorique = [1] * (n+1)
    for k in range(n+1):
        p_theorique[k] *= (p ** k) * ((1-p)**(n-k))
        fact = 1
        for q in range(k):
            fact *=  (n-q) / (q+1.)
        p_theorique[k] *= fact
    plot(p_theorique, 'or')
    axis([-0.5,20.5,0,0.2])
    title("Histogramme de %d simulations d'une\nbinomiale(%d, %.2f) et valeur theorique" % (nb_simus,n,p))
    show()



    ##### Convergence par LFGN #####

    p = 0.4
    n = 1000
    X_n = [bernoulli(p) for i in range(n)]
    Y_n = [sum(X_n[:i])/float(i) for i in range(1,n+1)]
    plot(Y_n)
    plot([0,n],[p, p], '--k')
    axis([0,n,0,1])
    title("Convergence de 1/n \sum X_i vers p, pour\ndes Bernoulli(%.2f), avec n=%d" % (p,n))
    show()



    ##### Loi arbitraire #####


    hist([simu_X() for k in range(1000)], bins=4, range=(-0.5,3.5), normed=True)
    plot([0,1,2,3], [1./2, 1./4, 1./6, 1./12], 'ro')
    axis([-0.5,3.5,0,0.6])
    title("Histogramme de 1000 realisations de la loi (1/2,1/4,1/6,1/12)")
    show()