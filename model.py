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
            n = self.vrstice
            m = self.stolpci
            vsota = []
            vrstica = []
            for i in range(n):
                for j in range(m):
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
            n = self.vrstice
            m = self.stolpci
            razlika = []
            vrstica = []
            for i in range(n):
                for j in range(m):
                    vrstica.append(self.matrika[i][j] - other.matrika[i][j])
                razlika.append(vrstica)
            return Matrika(razlika)
    def sled_matrike(self):
        #funkcija, ki izračuna sled matrike
        if not self.vrstice == self.stolpci:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            n = self.vrstice
            sled = 0
            for i in range(n):
                sled += self.matrika[i][i]
            return sled

    def transponiraj_matriko(self):
    # fukcija, ki bo transponirala matriko
        n = self.vrstica
        m = self.stolpec
        transponiranka = []
        vrstica = []
        for i in range(n):
            for j in range(m):
                vrstica.append(self.matrika[j][i])
                transponiranka.append(vrstica)
        return transponiranka

    def potencirajmo_celene_matrike(self,k): 
    #funkcija, ki bo potencirala matriko
    #pogoji so, da je kvadratna torej
        if self.vrstice != self.stolpci:
            return Exception("POZOR! Matrika ni kvadratna!")

        else:
            n = self.vrstice 
            m = self.stolpci
            matrikca = []
            vrstica = []
            for i in range(n):
                for j in range(m):
                    vrstica.append(self.matrika[i**int(k)][j**int(k)])
                    matrikca.append(vrstica)
            return matrikca

    def __mul__(self,other):
        #funkcija, za množenje matrike 
            if self.stolpci != other.vrstice:
                return Exception("POZOR! Dimenzije matrik se ne ujemajo!")
            else:
                n = self.vrstice
                m = other.stolpci
                l = other.vrstice
                matrikca = []
                #POTREBNO BO ŠE DEFINIRATI MATRIKO, Z DIM. m×l LE-TA PA BO IMELA POVSOD SAME NIČLE
                for i in range(n):
                    for j in range(m):
                        for k in range(l):
                            matrikca.append(self.matrika[i][k]*other.matrika[k][j])
                return matrikca


# funkcija, ki izračuna inverz matrike
#funkcija, za množenje s vektorji
#funkcija za MNK
# sistem linearnih enačb 