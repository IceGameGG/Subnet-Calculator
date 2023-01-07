#----------------MODULES-----------------
from math import log2
#Vérification des valeurs
#Adresse
def recupIP():
    IP = input("Quelle adresse ? ")
    adrIP = IP.split(".")
    if len(adrIP) == 4:
        for numIP in adrIP:
            if numIP.isdigit:
                if int(numIP) >= 0 and int(numIP) <= 255:
                    return adrIP
                else:
                    print("Erreur : l'adresse rentrée n'est pas correct")
                    return False
            else:
                print("Erreur : l'adresse rentrée n'est pas correct")
                return False
    else:
        print("Erreur : l'adresse rentrée n'est pas correct")
        return False

def realNetIP(ip, masque):
    stringBinaryIP = ""
    stringBinaryMasque = ""
    stringNewIP=""
    newIP=[]
    for cptIP in ip:
        stringBinaryIP += format(int(cptIP), 'b').zfill(8)
    for cptMasque in masque:
        stringBinaryMasque += format(int(cptMasque), 'b').zfill(8)
    for cptCalcNet in range(32):
        stringNewIP += str(int(stringBinaryIP[cptCalcNet]) and int(stringBinaryMasque[cptCalcNet]))
    for cptBinToList in range(4):
        newIP.append(str(int(stringNewIP[8*cptBinToList:8*(cptBinToList+1)], 2)))
    return newIP

#Masque
def recupMasque():
    masque = input("Quel masque ? ")
    adrMasque = masque.split(".")
    if len(adrMasque) == 4:
        for numMasque in adrMasque:
            if numMasque.isdigit():
                if int(numMasque) in [0, 128, 192, 224, 240, 248, 252, 254, 255]:
                    return adrMasque
                else:
                    print("Erreur : le masque rentré n'est pas correct")
                    return False
            else:
                print("Erreur : le masque rentré n'est pas correct")
                return False
    else:
        print("Erreur : le masque rentré n'est pas correct")
        return False
#Mode de fonctionnement
def recupMode():
    mode = input("Définir le nombre d'hôtes (1) ou de sous-réseaux (2) ?")
    if mode.isdigit():
        if int(mode) == 1 or int(mode) == 2:
            return int(mode)
        else:
            print("Erreur : le mode de calcul doit être 1 ou 2")
            recupMode()
    else:
        print("Erreur : le mode de calcul doit être 1 ou 2")
        recupMode()
#Nombre d'hôtes
#Calcul du nombre d'hôte total du réseau
def calculNbHote(masque):
    masqueBinaire = ""
    for i in masque:
        masqueBinaire += format(int(i), 'b').zfill(8)
    masqueVal = masqueBinaire.count("0")
    nbhote = 2 ** masqueVal - 2 # retire les adresses de réseau et de broadcast
    return nbhote
def recupNbHotes(nbHoteReseau):
    nbHote = input("Nombres d'hôtes ? ")
    if nbHote.isdigit():
        if int(nbHote) <= nbHoteReseau:
            return int(nbHote)
        else:
            print("Erreur : le nombre d'hôtes doit être inférieur ou égale au nombre d'hôtes total du réseau")
            recupNbHotes(nbHoteReseau)
    else:
        print("Erreur : Le nombre d'hôtes doit être un entier")
        recupNbHotes(nbHoteReseau)
def recupNbReseaux(nbHoteReseau):
    nbReseaux = input("Nombres de réseaux ? ")
    if nbReseaux.isdigit():
        if int(nbReseaux) <= nbHoteReseau:
            return int(nbReseaux)
        else:
            print("Erreur : le nombre de réseaux doit être inférieur ou égale au nombre d'hôtes total du réseau")
            recupNbReseaux(nbHoteReseau)
    else:
        print("Erreur : Le nombre de réseaux doit être un entier")
        recupNbReseaux(nbHoteReseau)
#Calcul des reseaux
def calcSubHotesByUser(nbMiniHotes):
    cpt = 0
    nbHotes = 1
    while nbHotes - 2 < nbMiniHotes:
        cpt += 1
        nbHotes = 2 ** cpt
    return nbHotes - 2
def calcSubHotesByNbReseaux(masque, nbReseaux):
    nbHotes = calculNbHote(masque) // nbReseaux - 2 + 1
    return nbHotes

def calcSubReseauxByNbHotes(masque, nbHotes):
    nbReseaux = calculNbHote(masque) // (nbHotes + 2) + 1
    return nbReseaux
def calcSubReseauxByUser(nbMiniReseaux):
    cpt = 0
    nbReseaux = 1
    while nbReseaux < nbMiniReseaux:
        cpt += 1
        nbReseaux = 2 ** cpt
    return nbReseaux


def calcSubMasque(masque, nbReseau):
    masqueBinaire = ""
    for i in masque:
        masqueBinaire += format(int(i), 'b').zfill(8)
    nbBitReseau = masqueBinaire.count("1")
    nbBitReseau += int(log2(nbReseau))
    masqueBinaire = ""
    for i in range(nbBitReseau):
        masqueBinaire += "1"
    for i in range(32 - nbBitReseau):
        masqueBinaire += "0"
    subMasque = []
    for i in range(4):
        subMasque.append(str(int(masqueBinaire[8*i:8*(i+1)], 2)))
    return subMasque, nbBitReseau

def calcSubReseauIp(reseau, nbHotes, numReseau):
    reseauBinaire = ""
    for i in reseau:
        reseauBinaire += format(int(i), 'b').zfill(8)
    subReseauBinaire = int(reseauBinaire, 2) + ((nbHotes + 2) * numReseau)
    subReseauBinaire = format(subReseauBinaire, 'b').zfill(32)
    subReseau = []
    for i in range(4):
        subReseau.append(str(int(subReseauBinaire[8*i:8*(i+1)], 2)))
    return subReseau
def calcFirstHote(reseau):
    reseauBinaire = ""
    for i in reseau:
        reseauBinaire += format(int(i), 'b').zfill(8)
    firstHoteBinaire = int(reseauBinaire, 2) + 1
    firstHoteBinaire = format(firstHoteBinaire, 'b').zfill(32)
    firstHote = []
    for i in range(4):
        firstHote.append(str(int(firstHoteBinaire[8*i:8*(i+1)], 2)))
    return firstHote
def calcLastHote(reseau, nbHotes):
    reseauBinaire = ""
    for i in reseau:
        reseauBinaire += format(int(i), 'b').zfill(8)
    lastHoteBinaire = int(reseauBinaire, 2) + nbHotes
    lastHoteBinaire = format(lastHoteBinaire, 'b').zfill(32)
    lastHote = []
    for i in range(4):
        lastHote.append(str(int(lastHoteBinaire[8*i:8*(i+1)], 2)))
    return lastHote
#Pour calculer l'adresse de broadcast, il suffit de calculer
#l'adresse suivant celle du dernier hote. La fonction calcFirstHote
#effectue déja ce calcul. On peut donc la réutiliser en utilisant 
#l'adresse de dernier hote comme paramètre

def mainCalc(reseau, masque, mode, nbMini):
    print("")
    if mode == 1:
        nbHotes = calcSubHotesByUser(nbMini)
        nbReseaux = calcSubReseauxByNbHotes(masque, nbHotes)
        
    else:
        nbReseaux = calcSubReseauxByUser(nbMini)
        nbHotes = calcSubHotesByNbReseaux(masque, nbReseaux)
    subMasque, subMasqueBits = calcSubMasque(masque, nbReseaux)
    print(f"Nouveaux masque réseau : {'.'.join(subMasque)} (/{subMasqueBits})")
    print(f"Nombre de sous-réseaux : {nbReseaux}")
    for i in range(nbReseaux):
        subReseau = calcSubReseauIp(reseau, nbHotes, i)
        firstHote = calcFirstHote(subReseau)
        lastHote = calcLastHote(subReseau, nbHotes)
        broadcast = calcFirstHote(lastHote)
        print(f"Réseaux {i + 1} : ")
        print(f"Masque réseau : {'.'.join(subMasque)}")
        print(f"Adresse du réseau : {'.'.join(subReseau)}")
        print(f"Adresse du premier hôte : {'.'.join(firstHote)}")
        print(f"Adresse du dernier hôte : {'.'.join(lastHote)}")
        print(f"Adresse de diffusion : {'.'.join(broadcast)}")
        print(f"Nombres maximal d'hôtes : {nbHotes}", end="\n \n")
        


    


reseau = recupIP()
while not reseau: #Ceci est du au fait que si j'utilise une fonction recursive python retourne un objet NoneType un à la premiere iteration
    reseau = recupIP()

masque = recupMasque()
while not masque:
    masque = recupMasque()
realReseau = realNetIP(reseau, masque)
mode = recupMode()
if mode == 1 :
    nbMini = recupNbHotes(calculNbHote(masque))
else:
    nbMini = recupNbReseaux(calculNbHote(masque))
mainCalc(realReseau, masque, mode, nbMini)


    






