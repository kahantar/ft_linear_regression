from fractions import Fraction
import matplotlib.pyplot as plt
import fonction
import os
from decimal import Decimal

class resolution:
    def __init__(self, data):
        self.prix = []
        self.km = []
        self.data = data
        self.x = 0
        self.y = 0
        self.xy = 0
        self.xcarre = 0
        self.mx = 0
        self.my = 0
        self.mxy = 0
        self.mxcarre = 0
        self.m = 0
        self.b = 0

    def add(self):
        i = 1
        for data in self.data:
            self.x = data[0] + self.x
            self.y = data[1] + self.y
            self.xy = (data[0] * data[1]) + self.xy
            self.xcarre = (data[0] * data[0]) + self.xcarre
            self.prix.append(data[0])
            self.km.append(data[1])
            self.mx = Fraction(self.x, i)
            self.my = Fraction(self.y, i)
            self.mxcarre = Fraction(self.xcarre , i)
            self.mxy = Fraction(self.xy, i)
            if i > 1:
                self.m = (self.mxy - (self.my * self.mx)) / (self.mxcarre - (self.mx * self.mx))
                self.b = self.my - (self.m * self.mx)
            i += 1
        fonction.trace(self.prix, self.km, self.b, self.m)
        self.fichier()

    def fichier(self):
        x = str(float(self.m)) + ',' + str(float(self.b))
        f = open('value.csv','w')
        f.write(x)
        f.close()
