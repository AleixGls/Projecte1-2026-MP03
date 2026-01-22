import datetime

import pymysql

# COMPLETADA
def connectToDB():
    conn = pymysql.connect(
        host='chooseyourstory-database.cbim0ycisox3.eu-north-1.rds.amazonaws.com',
        user='admin',
        password='Jefecolorado123!',
        database='mydb')
    return conn

# COMPLETADA
def saveAndCloseDB(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()
    return


# COMPLETADA
def get_answers_bystep_adventure(idAdventure):
    # Ens retornarà el diccionari idAnswers_ByStep_Adventure una vegada hàgim seleccionat una aventura.
    # Només tindrem els passos relacionats amb l'aventura que estem jugant.

    conn = connectToDB()  # Conexión a la base de datos
    cursor = conn.cursor()  # Abrimos el cursor
    cursor.execute(
        "SELECT Id_step_option, Id_step_adventure, leads_to, description FROM Step_options WHERE id_step_adventure in (SELECT id_step_adventure from Step_adventures where id_adventure = %s);",(idAdventure,))
    step_option_query = cursor.fetchall()

    options_dict = {}

    for row in step_option_query:
        options_dict[row[0]] = {
            'Id_step_adventure': row[1],
            'Leads_to': row[2],
            'Description': row[3]
        }

    saveAndCloseDB(conn, cursor)

    return options_dict


# COMPLETADA
def get_adventures_with_chars():
    # Ens retornarà el diccionari adventures, compuesto de las columnas id_adventure, name y description
    conn = connectToDB()
    cursor = conn.cursor()

    query = "SELECT * FROM Adventures"
    cursor.execute(query)

    adventures = {}
    for row in cursor.fetchall():
        adventures[row[0]] = {
            "name": row[1],
            "description": row[2]}

    saveAndCloseDB(conn, cursor)

    return adventures


# COMPLETADA
def get_id_bystep_adventure(idAdventure):
    # Ens retornarà el diccionari id_by_steps amb només els passos relacionats amb l'aventura que estem jugant.
    steps_dict = {}
    conn = connectToDB()  # Conexión a la base de datos

    cursor = conn.cursor()  # Abrimos el cursor
    cursor.execute(
        "SELECT Id_step_adventure, Description, Is_final_step FROM Step_adventures WHERE Id_adventure = %s;",(idAdventure))

    step_adventure_query = cursor.fetchall()

    for row in step_adventure_query:
        steps_dict[row[0]] = {
            'Description': row[1],
            'Is_final_step': row[2]
        }

    saveAndCloseDB(conn,cursor)
    return steps_dict


# COMPLETADA
def get_first_step_adventure(idAdventure):
    # Un cop seleccionada una aventura, aquesta funció ens serveix per trobar el primer pas d'aquesta aventura.
    conn = connectToDB()
    cursor = conn.cursor()

    init_step_adventure=cursor.execute("SELECT * FROM Step_adventures WHERE id_adventure = %s AND id_step_adventure NOT IN (SELECT Leads_to from Step_options);",(idAdventure))

    return init_step_adventure

# COMPLETADA
def get_characters():
    # Ens retorna el diccionari characters, compuesto de las columnas id_character, name y description

    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Characters")

    characters = {}
    for row in cursor.fetchall():
        characters[row[0]] = {
            "name": row[1],
            "description": row[2]}

    saveAndCloseDB(conn, cursor)

    return characters


# COMPLETADA
def getReplayAdventures():
    # Ens retorna el diccionari replayAdventures
    #idGame:{idUser': id dusuari, 'Username': 'nom del usuari', 'idAdventure': id de aventura, 'Name': 'nom de l'aventura', # 'date': data en format datetime, 'idCharacter': id del personatje, 'CharacterName': 'Nom delpersonatje'} ,
    # 1: {'idUser': 1, 'Username': 'Rafa', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo', 'date': datetime.datetime(2021, 11, 16, 19, 5, 48), 'idCharacter': 1, 'CharacterName': 'Beowulf'},
    # 2: {'idUser': 1, 'Username': 'Rafa', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
    # 'date': datetime.datetime(2021, 11, 24, 0, 0), 'idCharacter': 1, 'CharacterName': 'Beowulf'},

    conn = connectToDB()
    cursor = conn.cursor()

    replayAdventures_query=cursor.execute("SELECT g.id_game, g.id_user, u.username, g.Id_adventure, a.name, g.date, g.id_character, c.name from Games as g INNER JOIN Users u on g.id_user= u.id_user INNER JOIN Adventures a on g.id_adventure=a.id_adventure INNER JOIN Characters c on g.id_character=c.id_character")
    replayAdventures_dict={}
    for row in replayAdventures_query:
        replayAdventures_dict[row[0]] = {
            'idUser': row[1],
            'Username': row[2],
            'idAdventure': row[3],
            'Name': row[4],
            'date': row[5],
            'idCharacter': row[6],
            'CharacterName': row[7],
        }
    saveAndCloseDB(conn,cursor)
    return replayAdventures_dict

# COMPLETADA
def getChoices(idGame):
    # Tornem una tuple de tuples binàries on cada tupla binària representa un pas i la selecció
    # Per exemple, comencem l'aventura X, comencem al pas 101 i triem l'opcio 101 ( en aquest cas l'id d'opcio coincideix amb l'id de pas )
    # Aquesta elecció ens porta al pas 103, on escollim l'opció 108.
    # Aquesta elecció ens porta al pas 108 on escollim l'opció 110 i acaba l'aventura.
    # En aquest cas, si escollim reviure aquesta aventura, la funció ens tornaria:
    # ((101, 101), (103, 108), (108, 110))
    conn = connectToDB()
    cursor = conn.cursor()

    choices_query=cursor.execute("SELECT id_step_adventure, id_step_option from Game_has_choices where id_game = %s",(idGame))
    choices_list=[]
    for row in choices_query:
        choices_list.append((row[0],row[1]))
    choices_tuple=tuple(choices_list)

    return choices_tuple


# COMPLETADA
def getIdGames():
    # Ens retorna una tupla amb tots els id de game que s'han jugat, després la utilitzarem per a establir un id de joc que no existeixi en la bbdd
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute("SELECT id_game from Games")
    id_list = []
    query = cursor.fetchall()
    for id in query:
        id_list.append(id[0])
    game_list = tuple(id_list)

    saveAndCloseDB(conn,cursor)
    return game_list


# COMPLETADA
def insertCurrentGame(idGame, idUser, idChar, idAdventure):
    # Aquesta funció insereix un nou registre de “game” a la BBDD
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Games (id_game, id_user, id_character,id_adventure, date) VALUES (%s,%s,%s,%s,%s)",(idGame,idUser,idChar,idAdventure,datetime.datetime.now()))
    saveAndCloseDB(conn, cursor)
    return


# COMPLETADA
def getUsers():
    # Aquesta funció ens retorna un diccionari del tipus:
    # {
    #   'NomUsuari': {'password': 'passwordDelUsuari', 'idUser': id de l’usuari}, 
    #   'Jordi': {'password':'1234', 'idUser': 2}
    # }
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")

    users = {}
    for row in cursor.fetchall():
        users[row[1]] = {
            "passwordDelUsuari": row[2],
            "idUser": row[0]}
    saveAndCloseDB(conn, cursor)
    return users



# COMPLETADA
def getUserIds():
    # Ens retorna una llista composta de dues llistes, la primera els noms d’usuaris, la segona els id dels usuaris, exemple:
    # [
    #   ['ester23', 'Jordi', 'MarioR', 'MarioT', 'PedroG', 'Rafa12'], 
    #   [0, 2, 5, 3, 4, 1]
    # ]

    conn = connectToDB()
    cursor = conn.cursor()

    cursor.execute("SELECT username from Users")
    username_query = cursor.fetchall()
    username_list = []
    for username in username_query:
        username_list.append(username[0])

    cursor.execute("SELECT id_user from Users")
    iduser_query = cursor.fetchall()
    iduser_list = []
    for iduser in iduser_query:
        iduser_list.append(iduser[0])

    compound_list = [username_list] + [iduser_list]
    saveAndCloseDB(conn, cursor)
    return compound_list


# COMPLETADA
def insertUser(id, user, password):
    # Aquesta funció ens servirà per inserir un usuari a la BBDD un cop hàgim creat.
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Users (id_user, username, password) VALUES (%s, %s, %s)",
        (id, user, password)
    )
    saveAndCloseDB(conn, cursor)
    return

# COMPLETADA
def get_table(query):
    # Aquesta funció rebrà una query i ens retornarà el resultat de la query en una tupla de tuples.
    # La tupla 0 serà una tupla amb els noms de les columnes de la query i la resta de tuples seran les files de la query.
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute(query)
    columns = []
    for i in cursor.description:
        columns.append(i[0])

    column_names = tuple(columns)
    rows = []
    row_query=cursor.fetchall()
    for row in row_query:
        rows.append(tuple(row))

    saveAndCloseDB(conn,cursor)
    return (column_names,) + tuple(rows)

# COMPLETADA
def checkUserbdd(user, password):
    # Funció que chequea usuari i password de la BBDD, si usuari no existeix, retorna 0.
    # Si password no és correcte, retorna -1, si tot és correcte, retorna 1
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM Users WHERE username = %s",
        (user,)
    )
    row = cursor.fetchone()
    if row is None:
        saveAndCloseDB(conn, cursor)

        return 0
    elif password != row[0]:
        saveAndCloseDB(conn, cursor)

        return -1
    else:
        saveAndCloseDB(conn, cursor)

        return 1

def insertCurrentChoice(idGame,actual_id_step,id_answer):

    conn=connectToDB()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO Game_has_choices (Id_game, id_step_adventure, id_step_option) VALUES (%s,%s,%s);",(idGame,actual_id_step,id_answer))
    saveAndCloseDB(conn,cursor)
    return

# NO HECHA (no entiendo que esté esta función y otra exactamente igual, la de insertcurrentgame, esta por ahora peta)
def setIdGame():
    # Aquesta funció actualitza la bbdd amb un nou game.
    conn = connectToDB()
    cursor = conn.cursor()
    idgamelist=getIdGames()
    maxid=0
    for id in idgamelist:
        if id>maxid:
            maxid=id+1

    cursor.execute(("INSERT INTO Games (id_game) VALUES (%s)"),(maxid,))
    saveAndCloseDB(conn,cursor)

    return maxid+1

