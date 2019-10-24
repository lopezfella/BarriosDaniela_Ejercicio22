import math 
class Complejo():
    
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
        self.norma = math.sqrt(real*real + imaginario*imaginario)

        
    def conjugado(self):
        self.imaginario = -self.imaginario
        

    def calcula_norma(self):
        self.norma = math.sqrt(self.real**2 + self.imaginario**2)
        

    def pow(self, n):
        a = Complejo(self.real, self.imaginario)
        self.calcula_norma()
        r = self.norma ** n
        if abs(self.real)<1E-10:
            theta = math.pi/2.0
        else:
            theta = math.atan(self.imaginario/self.real)
        a.real = r * math.cos(n * theta)
        a.imaginario = r * math.sin(n * theta)
        return a 
    

    def mult(self, a2):
        a1 = Complejo(self.real, self.imaginario)
        a2 = Complejo(self.real, self.imaginario)

        self.mult = (self.real*self.real) + (self.imaginario*self.imaginario)
