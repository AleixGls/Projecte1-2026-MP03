# HACER
def get_answers_bystep_adventure():
    # Ens retornarà el diccionari idAnswers_ByStep_Adventure una vegada hàgim seleccionat una aventura.
    # Només tindrem els passos relacionats amb l'aventura que estem jugant.
    pass

# HACER
def get_adventures_with_chars():
    # Ens retornarà el diccionari adventures
    pass

# HACER
def get_id_bystep_adventure():
    # Ens retornarà el diccionari id_by_steps amb només els passos relacionats amb l'aventura que estem jugant.
    pass

# HACER
def get_first_step_adventure():
    # Un cop seleccionada una aventura, aquesta funció ens serveix per trobar el primer pas d'aquesta aventura.
    pass

# HACER
def get_characters():
    # Ens retorna el diccionari characters
    pass

# HACER
def getReplayAdventures():
    # Ens retorna el diccionari replayAdventures
    pass

# HACER
def getChoices():
    # Tornem una tuple de tuples binàries on cada tupla binària representa un pas i la selecció
    # Per exemple, comencem l'aventura X, comencem al pas 101 i triem l'opcio 101 ( en aquest cas l'id d'opcio coincideix amb l'id de pas )
    # Aquesta elecció ens porta al pas 103, on escollim l'opció 108.
    # Aquesta elecció ens porta al pas 108 on escollim l'opció 110 i acaba l'aventura.
    # En aquest cas, si escollim reviure aquesta aventura, la funció ens tornaria:
    # ((101, 101), (103, 108), (108, 110))
    pass

# HACER
def getIdGames():
    # Ens retorna una tupla amb tots els id de game que s'han jugat, després la utilitzarem per a establir un id de joc que no existeixi en la bbdd
    pass

# HACER
def insertCurrentGame(idGame,idUser,isChar,idAdventure):
    # Aquesta funció insereix un nou registre de “game” a la BBDD
    pass

# HACER
def getUsers():
    # Aquesta funció ens retorna un diccionari del tipus:
    # {
    #   'NomUsuari': {'password': 'passwordDelUsuari', 'idUser': id de l’usuari}, 
    #   'Jordi': {'password':'1234', 'idUser': 2}
    # }
    pass

# HACER
def getUserIds():
    # Ens retorna una llista composta de dues llistes, la primera els noms d’usuaris, la segona els id dels usuaris, exemple:
    # [
    #   ['ester23', 'Jordi', 'MarioR', 'MarioT', 'PedroG', 'Rafa12'], 
    #   [0, 2, 5, 3, 4, 1]
    # ]
    pass

# HACER
def insertUser(id, user,password):
    # Aquesta funció ens servirà per inserir un usuari a la BBDD un cop hàgim creat.
    pass

# HACER
def get_table(query):
    # Aquesta funció rebrà una query i ens retornarà el resultat de la query en una tupla de tuples.
    # La tupla 0 serà una tupla amb els noms de les columnes de la query i la resta de tuples seran les files de la query.
    pass

# HACER
def checkUserbdd(user,password):
    # Funció que chequea usuari i password de la BBDD, si usuari no existeix, retorna 0.
    # Si password no és correcte, retorna -1, si tot és correcte, retorna 1
    pass

# HACER
def setIdGame():
    # Aquesta funció actualitza la bbdd amb un nou game.
    pass