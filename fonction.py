import matplotlib.pyplot as plt
import matplotlib

def trace(x, y, b, m):
    point = float(max(x)) * float(m) + float(b)
    nuage = plt.figure()
    plt.scatter(x,y,s=300,color='red',zorder=2)
    nuage.savefig('nuage')
    plt.close()
    droite = plt.figure()
    plt.plot([max(x), 0.0], [point, b],zorder=1)
    plt.grid()
    droite.savefig('droite')
    plt.close()
    full = plt.figure()
    plt.scatter(x,y,s=300,color='red',zorder=2)
    plt.plot([max(x), 0.0], [point, b],zorder=1)
    plt.grid()
    full.savefig('full')
    plt.close()
