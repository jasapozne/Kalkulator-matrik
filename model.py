import numpy as np

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
            for i in range(n):
                vrstica = []
                for j in range(m):
                    vrstica.append(self.matrika[i][j] + other.matrika[i][j])
                vsota.append(vrstica)
            return Matrika(vsota)

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
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self.matrika[j][i])
            transponiranka.append(vrstica)
        return transponiranka

    def mnozenje_vseh_clenov_s_k(self,k): 
        n = self.vrstice 
        m = self.stolpci
        matrikca = []
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self.matrika[i][j]*int(k))
            matrikca.append(vrstica)
        return matrikca
    
    def odstevanje_matrik(self, other):
        return __add__(self.matrika, mnozenje_vseh_clenov_s_k(self,-1))

    def matrika_s_samimi_niclami(self):
        #pomožna funkcija za pomoč pri množenju
        n = self.vrstice
        m = self.stolpci
        matrikca = []
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self.matrika[i][j] *0)
            matrikca.append(vrstica)
        return matrikca
    
    def nicelni_seznam(self):
        #pomožna funkcija za normiranje
        m = self.stolpci
        sez = []
        for j in range(m):
            sez[j]=0
        return sez

    
    def __mul__(self,other):
        #funkcija, za množenje matrike 
            if self.stolpci != other.vrstice:
                raise Exception("POZOR! Dimenzije matrik se ne ujemajo!")
            else:
                n = self.vrstice
                m = other.stolpci
                l = other.vrstice
                matrikca = matrika_s_samimi_niclami(self.matrika)
                for i in range(n):
                    for j in range(m):
                        for k in range(l):
                            matrikca[i][j] += self.matrika[i][k]*other.matrika[k][j]
                return matrikca

    def inverz_matrike(self):
    # funkcija, ki izračuna inverz matrike
        if self.stolpci != self.vrstice:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            return np.linalg.inv(np.self.matrika) 

    def sistem_linearnih_enacb(self,other):
        #sistem linearnih enačb
        if self.stolpci != other.vrstice:
            raise Exception("POZOR! Dimenzije matrik se ne ujemajo!")
        elif other.stolpci != 1:
            raise Exception("POZOR! Sistem enačb ima lahko ima eno rešitev!")
        else:
            return __mul__(inverz_matrike(self.matrika),other.matrika)

    def dolzina_vektorjev(self):
        #pomožna funkcija
        n = self.vrstice
        m = self.stolpci
        sez = nicelni_seznam(self.matrika)
        for i in range(n):
            for j in range(m):
                for k in range(len(sez)):
                    if j==k:
                        sez[k] += (self.matrika[i][j]) ** 2
                    else:
                        pass
        return sez
    
    def dolzine_sestete(self):
        #pomožna funkcija 
        sez = dolzina_vektorjev(self.matrika)
        for h in range(len(sez)):
            sez[h]=sez[h] ** (1/2)
        return sez
    
    def seznam_veckratnih_dolzin(self):
        #pomožna funkcija
        #funkcija vrne prejšni seznam kot matriko z elementi večkrat ponovljenimi
        sez = dolzine_sestete(self.matrika)
        ponavljaj = self.vrstice
        sez_kot_matrika = [sez]*self.vrstice
        return sez_kot_matrika

    def normiranje(self):
        n = self.vrstice
        m = self.stolpci
        sez = seznam_veckratnih_dolzin(self.matrika)
        matrikca = matrika_s_samimi_niclami(self.matrika)
        for i in range(n):
            for j in range(m):
                matrikca[i][j] += self.matrika[i][j] * 1/sez[i][j]
        return matrikca                   

    def izracun_determinante(self):
        # determinanta
        #matrika mora biti
        if self.vrstice != self.stolpci:
            raise Exception("POZOR! Matrika ni kvadratna!")
        #če bo 1×1
        elif self.stolpci == 1: #and self.vrstica==1 
            return self.matrika[0][0]
        #če bo matrika 2×2
        elif self.stolpci == 2:
            return self.matrika[0][0] * self.matrika[1][1] - self.matrika[0][1] * self.matrika[1][0]
        #sicer
        else:
            A = self.matrika
            determinanta = 0
            indeksi = list(range(self.matrika.vrstice))
            for stolpci in indeksi:
                matrikca = self.matrika 
                matrikca = matrikca[1:]
                visina = len(matrikca)
                for i in range(visina): 
                    matrikca[i] = matrikca[i][0:stolpci] + matrikca[i][stolpci+1:] 
                predznak = (-1) ** (stolpci % 2)
                matrikca = Matrika(matrikca)
                poddeterminanta = matrikca.izracun_determinante()
                determinanta += predznak *matrikca[0][stolpci] * poddeterminanta 
            return determinanta
#potenciranje
#MGS