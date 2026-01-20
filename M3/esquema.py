# Importamos nuestro módulo con funciones de BBDD y utilidades
import Auxiliars as mj

def main():
    game_context = {}  # Diccionario para guardar contexto de la partida

    while True:
        # Menú principal
        opcion = mj.getOpt(
            textOpts="\n1) Login\n2) Crear usuario\n3) Mostrar aventuras\n4) Jugar\n5) Replay\n6) Informes\n7) Salir",
            inputOptText="\nElige tu opción:",
            rangeList=[1, 2, 3, 4, 5, 6, 7]
        )

        if opcion == 1:  # Login
            user = input("Usuario: ")
            password = input("Contraseña: ")
            resultado = mj.checkUserbdd(user, password)
            if resultado == 1:
                game_context['idUser'] = mj.getUsers()[user]['idUser']
                game_context['user'] = user
                print("Login correcto.")
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == 2:  # Crear usuario
            # Validar formato usuario/contraseña y registrar en BBDD
            pass

        elif opcion == 3:  # Mostrar aventuras
            adventures = mj.get_adventures_with_chars()
            print(mj.getFormatedAdventures(adventures))

        elif opcion == 4:  # Jugar
            if 'idUser' not in game_context:
                print("Primero debes hacer login.")
                continue

            # Seleccionar aventura
            adventures = mj.get_adventures_with_chars()
            id_aventura = mj.elegir_aventura(adventures)  # función auxiliar
            game_context['idAdventure'] = id_aventura
            game_context['nameAdventure'] = adventures[id_aventura]['Name']

            # Seleccionar personaje disponible para esta aventura
            characters = mj.get_characters()
            id_personaje = mj.elegir_personaje(adventures[id_aventura]['characters'], characters)
            game_context['idChar'] = id_personaje
            game_context['characterName'] = characters[id_personaje]

            # Generar ID de partida y guardar en BBDD
            id_game = mj.setIdGame()
            mj.insertCurrentGame(id_game, game_context['idUser'], id_personaje, id_aventura)

            # Cargar pasos de la aventura
            pasos = mj.get_id_bystep_adventure(id_aventura)
            respuestas = mj.get_answers_bystep_adventure(id_aventura)

            # Comenzar juego
            paso_actual = mj.get_first_step_adventure(id_aventura)
            while True:
                paso_info = pasos[paso_actual]
                print(mj.formatText(paso_info['Description'], 105, '\n'))

                if paso_info['Final_Step'] == 1:
                    print("Fin de la aventura.")
                    break

                # Mostrar opciones
                for id_respuesta in paso_info['answers_in_step']:
                    print(mj.getFormatedAnswers(id_respuesta, respuestas[(paso_actual, id_respuesta)]['Description'], 100, 4))

                # Elegir respuesta
                eleccion = mj.getOpt(rangeList=paso_info['answers_in_step'])
                # Guardar elección en BBDD
                mj.insertCurrentChoice(id_game, paso_actual, eleccion)
                # Mostrar texto de resolución de la respuesta
                print(mj.formatText(respuestas[(paso_actual, eleccion)]['Resolution_Answer'], 105, '\n'))
                # Ir al siguiente paso
                paso_actual = respuestas[(paso_actual, eleccion)]['NextStep_Adventure']

            print("Partida terminada.")
            # Mostrar estadísticas (opcional)
            mj.mostrar_estadisticas(id_aventura)

        elif opcion == 5:  # Replay
            partidas = mj.getReplayAdventures()
            id_game = mj.seleccionar_partida(partidas)  # función auxiliar
            choices = mj.getChoices(id_game)
            mj.replay(choices)

        elif opcion == 6:  # Informes
            # Menú de informes
            informe = mj.getOpt(
                textOpts="\n1) Respuesta más usada por paso\n2) Jugador más activo\n3) Aventuras jugadas por usuario",
                inputOptText="\nElige informe:",
                rangeList=[1, 2, 3]
            )
            if informe == 1:
                query = "SELECT ... "  # Consulta para el informe 1
                tabla = mj.get_table(query)
                print(mj.getFormatedTable(tabla, title="Respuestas más usadas"))
            # ... otros informes

        elif opcion == 7:  # Salir
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()