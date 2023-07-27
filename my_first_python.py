
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

# def calculer_moyenne(nombres):
#     x = 0
#     for el in nombres:
#         x += el
#     moyenne = x / len(nombres)
#     return moyenne

# nombres = [5, 10, 15, 20, 25]
# resultat = calculer_moyenne(nombres)
# print("La moyenne est : ", resultat)

# text = "my_variable"
# print("bonjour {}".format(text))

list0 = [[1,5,4,8], ["abd", "acd", "jid"]]
copieSuperficielle = list0[:]
# copieProfonde = list0.copy()
copieProfonde = list(list0)
print("Ma copie Superficielle", copieSuperficielle)
print("=========================================")
print("Ma copie Profonde", copieProfonde)
print("=========================================")
copieSuperficielle[0][1] = 748
copieProfonde[1][1] = 70
print("Ma copie Profonde", copieProfonde)
print("=========================================")
print("ma liste d'origine ", list0)
print("=========================================")

# list1 = [1,5,4,8]
# list2 = list1[:]
# list3 = list1.copy()
# print(list2)
# print(list3)