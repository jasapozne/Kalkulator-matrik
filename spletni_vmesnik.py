import bottle
from model import Matrika
import numpy as np


def izpisana_matrika(matrika):
    matrika = matrika.split("\n")
    matrikca = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [float(x) for x in vrstica]
        matrikca.append(vrstica)
    return Matrika(matrikca)


@bottle.get("/")
def domaca_stran():
    return bottle.template("domaca_stran.html")


@bottle.get("/sestevanje")
def sestevanjem():
    return bottle.template(
        "operacijem.html", operacija="/sestej", operator="+", operiraj="Seštej"
    )


@bottle.post("/sestej")
def sestejm():

    matrika1 = bottle.request.forms["matrika1"]
    matrika2 = bottle.request.forms["matrika2"]
    matrikca1 = izpisana_matrika(matrika1)
    matrikca2 = izpisana_matrika(matrika2)
    vsota = matrikca1 + matrikca2
    return bottle.template("resitev.html", besedilo="Vsota matrik", rezultat=vsota)


@bottle.get("/odstevanje")
def odstevanjem():
    return bottle.template(
        "operacijem.html", operacija="/odstej", operator="-", operiraj="Odštej"
    )


@bottle.post("/odstej")
def odstej():
    matrika1 = bottle.request.forms["matrika1"]
    matrika2 = bottle.request.forms["matrika2"]
    matrikca1 = izpisana_matrika(matrika1)
    matrikca2 = izpisana_matrika(matrika2)
    razlika = matrikca1 - matrikca2
    return bottle.template("resitev.html", besedilo="Razlika matrik", rezultat=razlika)


@bottle.get("/mnozenje")
def mnozenje():
    return bottle.template(
        "operacijem.html", operacija="/mnozi", operator="*", operiraj="Zmnoži"
    )


@bottle.post("/mnozi")
def mnozi():
    matrika1 = bottle.request.forms["matrika1"]
    matrika2 = bottle.request.forms["matrika2"]
    matrikca1 = izpisana_matrika(matrika1)
    matrikca2 = izpisana_matrika(matrika2)
    produkt = matrikca1 * matrikca2
    return bottle.template("resitev.html", besedilo="Zmnožek matrik", rezultat=produkt)


@bottle.get("/sistem_linearnih_enacb")
def sistem_linearnih_enacb():
    return bottle.template(
        "lin_sis.html", objekt="vektor", operacija="/sistemi", izracunaj="Izračunaj"
    )


@bottle.post("/sistemi")
def sistemi():
    matrika = bottle.request.forms["matrika"]
    vektor = bottle.request.forms["vektor"]
    matrikca = izpisana_matrika(matrika)
    vektor1 = izpisana_matrika(vektor)
    resitev_lin_sistema = matrikca.sistem_linearnih_enacb(vektor1)
    return bottle.template(
        "resitev.html", besedilo="Sistem", rezultat=resitev_lin_sistema
    )


################################################################################
@bottle.get("/transponiranje")
def transponiranje():
    return bottle.template(
        "enojnematrike.html", operacija="/transponiraj", izracunaj="Transponiraj"
    )


@bottle.post("/transponiraj")
def transponiraj():
    matrika = bottle.request.forms["matrika"]
    matrikca = izpisana_matrika(matrika)
    trans = matrikca.transponiraj_matriko()
    return bottle.template("resitev.html", besedilo="Transponiranje:", rezultat=trans)


@bottle.get("/inverz")
def inverz():
    return bottle.template(
        "enojnematrike.html", operacija="/inverziraj", izracunaj="Inverziraj"
    )


@bottle.post("/inverziraj")
def inverziraj():
    matrika = bottle.request.forms["matrika"]
    matrikca = izpisana_matrika(matrika)
    inv = matrikca.inverz_matrike()
    return bottle.template("resitev.html", besedilo="Inverz:", rezultat=inv)


@bottle.get("/potenciranje")
def potenciranje():
    return bottle.template(
        "potenca.html",
        objekt="potenca",
        operacija="/potenciraj",
        izracunaj="Potenciraj",
    )


@bottle.post("/potenciraj")
def potenciraj():
    matrika = bottle.request.forms["matrika"]
    matrikca = izpisana_matrika(matrika)
    potenca = bottle.request.forms["potenca"]
    rezultat = matrikca.potenciranje_matrike(potenca)
    return bottle.template("resitev.html", besedilo="Potenciraj:", rezultat=rezultat)


@bottle.get("/normiranje")
def normiranje():
    return bottle.template(
        "enojnematrike.html", operacija="/normiraj", izracunaj="Normiraj"
    )


@bottle.post("/normiraj")
def normiraj():
    matrika = bottle.request.forms["matrika"]
    matrikca = izpisana_matrika(matrika)
    norm = matrikca.norma()
    return bottle.template("resitev.html", besedilo="Norma:", rezultat=norm)


@bottle.get("/slede")
def sledenje():
    return bottle.template("enojnematrike.html", operacija="/sled", izracunaj="Sled")


@bottle.post("/sled")
def sled():
    matrika = bottle.request.forms["matrika"]
    matrikca = izpisana_matrika(matrika)
    sled = matrikca.sled_matrike()
    return bottle.template("resitev.html", besedilo="Sled:", rezultat=sled)


@bottle.get("/determiniranje")
def determiniranje():
    return bottle.template(
        "enojnematrike.html", operacija="/determinanta", izracunaj="Determiniraj"
    )


@bottle.post("/determinanta")
def determinanta():
    matrika = bottle.request.forms["matrika"]
    matrikca = izpisana_matrika(matrika)
    det = matrikca.izracun_determinante()
    return bottle.template("resitev.html", besedilo="Determinanta:", rezultat=det)


@bottle.get("/obrnljivost_matrike")
def obrnljivost_matrike():
    return bottle.template("enojnematrike.html", operacija="/obrni", izracunaj="Obrni")


@bottle.post("/obrni")
def obrni():
    matrika = bottle.request.forms["matrika"]
    matrikca = izpisana_matrika(matrika)
    obrnljivo = matrikca.obrnljivost_matrike()
    if obrnljivo is True:
        return bottle.template(
            "resitev.html", besedilo="Operator", rezultat="Matrika je obrnljiva!"
        )
    else:
        return bottle.template(
            "resitev.html", besedilo="Operator", rezultat="Matrika ni obrnljiva!"
        )


bottle.run(reloader=True, debug=True)
