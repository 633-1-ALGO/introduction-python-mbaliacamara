# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

occ = texte.count("exemple")
print("Il y a ", occ, " fois le mot 'exemple'")
print(texte.replace("est","représente"))

