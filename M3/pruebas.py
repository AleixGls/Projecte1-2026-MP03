tuple_of_keys = ("Username", "Name", "CharacterName", "date")
weigth_of_columns = (20, 30, 20, 20)
dict_of_data = {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
                    'date': (2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName': 'Beowulf'},
                5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
                    'date': (2021, 11, 26, 13, 28, 36), 'idCharacter': 1, 'CharacterName': 'Beowulf'}}
def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    # A aquesta funció li passem com a paràmetres, un diccionari del tipus {id: {diccionari amb dades}}
    # Una tupla amb les keys que ens interessa.
    # Una tupla amb les grandàries de cada columna.
    # I ens retorna un string que imprès té forma de taula, amb les dades corresponents a les keys que passem i formatades amb les grandàries donades

    pass
    cabecera="|"+"id".center(6)+"|"
    datos=""
    for key in range(0, len(tuple_of_keys)):
        cabecera+=tuple_of_keys[key].center(weigth_of_columns[key])+"|"

    for dicto in dict_of_data:
        datos+="\n"+"|"+str(dicto).center(6)+"|"
        for key in range(0, len(tuple_of_keys)):
            if tuple_of_keys[key] in dict_of_data[dicto]:
                datos+=str(dict_of_data[dicto][tuple_of_keys[key]]).center(weigth_of_columns[key])+"|"

    print(cabecera+datos)


getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data)