nota = 50
presenca = 50

if nota < 70 or presenca < 70:
    print ("Você reprovou.")

    if nota < 70:
        print ("Tente melhorar sua nota para o ano que vem.")
    if presenca < 70:
        print ("Você deve frequentar as aulas.")
else:
    print ("Você passou!")

    if nota == 100 and presenca == 100:
        print ("Aprovado com louvor.")


