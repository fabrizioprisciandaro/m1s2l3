print("Benvenuto su BandCreator. Vuoi creare il nome della tua band?")

answer = input ("Digita SI per continuare: ")

if answer == "SI":
    print("Ottimo!")

    cittaOrigine = input ("Inserisci la tua città di origine: ")

    animaleDomestico = input ("Inserisci il nome del tuo animale domestico: ")


    nomeBand = cittaOrigine + animaleDomestico
    print("Hai ottenuto questo nome per la tua band: ", nomeBand)

else :
    print("OK! Alla prossima!")

