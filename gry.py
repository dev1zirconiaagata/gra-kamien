import random
opcie = ["papier","kamień","nozyce"]
# milej gry
while True:
    gracz = input("wybierz kamień papier lub nożyce (albo napisz koniec)")

    if gracz == "koniec":
        print("dobra gra")
        break
    komputer = random.choice(opcie)
    print("komputer wybrał:", komputer)
    
    if gracz == komputer:
        print("remis")
    elif (gracz == "kamien" and komputer == "nozyce") or \
            (gracz == "papier" and komputer == "kamien") or \
            (gracz == "nozyce" and komputer == "papier"):
        print("wygrałeś!🎉")
    else:
        print("komputer wygrał!🤖")

    
    
     
