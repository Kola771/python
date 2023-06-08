
# print("Bonjour le monde !")
# x = 10
# y = 5
# somme = x + y
# print("La somme de ", x, " et ", y, " est : ", somme)

# for i in range(10):
#     if i == 9 :
#         break
#     elif i == 2:
#         continue
#     elif i == 4:
#         pass
#     print(i)

def calculer_moyenne(nombres):
    x = 0
    for el in nombres:
        x += el
    moyenne = x / len(nombres)
    return moyenne

nombres = [5, 10, 15, 20, 25]
resultat = calculer_moyenne(nombres)
print("La moyenne est : ", resultat)