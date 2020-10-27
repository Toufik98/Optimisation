# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:25:15 2020

UE MU4MEN01 - Introduction à l'optimisation

Programme cadre pour le TP n°2

@author: Florence Ossart, Sorbonne Université
"""

#%% Programme de test de la recherche de minimum par dichotomie

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
