def inmating():
    NederbördLista = []
    months = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli",
     "Augusti", "September", "Oktober", "November", "December"]
    print("Var god att mata in nederbörden för följande månader.")
    for i in range(len(months)):
        print("Nederbörd för", str(months[i]), "månad?")
        Nederbörd = input("> ")
        NederbördLista.append(Nederbörd)
    return NederbördLista

def statistik(NederbördLista):
    Medelvärde = 0
    for i in range(len(NederbördLista)):
        Medelvärde += int(NederbördLista[i])
    Medelvärde /= len(NederbördLista)
    print("Medelvärde av nederbörd under året är", Medelvärde, "\nMax nederbörd är", max(NederbördLista),
          "och Min nederbörd är", min(NederbördLista), ".\n")

def main():
    import sys
    NederbördLista = []
    while True:
        print("Hejsan, välkommen till ett verktyg för att ta fram statistik av nederbörden för ett år.")
        användar_svar = input("Vill du\n\n1. Mata in nederbörd månadsvis för ett år?\n2. Se statistik för detta år?\n"
                              "3. Avsluta?")
        print("Ditt val:", användar_svar, "\n")
        if användar_svar == str(1):
            NederbördLista = inmating()
        elif användar_svar == str(2):
            if NederbördLista == []:
                print("Du måste först fylla i nederbörd för varje månad.\n")
                continue
            else:
                statistik(NederbördLista)
        elif användar_svar == str(3):
            sys.exit()
        else:
            print("Du angav ett felaktigt svar, var god försök igen.")

main()