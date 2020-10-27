# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:25:15 2020

UE MU4MEN01 - Introduction à l'optimisation

Programme cadre pour le TP n°2

@author: Florence Ossart, Sorbonne Université
"""
import numpy as np
import matplotlib.pylab as plt
#%% Programme de test de la recherche de minimum par dichotomie
def dichotomie(f, x1, x5):
    x3 = (x1 + x5)/2
    x2 = (x3 + x1)/2
    x4 = (x3 + x5)/2
    x_inf = x1
    x_sup = x5
    
    f1 , f2, f3, f4, f5 = f(x1), f(x2), f(x3), f(x4), f(x5)
    
    if f1 < f2 < f3 < f4 < f5 :
        x_inf = x1
        x_sup = x2
    elif f1 > f2 < f3 < f4 < f5 :
        x_inf = x1
        x_sup = x3
    
    elif f1 > f2 > f3 < f4 < f5 :
        x_inf = x2
        x_sup = x4
    elif f1 > f2 > f3 > f4 < f5 :
        x_inf = x3
        x_sup = x5
    
    elif f1 > f2 > f3 > f4 > f5 :
        x_inf = x4
        x_sup = x5
    
    return x_inf , x_sup
        
def minimumDichotomie(f, x_min, x_max, eps):
    err = False
    bornes_min = []
    bornes_max = []
    n_iter = 0 
    
    x1 , x5 = x_min , x_max
    while x5 - x1 > eps :
        
        bornes_min.append([x1,f(x1)])
        bornes_max.append([x5,f(x5)])
        x1 , x5 = dichotomie(f, x1, x5)
        n_iter = n_iter + 1 
    
    return bornes_min, bornes_max, n_iter, err

#%% Fonction test n°1
def f1(x) :
    return (x+1)**2 + 7*np.sin(x)

#%% Recherche du minimum de f1 sur l'intervalle [-4,4]
x_min = -4
x_max = +4

f = f1
precision = 1e-1
# METHODE minimumDichotomie A CREER
bornes_min, bornes_max, n_iter, ier = minimumDichotomie(f,x_min,x_max,precision)
#
x_min, y_min = bornes_min[0][-1], bornes_min[1][-1]
x_max, y_max = bornes_max[0][-1], bornes_max[1][-1]

# Visualisation des résultats
plt.plot(bornes_min[0],bornes_min[1],'rs', label = 'x_min')
plt.plot(bornes_max[0],bornes_max[1],'bs', label = 'x_max')
plt.legend()
plt.xlabel('Valeurs de $x$')
plt.ylabel('Valeurs de $f_1(x)$')
plt.title('Recherche du minimum de $f_1$ par dichotomie')
plt.grid()

message = 'Precision = {}'.format(precision)
message += '\nCV en {} iterations'.format(n_iter)
message += '\nBorne inférieure :'
message += '\n  x_min = {:6.4f}'.format(x_min)
message += '\n  y_min = {:6.4f}'.format(y_min)
message += '\nBorne supérieure :'
message += '\n  x_max = {:6.4f}'.format(x_max)
message += '\n  y_max = {:6.4f}'.format(y_max)
plt.text(1,-5,message)
