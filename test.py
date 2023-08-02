def main():
    # recolter une premiere note
    note1 = int(input("Entrer la première note"))

    # recolter une deuxième note
    note2 = int(input("Entrer la seconde note"))

    # recolter une trosième note
    note3 = int(input("Entrer la dernière note"))

    # calculer la moyenne
    result = (note1 + note2 + note3) / 3

    # afficher le resultat
    print("La moyenne est de " + str(result))


if __name__ == '__main__':
    main()