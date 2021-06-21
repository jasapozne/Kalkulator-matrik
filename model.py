import numpy as np

class Matrika:
    def __init__(self, matrika):
        self.matrika = matrika
        self.stolpci = len(matrika[0])  # j
        self.vrstice = len(matrika)  # i

    def __str__(self):
        matrikca = ""
        for vrstica in self.matrika:
            matrikca += str(vrstica) + "\n"
        return matrikca

    def __eq__(self, other):
        return self.matrika == other.matrika

    def __repr__(self):
        return "Matrika({0})".format(self.matrika)

    def __getitem__(self, indeks):
        return self.matrika[indeks]

    def __add__(self, other):
        # funkcija bo seštela dve matriki
        # najprej naj bo kaj se zgodi, če pogoji seštevanja niso "mogoči"
        if self.vrstice != self.stolpci or other.vrstice != other.stolpci:
            raise Exception("POZOR! Matriki nista kvadratni!")

        elif self.vrstice != other.vrstice or self.stolpci != other.stolpci:
            raise Exception("POZOR! Matriki sta raličnih velikosti!")
        # če pogoji seštevanja so "mogoči"
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
        # funkcija, ki izračuna sled matrike
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

    def mnozi_k_poteciraj_l(self, k, l):
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
        # prvi del podoben kot pri seštevanju,
        # tj. pogoji odštevanja niso mogoči
        if self.vrstice != self.stolpci or other.vrstice != other.stolpci:
            raise Exception("POZOR! Matriki nista kvadratni!")

        elif self.vrstice != other.vrstice or self.stolpci != other.stolpci:
            raise Exception("POZOR! Matriki sta raličnih velikosti!")
        # pogoji so mogoči
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
        return Matrika([[0 for j in range(self.stolpci)] for i in range(self.vrstice)])

    def nicelni_seznam(self):
        return [0 for j in range(self.stolpci)]

    def __mul__(self, other):
        # funkcija, za množenje matrike
        if self.stolpci != other.vrstice:
            raise Exception("POZOR! Dimenzije matrik se ne ujemajo!")
        else:
            matrikca = [[0 for j in range(self.stolpci)] for i in range(other.vrstice)]
            n = self.vrstice
            m = other.stolpci
            l = other.vrstice
            for i in range(n):
                for j in range(m):
                    for k in range(l):
                        matrikca[i][j] += self.matrika[i][k] * other.matrika[k][j]
            return Matrika(matrikca)

    def inverz_matrike(self):
        # funkcija, ki izračuna inverz matrike
        if self.stolpci != self.vrstice:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            return Matrika(np.linalg.inv(np.array(self.matrika)))

    def __len__(self):
        return len(self.matrika)

    def __round__(self):
        return round(self.matrika, 2)

    def sistem_linearnih_enacb(self, vektor):
        # sistem linearnih enačb
        if self.stolpci != len(vektor):
            raise Exception("POZOR! Dimenzije matrik se ne ujemajo!")
        elif len(vektor[0]) != 1:
            raise Exception("POZOR! Sistem enačb ima lahko ima eno rešitev!")
        else:
            mat = self.inverz_matrike().__mul__(vektor)
            sez = self.nicelni_seznam()
            for i in range(len(sez)):
                sez[i] += round(mat[i][0])
            return sez

    def dolzina_vektorjev(self):
        # pomožna funkcija, sešteje kvadrate elementov vektorja pa stolpcih
        n = self.vrstice
        m = self.stolpci
        sez = self.nicelni_seznam()
        for i in range(n):
            for j in range(m):
                for k in range(len(sez)):
                    if j == k:
                        sez[k] += (self.matrika[i][j]) ** 2
                    else:
                        pass
        return sez

    def dolzine_sestete(self):
        # pomožna funkcija, koreni dolžine
        sez = self.dolzina_vektorjev()
        for h in range(len(sez)):
            sez[h] = sez[h] ** (1 / 2)
        return sez

    def norma(self):
        # funkcija, ki normira vektorje v matriki
        sez = self.dolzine_sestete()
        n = self.vrstice
        m = self.stolpci
        matrikca = self.matrika_s_samimi_niclami()
        for j in range(m):
            for i in range(n):
                matrikca[i][j] += self.matrika[i][j] * 1 / sez[j]
        return Matrika(matrikca)

    def izracun_determinante(self):
        # funkcija, ki izračuna determinanto
        # matrika mora biti kvadratna
        if self.vrstice != self.stolpci:
            raise Exception("POZOR! Matrika ni kvadratna!")
        # če bo 1×1
        elif self.stolpci == 1:  # and self.vrstica==1
            return self.matrika[0][0]
        # če bo matrika 2×2
        elif self.stolpci == 2:
            return (
                self.matrika[0][0] * self.matrika[1][1]
                - self.matrika[0][1] * self.matrika[1][0]
            )
        # sicer
        else:
            A = self.matrika
            determinanta = 0
            indeksi = list(range(self.vrstice)) 
            for stolpci in indeksi:
                matrikca = A
                matrikca = matrikca[1:] 
                visina = len(matrikca) 
                for i in range(visina):
                    matrikca[i] = matrikca[i][0:stolpci] + matrikca[i][stolpci + 1 :] 
                predznak = (-1) ** (stolpci % 2)
                matrikca = Matrika(matrikca)
                poddeterminanta = matrikca.izracun_determinante()
                determinanta += predznak * A[0][stolpci] * poddeterminanta 
            return determinanta

    def potenciranje_matrike(self, k):
        # potenciranje
        # pogoji
        if self.vrstice != self.stolpci:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            if k == 0:
                return self.mnozi_k_poteciraj_l(1, 0)
            elif k == 1:
                return self.matrika
            elif k == 2:
                return self.matrika.__mul__(self.matrika)
            elif float(k) < 0:
                raise Exception("POZOR! K mora biti večji od 0!")
            else:
                l = float(k) - 1
                nova_matrika = self.matrika
                while l > 0:
                    matrikca = self.matrika_s_samimi_niclami()
                    n = self.vrstice
                    m = self.stolpci
                    r = self.vrstice
                    for i in range(n):
                        for j in range(m):
                            for p in range(r):
                                matrikca[i][j] += (
                                    nova_matrika[i][p] * self.matrika[p][j]
                                )
                    l -= 1
                    nova_matrika = matrikca
                return Matrika(nova_matrika)

    def obrnljivost_matrike(self):
        # pogoji
        if self.vrstice != self.stolpci:
            raise Exception("POZOR! Matrika ni kvadratna!")
        else:
            return self.izracun_determinante() != 0
