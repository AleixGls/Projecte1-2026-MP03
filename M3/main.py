# main.py
import BBDD
import Auxiliars

# ============================================
# 1. VARIABLES GLOBALES Y CONTEXTO
# ============================================
game_context = {
    # User
    'idUser': None,
    'username': None,
    # Adventure
    'idAdventure': None,
    'adventureName': None,
    # Character
    'idChar': None,
    'characterName': None,
    # Game 
    'idGame': None
}

# ============================================
# 2. FUNCIONES PRINCIPALES DEL FLUJO
# ============================================

# COMPLETADA
def login_user():
    """Función para login de usuario existente"""
    print(Auxiliars.getHeader("LOGIN"))
    
    while True:
        user = input("Usuario: ")
        user=str(user)
        password = input("Contraseña: ")
        password=str(password)
        a="a"
        
        check_result = BBDD.checkUserbdd(user, password)
        
        if check_result == 0:
            print("Usuario no existe.")
            return None
        
        elif check_result == -1:
            print("Contraseña incorrecta.")
            return None
        
        elif check_result == 1:
            users = BBDD.getUsers()
            if user in users:
                game_context['idUser'] = users[user]['idUser']
                game_context['username'] = user
                print("¡Bienvenido, {}!".format(user))
                return True
        return False

# COMPLETADA
def logout():
    game_context['idUser'] = None
    game_context['username'] = None
    print("Sesión cerrada correctamente.")

# COMPLETADA
def create_user():
    print(Auxiliars.getHeader("CREAR NUEVO USUARIO"))
    
    while True:
        user = input("Nuevo usuario (6-10 chars alfanuméricos): ")
        if user==0:
            break
        
        if not Auxiliars.checkUser(user):
            continue
            
        if Auxiliars.userExists(user):
            print("El usuario ya existe. Prueba otro.")
            continue
            
        password = input("Contraseña (8-12 chars, mayúsc, minúsc, número, especial): ")
        
        if not Auxiliars.checkPassword(password):
            continue
            
        # Obtener nuevo ID
        user_ids = BBDD.getUserIds()
        if user_ids and len(user_ids) > 1:
            new_id = max(user_ids[1]) + 1
        else:
            new_id = 1
            
        BBDD.insertUser(new_id,user,password)
        print("Usuario creado correctamente. Ahora puedes hacer login.")
        print("Enter to continue: ")
        return True


# COMPLETADA
def select_adventure():
    adventures = BBDD.get_adventures_with_chars()
    
    if not adventures:
        print("No hay aventuras disponibles.")
        return None
    

    print(Auxiliars.getHeadeForTableFromTuples(("Id Aventura","Aventura","Descripcion"), (25,40,40),"Aventuras"))
    for i in adventures:
        print(Auxiliars.getFormatedBodyColumns((str(i)+")",adventures[i]["name"],adventures[i]["description"]),(25,40,40),0))
    
    aventura = Auxiliars.getOpt("0) Para salir","Elige una aventura: ",[],adventures,[0])
    
    if aventura != 0:
        game_context["idAdventure"] = aventura
        game_context["adventureName"] = adventures[aventura]["name"]
    else:
        game_context["idAdventure"] = None
        game_context["adventureName"] = None


# COMPLETADA
def select_character():
    characters = BBDD.get_characters()
    
    if not characters:
        print("No hay personajes disponibles.")
        return None
    
    print(Auxiliars.getHeadeForTableFromTuples(("Id Personaje","Personaje","Descripcion"), (25,40,40),"Personajes"))
    for i in characters:
        print(Auxiliars.getFormatedBodyColumns((str(i)+")",characters[i]["name"],characters[i]["description"]),(25,40,40),0))

    personaje = Auxiliars.getOpt("0) Para salir","Elige un personaje: ",[],characters,[0])
    
    if personaje != 0:
        game_context["idChar"] = personaje
        game_context["characterName"] = characters[personaje]["name"]
    else:
        game_context["idChar"] = None
        game_context["characterName"] = None

# REVISAR
def play_adventure():
    # checa que el context esté completo
    if not game_context['idAdventure']:
        print("Error: No hay aventura seleccionada.")
        return
    if not game_context['idChar']:
        print("Error: No hay personaje seleccionado.")
        return

    # nuevo id de juego y lo mete en el context
    game_ids = BBDD.getIdGames()
    maxid = 0
    for id in game_ids:
        if id >= maxid:
            maxid = id+1
    game_context['idGame'] = maxid
    # inserta en la bd el nuevov juego
    BBDD.insertCurrentGame(
        maxid,
        game_context['idUser'],
        game_context['idChar'],
        game_context['idAdventure'],
    )
    
    # coge los steps y las opciones
    steps = BBDD.get_id_bystep_adventure(game_context['idAdventure'])
    options = BBDD.get_answers_bystep_adventure(game_context['idAdventure'])
    
    # coge la primera step
    current_step_number = BBDD.get_first_step_adventure(game_context['idAdventure'])
    
    print(Auxiliars.getHeader("Starting adventure... | {}".format(game_context['adventureName'])))
    print("Personaje: {}".format(game_context['characterName']))

    # el juego en sí
    flag_exit=False
    step_data = steps[current_step_number]
    while not flag_exit:

        
        # Mostrar descripción del step
        print("\n" + "".center(105,"=")) # cambia a center
        print(Auxiliars.formatText(step_data['Description'], 100))
        print("".center(105,"="))

        
        step_adventure_options = {}
        for opt_id in options.keys():
            opt_data= options[opt_id]
            if opt_data["Id_step_adventure"] == current_step_number:
                step_adventure_options[opt_id] = opt_data
        

        if step_adventure_options=={}:
            print(current_step_number)
            print("No hay opciones disponibles. Fin de la aventura.")
            input()
            break
        # Mostrar opciones
        formattedAnswersList=[]
        formattedAnswers=""
        print("\nOpciones disponibles:")
        for opt_id in step_adventure_options.keys():
            opt_data=step_adventure_options[opt_id]
            formattedAnswersList.append(opt_id)
            formattedAnswers += "\n"+Auxiliars.getFormatedAnswers(opt_id,opt_data['Description'],80,5)

        choice=Auxiliars.getOpt(formattedAnswers,"\nElige una opción (número): ",formattedAnswersList)

        #elige opcion
        flag_exit_option=False
        while not flag_exit_option and step_adventure_options!={}:
            if not str(choice).isnumeric():
                choice = input("\nIntroduce una opción válida: ")
                continue
            choice=int(choice)
            if choice not in step_adventure_options.keys():
                input("\nIntroduce una opción válida: ")
                continue
            else:
                BBDD.insertCurrentChoice(maxid, current_step_number, choice)

                current_step_number = step_adventure_options[choice]['Leads_to']
                flag_exit_option=True
        step_data = steps[current_step_number]
        # verif si es final_Step
        if step_data['Is_final_step']==1:
            print("\n" + "".center(105,"*") )
            print("FIN DE LA AVENTURA: ".center(105)+"\n"+Auxiliars.formatText(step_data['Description'], 100))
            print("*" * 105)
            input()
            flag_exit = True


    # fin juego


#TODO
def replay_adventure():
    replay_data = BBDD.getReplayAdventures()
    
    if not replay_data:
        print("No hay partidas guardadas para rejugar.")
        return
    
    # Mostrar partidas disponibles
    print(Auxiliars.getHeader("PARTIDAS GUARDADAS"))
    
    # Formatear como tabla
    table_data = {}
    for game_id, game_data in replay_data.items():
        table_data[game_id] = game_data
    
    formatted = Auxiliars.getTableFromDict(
        ("Username", "Name", "CharacterName", "date"),
        (20, 30, 20, 30),
        table_data
    )
    print(formatted)
    
    # Seleccionar partida
    while True:
        try:
            game_choice = int(input("\nSelecciona el ID de la partida a rejugar (0 para cancelar): "))
            if game_choice == 0:
                return
            elif game_choice in replay_data:
                # Obtener decisiones de esa partida
                choices = BBDD.getChoices(game_choice)
                if choices:
                    # Implementar replay (mostrar sin interactuar)
                    print("\nIniciando replay... (presiona Enter para avanzar)")
                    input("Presiona Enter para comenzar...")
                    
                    for step_id, choice_id in choices:
                        # Aquí mostrarías cada paso y elección
                        print("\nPaso: {}".format(step_id))
                        print("Elección: {}".format(choice_id))
                        input("Presiona Enter para continuar...")
                    
                    print("\nReplay completado.")
                else:
                    print("No hay datos de decisiones para esta partida.")
                break
            else:
                print("ID de partida no válido.")
        except ValueError:
            print("Por favor, introduce un número.")

# Funciones para los informes

def report_most_used_answer():
    """Informe 1: Respuesta más usada por paso de cada aventura"""
    query = """
        SELECT 
            CONCAT(a.id_adventure, ' - ', a.name) as 'ID AVENTURA - NOMBRE',
            CONCAT(sa.id_step_adventure, ' - ', sa.description) as 'ID PASO - DESCRIPCIÓN',
            CONCAT(so.id_step_option, ' - ', so.description) as 'ID RESPUESTA - DESCRIPCIÓN',
            COUNT(*) as 'VECES SELECCIONADA'
        FROM Game_has_choices ghc
        INNER JOIN Games g ON ghc.id_game = g.id_game
        INNER JOIN Step_adventures sa ON ghc.id_step_adventure = sa.id_step_adventure
        INNER JOIN Adventures a ON sa.id_adventure = a.id_adventure
        INNER JOIN Step_options so ON ghc.id_step_option = so.id_step_option
        GROUP BY a.id_adventure, sa.id_step_adventure, so.id_step_option, 
                 a.name, sa.description, so.description
        ORDER BY a.id_adventure, COUNT(*) DESC
    """
    result = BBDD.get_table(query)
    print(Auxiliars.getFormatedTable(result, "RESPUESTA MÁS USADA"))

def report_player_most_games():
    """Informe 2: Jugador con más partidas jugadas"""
    query = """
        SELECT 
            u.username as 'NOMBRE USUARIO',
            COUNT(g.id_game) as 'PARTIDAS JUGADAS'
        FROM Users u
        INNER JOIN Games g ON u.id_user = g.id_user
        GROUP BY u.id_user
        ORDER BY COUNT(g.id_game) DESC, MIN(g.date) ASC
        LIMIT 1
    """
    result = BBDD.get_table(query)
    print(Auxiliars.getFormatedTable(result, "JUGADOR CON MÁS PARTIDAS"))

def report_user_adventures():
    """Informe 3: Aventuras jugadas por un usuario específico"""
    username = input("\nIntroduce el nombre de usuario: ")
    
    # Primero verificamos si el usuario existe
    users = BBDD.getUsers()
    if username not in users:
        print(f"El usuario '{username}' no existe.")
        return
    
    query = """
        SELECT 
            a.id_adventure as 'ID',
            a.name as 'NOMBRE AVENTURA',
            DATE_FORMAT(g.date, '%%Y-%%m-%%d %%H:%%i:%%s') as 'FECHA'
        FROM Games g
        INNER JOIN Adventures a ON g.id_adventure = a.id_adventure
        INNER JOIN Users u ON g.id_user = u.id_user
        WHERE u.username = %s
        ORDER BY g.date DESC
    """
    result = BBDD.get_table(query, (username,))
    
    if len(result) > 1:  # Si hay resultados además de los nombres de columnas
        print(Auxiliars.getFormatedTable(result, f"AVENTURAS DE {username}"))
    else:
        print(f"\nEl usuario '{username}' no ha jugado ninguna aventura.")

#TODO
def show_reports():
    flag_menu = True
    while flag_menu:
        print(Auxiliars.getHeader("INFORMES"))
        
        opt = Auxiliars.getOpt(
            "1) Respuesta más usada\n2) Jugador con más partidas jugadas\n3) Aventuras jugadas por usuario\n4) Volver al menú principal\n",
            "\nElige una opción: ",
            [1,2,3,4],{},[]
        )
        
        if opt == 1:
            print("\n" + "="*120)
            print("INFORME 1: RESPUESTA MÁS USADA".center(120))
            print("="*120)
            report_most_used_answer()
            input("\nPresiona Enter para continuar...")
            
        elif opt == 2:
            print("\n" + "="*120)
            print("INFORME 2: JUGADOR CON MÁS PARTIDAS".center(120))
            print("="*120)
            report_player_most_games()
            input("\nPresiona Enter para continuar...")
            
        elif opt == 3:
            print("\n" + "="*120)
            print("INFORME 3: AVENTURAS POR USUARIO".center(120))
            print("="*120)
            report_user_adventures()
            input("\nPresiona Enter para continuar...")
            
        elif opt == 4:
            flag_menu = False


# ============================================
# 3. MENÚ PRINCIPAL
# ============================================

#TODO
def main_menu():
    """Menú principal del juego"""
    flag_menu = True
    while flag_menu:
        print(Auxiliars.getHeader("CHOOSE YOUR STORY"))
        
        if game_context['username']:
            print("Usuario: {}".format(game_context['idUser']))
            print("Nombre usuario: {}".format(game_context['username']))

        # ADVENTURE
        if game_context["idAdventure"]:
            print("Aventura: {}".format(game_context['idAdventure']))
        if game_context["adventureName"]:
            print("Nombre Aventura: {}".format(game_context['adventureName']))

        # CHARACTER
        if game_context["idChar"]:
            print("Personaje: {}".format(game_context['idChar']))
        if game_context["characterName"]:
            print("Nombre personaje: {}".format(game_context['characterName']))
        # User loggeado
        user_logged_in = game_context["idUser"] and game_context['username']
        
        # Menu no logeado
        if not user_logged_in:
            choice = Auxiliars.getOpt(
                textOpts="1) Login\n2) Crear nuevo usuario\n3) Rejugar aventura\n4) Ver informes\n5) Salir\n",
                inputOptText="\nElige una opción: ",
                rangeList=[1, 2, 3, 4, 5]
            )

            # Login en usuario
            if choice == 1:
                login_user()

                user_logged_in = game_context["idUser"] and game_context['username']

                if user_logged_in:
                    select_adventure()
                    select_character()
                    play_adventure()

            # Crear usuario
            elif choice == 2:
                create_user()
            
            # Replay
            elif choice == 3:
                replay_adventure()
            
            # Reports
            elif choice == 4:
                show_reports()
            
            # Salir
            elif choice == 5:
                print("\n¡Gracias por jugar a Choose your Story!")
                flag_menu = False

        # Menu logged
        else:
            choice = Auxiliars.getOpt(
                textOpts="1) Logout\n2) Jugar\n3) Rejugar aventura\n4) Ver informes\n5) Salir\n",
                inputOptText="\nElige una opción: ",
                rangeList=[1, 2, 3, 4, 5]
            )

            # Logout del usuario
            if choice == 1:
                logout()

            # Jugar
            elif choice == 2:
                play_adventure()
            
            # Replay
            elif choice == 3:
                replay_adventure()
            
            # Reports
            elif choice == 4:
                show_reports()
            
            # Salir
            elif choice == 5:
                print("\n¡Gracias por jugar a Choose your Story!")
                flag_menu = False
        
# ============================================
# 4. INICIO DEL PROGRAMA
# ============================================

if __name__ == "__main__":
    try:
        # Test de conexión a BD
        conn = BBDD.connectToDB()
        if conn:
            print("Conexión a base de datos establecida correctamente.")
            conn.close()
        else:
            print("Error: No se pudo conectar a la base de datos.")
            exit()
    except Exception as e:
        print("Error de conexión: {}".format(e))
        exit()
    
    # Iniciar menú principal
    main_menu()