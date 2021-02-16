#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    list=[]
    for i in range(10):
        l=input("Enter a value: ")
        list.append(l)
    return sorted(values)


def anagrams(words: list = None) -> bool:
    word1 = (input("Enter a word: "))
    worwd2 = (input("Enter a anag: "))
    if worwd2 == word1[::-1]:
        return True
    else:
        return False


def contains_doubles(items: list) -> bool:
    for i in items:
        if items.count(i)>1:
            return True
        else:
            return False
def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_grade = {}
    for names, notes in student_grades.items():
        best_grade[names] = sum(notes) / len(names)
    student_grades = {min(best_grade): best_grade[min(best_grade)] for key in student_grades}
    return student_grades


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    sentence_d = sentence.replace(' ', '')
    lettre_n_use = {}
    for letters in sentence_d:
        if sentence_d.count(letters) > 5:
            lettre_n_use[letters] = sentence_d.count(letters)
        #       Retourner le tableau de lettres
    a = dict(sorted(lettre_n_use.items(), key=lambda item: item[1], reverse=True))
    for i in a:
        return (i,a[i])


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
