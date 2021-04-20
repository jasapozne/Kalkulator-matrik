class Matrika:

    def __init__(self, matrika):
        self.matrika = matrika
        self.stolpci = len(matrika[0]) #j
        self.vrstice = len(matrika) #i
        
    
    def __str__(self):
        #naj funkcija uredi matriko, tako da se vsaka vrstica začne v svoji vrstici
        # *Kasneje (mogoče) dodaj še vejice med posamezne elemente za še lepši izpis
        matrikca = ""
        for vrstica in self.matrika:
            matrikca += str(vrstica) + '\n'
        return matrikca
    
    def __eq__(self, other):
        return self.matrika == other.matrika

    def __repr__(self):
        return "Matrika({0})".format(self.matrika)

    def __add__(self, other):
        #funkcija bo seštela dve matriki
        #najprej naj bo kaj se zgodi, če pogoji seštevanja niso "mogoči"
        if  self.vrstice != self.stolpci or other.vrstice != other.stolpci:
            raise Exception("POZOR! Matriki nista kvadratni!")

        elif self.vrstice != other.vrstice or self.stolpci != other.stolpci:
            raise Exception("POZOR! Matriki sta raličnih velikosti!")
        #če pogoji seštevanja so "mogoči"
        else:
            m = self.vrstice
            n = self.stolpci
            vsota = []
            vrstica = []
            for i in range(m):
                for j in range(n):
                    vrstica.append(self.matrika[i][j] + other.matrika[i][j])
                vsota.append(vrstica)
            return Matrika(vsota)

    def __sub__(self, other):
        #prvi del podoben kot pri seštevanju, 
        # tj. pogoji odštevanja niso mogoči
        if  self.vrstice != self.stolpci or other.vrstice != other.stolpci:
            raise Exception("POZOR! Matriki nista kvadratni!")

        elif self.vrstice != other.vrstice or self.stolpci != other.stolpci:
            raise Exception("POZOR! Matriki sta raličnih velikosti!")
        #pogoji so mogoči
        else:
            m = self.vrstice
            n = self.stolpci
            razlika = []
            vrstica = []
            for i in range(m):
                for j in range(n):
                    vrstica.append(self.matrika[i][j] - other.matrika[i][j])
                razlika.append(vrstica)
            return Matrika(razlika)
