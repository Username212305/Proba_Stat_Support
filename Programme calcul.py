from math import *

print("\033c", end="")


'''
Partie Analyse fichier
'''
with open("C:\\Users\PC\Desktop\Justin\AEPFL\Proba Stat\input_values.txt", "r") as file:

    f = str(tuple(file)[0])
    values = []
    n = 0
    curvar = ""

    for i, val in enumerate(f):

        if val == " " or val == "\n":

            if i != n:
                for j in range(n,i):
                    curvar += f[j]
                values.append(float(curvar))
                curvar = ""
                n = i
                pass
            
            n = i

        elif val.isdigit() or val == "." or val == "-":
            pass

        else:
            print("Erreur de texte")

    if i != n and val.isdigit:
        for j in range(n+1,i+1):
            curvar += f[j]
        values.append(float(curvar))
        curvar = ""


'''
Partie Calculatoire
'''
result = 0



# Calcul moyenne
for v in values:
    result += v
result = result / len(values)
print("La moyenne des données est: ", result)

# Calcul écart-type
m = result
result = 0
for r in values:
    result += (r - m)**2
result = sqrt(result)/(len(values)-1)
print("L'écart-type des données est: ", result)

# Calcul médiane
values_sorted = [values[0]]
# Tri de la liste
for number in values[1::]: # Prend chacune des valeurs de la liste pour l'insérer dans la liste triée

    index = len(values_sorted) - 1

    if number >= values_sorted[index]: # Après le dernier élément
        values_sorted.append(number)

    elif number <= values_sorted[0]: # Avant le dernier élément
        values_sorted = [number] + values_sorted

    else: # Au milieu
        if index == 12:
            print()
        index = index//2
        check = True

        while check:
            if number <= values_sorted[index]:
                if number > values_sorted[index-1]:
                    values_sorted = values_sorted[0:index:] + [number] + values_sorted[index::]
                    check = False
                else:
                    index = index//2
            else:
                if number <= values_sorted[index+1]:
                    values_sorted = values_sorted[0:index+1:] + [number] + values_sorted[index+1::]
                    check = False
                else:
                    if (index-1):
                        index += index//2
                    else:
                        index += 1

med = len(values_sorted)//2
print("La médiane des données est: ", values_sorted[med])

print("Données non-triées: ", values)
print("Données triées: ", values_sorted)

# Calcul quantil
p = float(input("Calcul du quantil: entrez une valeur entre 0 et 1 "))
quan = floor(len(values_sorted)*p)
print(f"Le {p}eme quantil des données est: ", values_sorted[quan])