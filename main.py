class Periodensystem:
    def __init__(self):
        self.elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
        self.valElek = [1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    def getValElek(self, ordZahl):
        return self.valElek[ordZahl - 1]
    def getSymbol(self, ordZahl):
        return self.elements[ordZahl - 1]

class Element:
    def __init__(self, ordZahl):
        self.p = Periodensystem()
        self.ordZahl = ordZahl
        self.valElek = self.p.getValElek(self.ordZahl)
        self.symbol = self.p.getSymbol(self.ordZahl)
        print(str(self.valElek))
        print(str(self.symbol))

e = Element(17)
