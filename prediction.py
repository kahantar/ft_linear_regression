import sys
import os
import numpy as np

def  calcul(theta00, theta01, x):
    x = round((theta00 * x) + theta01, 2)
    if x < 0:
        print("La voiture est gratuite")
    else:
        print("Le prix de la voiture est de {0} euros".format(x))

try:
    km = int(input("Entrez le kilométrage du véhicule : "))
except:
    print("Erreur saisi")
    sys.exit(0)
else:
    if os.path.isfile('value.csv'):
        try:
            fichier = open("value.csv")
        except:
            print("Erreur Fichier")
            sys.exit(0)
        else:
            data = fichier.read()
            fichier.close()
            try:
                [x, y] = data.split(',')
                theta00 = float(x)
                theta01 = float(y)
            except:
                print("Erreur Fichier")
                sys.exit(0)
            else:
                calcul(theta00, theta01, km)
    else:
        calcul(0, 0, km)
