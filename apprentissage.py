import pandas as pd
import numpy as np
import entrainement
import sys
import fonction

if len(sys.argv) != 2:
    print("Erreur Parametre")
    sys.exit()    
chemin = sys.argv[1]
data = np.recfromcsv(chemin, delimiter=',')
entrainement = entrainement.resolution(data)
entrainement.add()