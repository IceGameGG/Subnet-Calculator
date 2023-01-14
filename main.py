from math import log2


def recupIP():
    """
    Cette fonction permet de récuperer l'adresse IP que l'utilisateur saisi,
    elle verifie aussit qu'il s'agisse bien d'une adresse IP valide.

    Elle ne contient aucun paramètre.
    """
    IP = input("Quelle adresse ? ")
    adrIP = IP.split(".")
    if len(adrIP) == 4:
        for numIP in adrIP:
            try:
                int(numIP)
            except:
                print("Erreur : l'adresse rentrée n'est pas correct")
                return False
            else:
                if int(numIP) < 0 or int(numIP) > 255:
                    print("Erreur : l'adresse rentrée n'est pas correct")
                    return False
        return adrIP
    else:
        print("Erreur : l'adresse rentrée n'est pas correct")
        return False


def realNetIP(ip, masque):
    """
    Cette fonction permet de calculer l'adresse du réseaux à partir de l'adresse d'un hôte et du masque de sous réseaux.

    Elle prend donc comme paramètre ip [liste de string] et masque [liste de string]
    """
    stringBinaryIP = ""
    stringBinaryMasque = ""
    stringNewIP = ""
    newIP = []
    for cptIP in ip:
        stringBinaryIP += format(int(cptIP), 'b').zfill(8)
    for cptMasque in masque:
        stringBinaryMasque += format(int(cptMasque), 'b').zfill(8)
    for cptCalcNet in range(32):
        stringNewIP += str(int(stringBinaryIP[cptCalcNet])
                           and int(stringBinaryMasque[cptCalcNet]))
    for cptBinToList in range(4):
        newIP.append(
            str(int(stringNewIP[8*cptBinToList:8*(cptBinToList+1)], 2)))
    return newIP


def recupMasque():
    """
    Cette fonction permet de récuperer le masque que l'utilisateur saisi,
    elle verifie aussit qu'il s'agisse bien d'un masque valide.

    Elle ne contient aucun paramètre.
    """
    masque = input("Quel masque ? (format décimal pointé ou CIDR) ")
    if masque[0] == "/":
        return CIDRToMask(masque)
    adrMasque = masque.split(".")
    if len(adrMasque) == 4:
        for numMasque in adrMasque:
            try:
                int(numMasque)
            except:
                print("Erreur : le masque rentré n'est pas correct")
                return False
            else:
                if not int(numMasque) in [255, 254, 252, 248, 240, 224, 192, 128, 0]:
                    print("Erreur : le masque rentré n'est pas correct")
                    return False
        return adrMasque
    else:
        print("Erreur : le masque rentré n'est pas correct")
        return False


def CIDRToMask(masque):
    masque = masque.replace('/', '')
    try:
        int(masque)
    except:
        print("Erreur : le masque rentré n'est pas correctaa")
        return False
    else:
        if int(masque) >= 32 or int(masque) <= 0:
            print("Erreur : le masque rentré n'est pas correctaaa")
            return False
        else:
            masqueBinaire = ""
            for i in range(int(masque)):
                masqueBinaire += "1"
            for i in range(32-int(masque)):
                masqueBinaire += "0"
            masque = []
            for i in range(4):
                masque.append(str(int(masqueBinaire[8*i:8*(i+1)], 2)))
            return masque


def recupMode():
    """
    Cette fonction permet de récuperer le mode de calcul saisi par l'utilisateur,
    elle verifie qu'il s'agissent bien de l'un ou l'autre des mode

    Elle ne contient aucun paramètre.
    """
    mode = input("Définir le nombre d'hôtes (1) ou de sous-réseaux (2) ?")
    try:
        int(mode)
    except:
        print("Erreur : le mode de calcul doit être 1 ou 2")
        recupMode()
    else:
        if int(mode) == 1 or int(mode) == 2:
            return int(mode)
        else:
            print("Erreur : le mode de calcul doit être 1 ou 2")
            recupMode()


def calculNbHote(masque):
    """
    Cette fonction permet de calculer le nombre d'hôtes total du réseau.

    Elle prend donc comme paramètre masque [liste de string]
    """
    masqueBinaire = ""
    for i in masque:
        masqueBinaire += format(int(i), 'b').zfill(8)
    masqueVal = masqueBinaire.count("0")
    nbhote = 2 ** masqueVal - 2  # retire les adresses de réseau et de broadcast
    return nbhote


def recupNbHotes(nbHoteReseau):
    """
    Cette fonction permet de recuperer le nombre d'hôtes du sous-réseau.

    Elle prend donc comme paramètre nbHoteReseau [entier]
    """
    nbHote = input("Nombres d'hôtes ? ")
    try:
        int(nbHote)
    except:
        print("Erreur : le nombre d'hôtes doit être un entier")
        recupNbHotes(nbHoteReseau)
    else:
        if int(nbHote) <= nbHoteReseau:
            return int(nbHote)
        else:
            print(
                "Erreur : le nombre d'hôtes doit être inférieur ou égale au nombre d'hôtes total du réseau")
            recupNbHotes(nbHoteReseau)


def recupNbReseaux(nbHoteReseau):
    """
    Cette fonction permet de recuperer le nombre de sous-réseaux du réseau.

    Elle prend donc comme paramètre nbHoteReseau [entier]
    """
    nbReseaux = input("Nombres de réseaux ? ")
    try:
        int(nbReseaux)
    except:
        print("Erreur : le nombre de réseaux doit être un entier")
        recupNbReseaux(nbHoteReseau)
    else:
        if int(nbReseaux) <= nbHoteReseau:
            return int(nbReseaux)
        else:
            print(
                "Erreur : le nombre de réseaux doit être inférieur ou égale au nombre d'hôtes total du réseau")
            recupNbReseaux(nbHoteReseau)

#


def calcSubHotesByUser(nbMiniHotes):
    """
    Cette fonction permet de calculer le nombre d'hôtes du réseau en fonction du nombre indiqué par l'utilisateur.

    Elle prend donc comme paramètre nbMiniHotes [entier]
    """
    cpt = 0
    nbHotes = 1
    while nbHotes - 2 < nbMiniHotes:
        cpt += 1
        nbHotes = 2 ** cpt
    return nbHotes - 2


def calcSubHotesByNbReseaux(masque, nbReseaux):
    """
    Cette fonction permet de calculer le nombre d'hôtes du sous-réseau en fonction du nombre indiqué par l'utilisateur.
    Elle prend donc comme paramètre masque [liste de string] et nbReseaux [entier]
    """
    nbHotes = calculNbHote(masque) // nbReseaux - 2 + 1
    return nbHotes


def calcSubReseauxByNbHotes(masque, nbHotes):
    """
    Cette fonction permet de calculer le nombre de sous-réseaux du réseau en fonction du nombre d'hôtes indiqué par l'utilisateur.
    Elle prend donc comme paramètre masque [liste de string] et nbHotes [entier]
    """

    nbReseaux = calculNbHote(masque) // (nbHotes + 2) + 1
    return nbReseaux


def calcSubReseauxByUser(nbMiniReseaux):
    """
    Cette fonction permet de calculer le nombre de sous-réseaux du réseau en fonction du nombre d'hôtes indiqué par l'utilisateur.
    Elle prend donc comme paramètre nbMiniReseaux [entier]
    """
    cpt = 0
    nbReseaux = 1
    while nbReseaux < nbMiniReseaux:
        cpt += 1
        nbReseaux = 2 ** cpt
    return nbReseaux


def calcSubMasque(masque, nbReseau):
    """
    Cette fonction permet de calculer le nouveau masque de sous-réseaux.
    Elle prend donc comme paramètre l'ancien masque [liste de string] et nbReseaux [entier]
    """
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
    """
    Cette fonction permet de calculer la nouvelle adresse de réseau.

    Elle prend donc comme paramètre reseau [liste de string] nbHotes [entier] et numReseau [entier]
    """
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
    """
    Cette fonction permet de calculer le premier hôte du réseau.

    Elle prend donc comme paramètre reseau [liste de string]
    """
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
    """
    Cette fonction permet de calculer le dernier hôte du réseau.

    Elle prend donc comme paramètre reseau [liste de string] nbHotes [entier]
    """
    reseauBinaire = ""
    for i in reseau:
        reseauBinaire += format(int(i), 'b').zfill(8)
    lastHoteBinaire = int(reseauBinaire, 2) + nbHotes
    lastHoteBinaire = format(lastHoteBinaire, 'b').zfill(32)
    lastHote = []
    for i in range(4):
        lastHote.append(str(int(lastHoteBinaire[8*i:8*(i+1)], 2)))
    return lastHote
# Pour calculer l'adresse de broadcast, il suffit de calculer
# l'adresse suivant celle du dernier hote. La fonction calcFirstHote
# effectue déja ce calcul. On peut donc la réutiliser en utilisant
# l'adresse de dernier hote comme paramètre


def mainCalc(reseau, masque, mode, nbMini):
    """
    Cette fonction permet d'effectuer les calculs principaux et d'afficher toutes les informations de chaques réseaux
    """
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
while not reseau:  # Ceci est du au fait que si j'utilise une fonction recursive python retourne un objet NoneType un à la premiere iteration
    reseau = recupIP()
masque = recupMasque()
while not masque:
    masque = recupMasque()
realReseau = realNetIP(reseau, masque)
mode = recupMode()
if mode == 1:
    nbMini = recupNbHotes(calculNbHote(masque))
else:
    nbMini = recupNbReseaux(calculNbHote(masque))
mainCalc(realReseau, masque, mode, nbMini)
