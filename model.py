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
    
    def __getitem__(self, indeks):
        return self.matrika[indeks]
        
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
        n = self.vrstice
        m = self.stolpci
        transponiranka = []
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self.matrika[j][i])
            transponiranka.append(vrstica)
        return Matrika(transponiranka)

    def mnozi_k_poteciraj_l(self,k,l): 
        n = self.vrstice 
        m = self.stolpci
        matrikca = []
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append((self.matrika[i][j] ** int(l)) * int(k))
            matrikca.append(vrstica)
        return Matrika(matrikca)
    
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
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self.matrika[i][j] - other.matrika[i][j])
                razlika.append(vrstica)
            return Matrika(razlika)

    def matrika_s_samimi_niclami(self):
        return Matrika([[0 for i in range(self.stolpci)] for j in range(self.vrstice)])
    
    def nicelni_seznam(self):
        return [0 for i in range(self.stolpci)]
    
    def __mul__(self,other):
        #funkcija, za množenje matrike 
            if self.stolpci != other.vrstice:
                raise Exception("POZOR! Dimenzije matrik se ne ujemajo!")
            else:
                matrikca = [[0 for i in range(self.stolpci)] for j in range(other.vrstice)]
                n = self.vrstice
                m = other.stolpci
                l = other.vrstice
                #matrikca = matrika_s_samimi_niclami(self.matrika)
                for i in range(n):
                    for j in range(m):
                        for k in range(l):
                            matrikca[i][j] += self.matrika[i][k]*other.matrika[k][j]
                return Matrika(matrikca)

    def inverz_matrike(self):
    # funkcija, ki izračuna inverz matrike
        if self.stolpci != self.vrstice:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            return Matrika(np.linalg.inv(np.array(self.matrika))) 

    def sistem_linearnih_enacb(self,other):
        #sistem linearnih enačb
        if self.stolpci != other.vrstice:
            raise Exception("POZOR! Dimenzije matrik se ne ujemajo!")
        elif other.stolpci != 1:
            raise Exception("POZOR! Sistem enačb ima lahko ima eno rešitev!")
        else:
            return Matrika(self.matrika.__mul__(other.matrika))

    def norma(self):
        sez=[0 for i in range(self.stolpci)]
        n = self.vrstice
        m = self.stolpci
        for i in range(n):
            for j in range(m):
                for k in range(len(sez)):
                    if j==k:
                        sez[k] += (self.matrika[i][j]) ** 2
                    else:
                        pass

        for h in range(len(sez)):
            sez[h]=sez[h] ** (1/2)

        ponavljaj = self.vrstice
        sez_kot_matrika = [sez]*self.vrstice
        matrikca = [[0 for i in range(self.stolpci)] for j in range(self.vrstice)]
        for i in range(n):
            for j in range(m):
                matrikca[i][j] += self.matrika[i][j] * 1/sez_kot_matrika[i][j]
        return Matrika(matrikca)                   

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
    

    def potenciranje_matrike(self,k):
        #potenciranje
        #pogoji
        if self.vrstice != self.stolpci:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            if k == 0:
                return mnozi_k_poteciraj_l(self.matrika,1,0)
            elif k == 1:
                return self.matrika
            elif k == 2:
                return self.matrika.__mul__(self.matrika)
            elif float(k) < 0:
                raise Exception("POZOR! K mora biti večji od 0!")
            else:
                return Matrika(((self.matrika).__mul__(self.matrika)).__add__(potenciranje_matrike(self.matrika,k-2)))

    @staticmethod
    def identiteta(n):
        matrikca = []
        for i in range(n):
            vrstica = []
            for j in range(n):
                if i == j:
                    vrstica.append(1)
                else:
                    vrstica.append(0)
            matrikca.append(vrstica)
        return matrikca

    def obrnljivost_matrike(self):
        #pogoji
        if self.vrstice != self.stolpci:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            if self.matrika.__mul__(inverz_matrike(self.matrika)) == (inverz_matrike(self.matrika)).__mul__(self.matrika) and  self.matrika.__mul__(inverz_matrike(self.matrika)) == identiteta(self.vrstice):
                return True
            else:
                return False