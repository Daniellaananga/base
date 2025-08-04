fruits = ["banana", "orange", "mango", "powpow", "pineapple", "sugarcane"]
valeur = fruits.pop() # supprimmer le dernier element de la liste
fruits.insert(1, "pear") # insere un element a la position 2
fruits.remove("orange") # retire l'element orange

for fruit in fruits:
    print(fruit.upper())