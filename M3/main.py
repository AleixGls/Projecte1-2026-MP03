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

# REVISAR
def play_adventure():
    """Función para jugar una aventura seleccionada"""
    
    # Verificar que tenemos todo lo necesario
    if not game_context['idUser']:
        print("Error: No hay usuario logueado.")
        return
    if not game_context['idAdventure']:
        print("Error: No hay aventura seleccionada.")
        return
    if not game_context['idChar']:
        print("Error: No hay personaje seleccionado.")
        return
    
    print(Auxiliars.getHeader("JUGANDO AVENTURA"))
    print(f"Aventura: {game_context['adventureName']}")
    print(f"Personaje: {game_context['characterName']}")
    
    # Obtener un nuevo ID para el juego
    existing_ids = BBDD.getIdGames()
    if existing_ids:
        new_id = max(existing_ids) + 1
    else:
        new_id = 1
    
    game_context['idGame'] = new_id
    
    # Insertar el juego en la base de datos
    try:
        BBDD.insertCurrentGame(new_id, game_context['idUser'], 
                              game_context['idChar'], game_context['idAdventure'])
    except Exception as e:
        print(f"Error al crear la partida: {e}")
        return
    
    # Obtener datos de la aventura
    steps = BBDD.get_id_bystep_adventure(game_context['idAdventure'])
    options = BBDD.get_answers_bystep_adventure(game_context['idAdventure'])
    
    if not steps:
        print("Error: No se encontraron pasos para esta aventura.")
        return
    
    # Encontrar el primer paso (el que no aparece en ningún Leads_to)
    first_step = None
    all_leads_to = []
    
    # Recopilar todos los destinos de las opciones
    for opt_id, opt_info in options.items():
        leads_to = opt_info['Leads_to']
        if leads_to:
            all_leads_to.append(leads_to)
    
    # Encontrar el paso que no es destino de ninguna opción
    for step_id in steps:
        if step_id not in all_leads_to:
            first_step = step_id
            break
    
    if not first_step:
        print("Error: No se pudo encontrar el primer paso de la aventura.")
        return
    
    current_step = first_step
    game_finished = False
    
    while not game_finished and current_step in steps:
        # Obtener información del paso actual
        step_info = steps[current_step]
        description = step_info['Description']
        is_final = step_info['Is_final_step']
        
        # Reemplazar %personaje% por el nombre del personaje
        description = description.replace('%personaje%', game_context['characterName'])
        
        # Mostrar el paso
        print("\n" + "="*105)
        print(f"PASO: {current_step}")
        print("="*105)
        print(Auxiliars.formatText(description, 105))
        print("="*105)
        
        # Si es paso final, terminar la aventura
        if is_final:
            print("\n¡FIN DE LA AVENTURA!")
            game_finished = True
            break
        
        # Obtener opciones para este paso
        # Necesitamos una nueva función en BBDD para obtener las opciones de un paso específico
        # Por ahora, buscaremos manualmente
        step_options = {}
        
        # Buscar todas las opciones que tengan id_step_adventure = current_step
        # Necesitamos conectar directamente con la base de datos
        import pymysql
        
        conn = pymysql.connect(
            host='chooseyourstory-database.cbim0ycisox3.eu-north-1.rds.amazonaws.com',
            user='admin',
            password='Jefecolorado123!',
            database='mydb')
        
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Id_step_option, description, leads_to 
            FROM Step_options 
            WHERE id_step_adventure = %s
        """, (current_step,))
        
        rows = cursor.fetchall()
        
        for row in rows:
            option_id = row[0]
            option_desc = row[1]
            leads_to = row[2]
            
            step_options[option_id] = {
                'Description': option_desc,
                'Leads_to': leads_to
            }
        
        cursor.close()
        conn.close()
        
        # Si no hay opciones, es un paso final implícito
        if not step_options:
            print("No hay opciones disponibles. Fin de la aventura.")
            game_finished = True
            break
        
        # Mostrar opciones
        print("\nOPCIONES DISPONIBLES:")
        formatted_answers = ""
        
        for opt_id in sorted(step_options.keys()):
            opt_text = step_options[opt_id]['Description']
            opt_text = opt_text.replace('%personaje%', game_context['characterName'])
            
            # Formatear la respuesta
            formatted_answer = Auxiliars.getFormatedAnswers(
                opt_id, opt_text, 100, 105
            )
            formatted_answers += formatted_answer + "\n"
        
        print(formatted_answers)
        
        # Pedir al usuario que elija una opción
        valid_options = list(step_options.keys())
        
        while True:
            try:
                choice_input = input(f"Elige una opción ({', '.join(map(str, valid_options))}): ").strip()
                
                if choice_input.isdigit():
                    choice_int = int(choice_input)
                    if choice_int in valid_options:
                        selected_option = choice_int
                        break
                    else:
                        print(f"Opción no válida. Por favor, elige entre: {valid_options}")
                else:
                    print("Entrada no válida. Introduce un número.")
            except ValueError:
                print("Entrada no válida. Introduce un número.")
        
        # Registrar la elección en la base de datos
        # Primero necesitamos crear la función insertCurrentChoice en BBDD
        # Por ahora, hacemos la inserción directamente
        try:
            conn = pymysql.connect(
                host='chooseyourstory-database.cbim0ycisox3.eu-north-1.rds.amazonaws.com',
                user='admin',
                password='Jefecolorado123!',
                database='mydb')
            
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Game_has_choices (id_game, id_step_adventure, id_step_option)
                VALUES (%s, %s, %s)
            """, (new_id, current_step, selected_option))
            
            conn.commit()
            cursor.close()
            conn.close()
            
        except Exception as e:
            print(f"Error al registrar la elección: {e}")
        
        # Mostrar la respuesta seleccionada
        selected_text = step_options[selected_option]['Description']
        selected_text = selected_text.replace('%personaje%', game_context['characterName'])
        print("\n" + ">"*50)
        print("Has elegido:")
        print(Auxiliars.formatText(selected_text, 105))
        print(">"*50)
        
        # Avanzar al siguiente paso
        next_step = step_options[selected_option]['Leads_to']
        
        if next_step and next_step in steps:
            print(f"\nAvanzando al paso {next_step}...")
            current_step = next_step
        else:
            print("\nNo hay siguiente paso definido. Fin de la aventura.")
            game_finished = True
    
    # Mostrar estadísticas o mensaje final
    print("\n" + "*"*105)
    print("¡Partida completada!")
    print(f"ID de partida: {new_id}")
    print("Puedes revisar esta partida más tarde desde la opción 'Rejugar aventura'")
    print("*"*105)
    
    input("\nPresiona Enter para volver al menú principal...")


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