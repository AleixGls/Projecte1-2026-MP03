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

# REVISAR
def login_user():
    """Función para login de usuario existente"""
    print(Auxiliars.getHeader("LOGIN"))
    
    while True:
        user = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()
        
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

# REVISAR
def logout():
    game_context['idUser'] = None
    game_context['username'] = None
    print("Sesión cerrada correctamente.")

#TODO
def create_user():
    print(Auxiliars.getHeader("CREAR NUEVO USUARIO"))
    
    while True:
        user = input("Nuevo usuario (6-10 chars alfanuméricos): ")
        
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
    
    aventura = Auxiliars.getOpt("0) Para salir","Elige un personaje: ",[],adventures,[0])
    
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

#TODO
def play_adventure():
    """Jugar una aventura completa"""
    if not game_context['idAdventure']:
        print("Primero selecciona una aventura.")
        return
    
    # Crear nuevo juego en BD
    game_ids = BBDD.getIdGames()
    new_game_id = max(game_ids) + 1 if game_ids else 1
    game_context['idGame'] = new_game_id
    
    # Insertar registro del juego
    BBDD.insertCurrentGame(
        new_game_id,
        game_context['idUser'],
        game_context['idChar'],
        game_context['idAdventure']
    )
    
    # Obtener datos de la aventura
    steps = BBDD.get_id_bystep_adventure(game_context['idAdventure'])
    options = BBDD.get_answers_bystep_adventure(game_context['idAdventure'])
    
    # Encontrar primer paso
    first_step = BBDD.get_first_step_adventure(game_context['idAdventure'])
    current_step = first_step
    
    print(Auxiliars.getHeader("COMIENZA LA AVENTURA: {}".format(game_context['adventureName'])))
    print("Personaje: {}".format(game_context['characterName']))
    print("-" * 105)
    
    # Bucle principal del juego
    flag_exit=False
    while not flag_exit:
        step_data = current_step
        
        # Mostrar descripción del paso
        print("\n" + "=" * 105)
        print(Auxiliars.formatText(step_data['Description'], 100))
        print("=" * 105)
        
        # Verificar si es paso final
        if step_data.get('Is_final_step', 0) == 1:
            print("\n" + "*" * 105)
            print("FIN DE LA AVENTURA".center(105))
            print("*" * 105)
            flag_exit
        
        # Obtener opciones para este paso
        available_options = {}
        for opt_id, opt_data in options.items():
            # Aquí necesitarías una función para obtener opciones por paso
            # Por ahora, muestra todas las opciones disponibles
            if opt_data.get('Leads_to') == current_step or True:  # Placeholder
                available_options[opt_id] = opt_data
        
        if not available_options:
            print("No hay opciones disponibles. Fin de la aventura.")
            break
        
        # Mostrar opciones
        print("\nOpciones disponibles:")
        for opt_id, opt_data in available_options.items():
            formatted = Auxiliars.getFormatedAnswers(
                opt_id,
                opt_data['Description'],
                80,
                5
            )
            print(formatted)
        
        # Solicitar elección
        while True:
            try:
                choice = int(input("\nElige una opción (número): "))
                if choice in available_options:
                    # Registrar elección
                    BBDD.insertCurrentChoice(new_game_id, current_step, choice)
                    
                    # Mover al siguiente paso
                    current_step = available_options[choice]['Leads_to']
                    break
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Por favor, introduce un número.")
    
    # Estadísticas al final
    print("\n" + "=" * 105)
    print("ESTADÍSTICAS DE LA PARTIDA".center(105))
    print("=" * 105)
    # Aquí irían las estadísticas específicas

#TODO
def replay_adventure():
    """Rejugar una aventura ya jugada"""
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


#TODO
def show_reports():
    """Mostrar informes estadísticos"""
    print(Auxiliars.getHeader("INFORMES ESTADÍSTICOS"))
    
    # 1. Respuesta más usada por paso
    print("\n1. RESPUESTA MÁS USADA POR PASO:")
    query1 = """
    SELECT 
        a.id_adventure, 
        a.name as nombre_aventura,
        sa.id_step_adventure,
        sa.description as descripcion_paso,
        so.id_step_option,
        so.description as descripcion_respuesta,
        COUNT(*) as veces_seleccionada
    FROM Game_has_choices gc
    JOIN Step_adventures sa ON gc.id_step_adventure = sa.id_step_adventure
    JOIN Step_options so ON gc.id_step_option = so.id_step_option
    JOIN Adventures a ON sa.id_adventure = a.id_adventure
    GROUP BY so.id_step_option, sa.id_step_adventure, a.id_adventure
    ORDER BY a.id_adventure, sa.id_step_adventure, veces_seleccionada DESC
    """
    
    try:
        report1 = BBDD.get_table(query1)
        print(Auxiliars.getFormatedTable(report1, "Respuestas más usadas"))
    except:
        print("Error al generar el informe 1")
    
    # 2. Jugador que más ha jugado
    print("\n2. JUGADOR CON MÁS PARTIDAS:")
    query2 = """
    SELECT 
        u.username,
        COUNT(g.id_game) as partidas_jugadas,
        MIN(g.date) as primera_partida
    FROM Games g
    JOIN Users u ON g.id_user = u.id_user
    GROUP BY u.id_user
    ORDER BY partidas_jugadas DESC, primera_partida ASC
    LIMIT 1
    """
    
    try:
        report2 = BBDD.get_table(query2)
        print(Auxiliars.getFormatedTable(report2, "Jugador más activo"))
    except:
        print("Error al generar el informe 2")
    
    # 3. Aventuras jugadas por usuario específico
    print("\n3. AVENTURAS JUGADAS POR USUARIO:")
    user_to_check = input("Introduce el nombre de usuario a consultar: ").strip()
    

    query3 = ("SELECT g.id_adventure, a.name as nombre_aventura, g.date as fecha_partida FROM Games g JOIN Adventures a ON g.id_adventure = a.id_adventure JOIN Users u ON g.id_user = u.id_user) WHERE u.username = '{}' ORDER BY g.date DESC".format(user_to_check))
    
    try:
        report3 = BBDD.get_table(query3)
        print(Auxiliars.getFormatedTable(report3, "Aventuras jugadas por {}".format(user_to_check)))
    except:
        print("Error al generar el informe para {}".format(user_to_check))

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
                textOpts="1) Login\n2) Crear nuevo usuario\n3) Rejugar aventura\n4) Ver informes\n5) Salir\n6) Seleccionar aventura\n7) Seleccionar personaje\n8) Jugar aventura",
                inputOptText="\nElige una opción: ",
                rangeList=[1, 2, 3, 4, 5, 6, 7, 8]
            )

            # Login en usuario
            if choice == 1:
                login_user()

                user_logged_in = game_context["idUser"] and game_context['username']

                if user_logged_in:
                    select_adventure()
                    select_character()

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
            
            #DEBUG
            #ADVENTURE
            elif choice == 6:
                select_adventure()

            #CHARACTER
            elif choice == 7:
                select_character()

            #PLAY
            elif choice == 8:
                if not game_context['idUser']:
                    print("Primero debes hacer login.")
                elif not game_context['idAdventure']:
                    print("Primero selecciona una aventura.")
                elif not game_context['idChar']:
                    print("Primero selecciona un personaje.")
                else:
                    play_adventure()

        # Menu logged
        else:
            choice = Auxiliars.getOpt(
                textOpts="1) Logout\n2) Jugar\n3) Rejugar aventura\n4) Ver informes\n5) Salir\n6) Seleccionar aventura\n7) Seleccionar personaje",
                inputOptText="\nElige una opción: ",
                rangeList=[1, 2, 3, 4, 5, 6, 7, 8]
            )

            # Logout del usuario
            if choice == 1:
                logout()

            # Jugar
            elif choice == 2:
                if not game_context['idUser']:
                    print("Primero debes hacer login.")
                elif not game_context['idAdventure']:
                    print("Primero selecciona una aventura.")
                elif not game_context['idChar']:
                    print("Primero selecciona un personaje.")
                else:
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

            #DEBUG
            #ADVENTURE
            elif choice == 6:
                select_adventure()

            #CHARACTER
            elif choice == 7:
                select_character()

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