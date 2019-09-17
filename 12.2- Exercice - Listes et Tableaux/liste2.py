# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

maximum = 0
n = 0
m = 0
for i in range(len(tab)):
    for j in range(len(tab[i])):
        if tab[i][j] > maximum:
            maximum = tab[i][j]
            n = i
            m = j
print("La valeur max est : ", maximum, "et elle se trouve à l'indice [", n, "]", "[", m, "]")

# AUTRE SOLUTION TROUVEE
#tab.index(max(tab))
#print("La valeur max est : ", max(max(tab)),"et elle se trouve à l'indice [", tab.index(max(tab)), "]", "[", max(tab).index(max(max(tab))), "]")
