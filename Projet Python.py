"""Nombre de chasse à payer."""
# auteur : Mohamed Faye

# fonctions
def autorisationChas(p, c, b, a):
    bilans_perdus = p + 3*c +   5*b + 10*a
    nbre_autorisation = bilans_perdus/10.00
    return 200*nbre_autorisation
   
# programme principal -----------------------------------------------
while True:
    try:
           pigeon = int(input("=== Combien de pigeon ? ===    "))
    except ValueError:
            print("vous n'avez pas fourni de nbr")
    else:
            break       

while True:
             try:
                    chat = int(input("=== Combien de chat ? ===    "))
             except ValueError:
                    print("vous n'avez pas fourni de nbr")
             else:
                    break

while True:
            try:
                    boeuf = int(input("=== Combien de boeuf ? ===    "))
            except ValueError:
                    print("vous n'avez pas fourni de nbr")
            else:

                   break

while True:
            try:        
                    ane =int(input("=== Combien d'ane ? ===    "))
            except ValueError:
                    print("vous n'avez pas fourni de nbr")
            else:
                    break
print("================================================================")

payer = autorisationChas(pigeon, chat, boeuf, ane)
print("\nA payer :", end=" ")
print("rien a payer") if payer == 0 else print(payer, "euros")


