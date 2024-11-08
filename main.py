"""pas de module importe"""
#### Fonction secondaire


def ispalindrome(p):
    """
    Retourne True si p est un palindrome sinon retourne False
    """

    # votre code ici
    pmin = p.lower()
    pmin = pmin.replace(" ", "")
    pmin = pmin.replace("'", "")
    pmin = pmin.replace(",", "")
    pmin = pmin.replace("!", "")
    pmin = pmin.replace("?", "")
    pmin = pmin.replace(":", "")
    pmin = pmin.replace("-", "")
    accent = "éàçëêèûüùô"
    sans_accent = "eaceeeuuuo"
    trans = str.maketrans(accent, sans_accent)
    pmin = pmin.translate(trans)

    for i in range((int)(len(p)/2)):
        if pmin[i] != pmin[-(i+1)]:
            return False
    return True

#### Fonction principale


def main():
    """
    Fonction principale
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
