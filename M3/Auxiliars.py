import BBDD
import datetime
# COMPLETADA
def formatText(text, lenLine, split="\n"):
    # A aquesta funció li passem un text, i ens retorna el mateix text de manera que cada línia té com a màxim
    # lenline d'ample, entre línia i línia coŀloquem el separador "split", que normalment serà un salt de línia. No
    # es tallen les paraules, sempre s'arrodoneix a l'últim espai abans de lenline.
    text+=" "
    word = ""
    phrase = ""
    count = 0
    for a in text:
        word += a
        count += 1
        if a == " ":
            phrase += word
            word = ""
        if count % lenLine == 0:
            phrase += split
    return phrase

# COMPLETADA
def getHeader(text):
    # Aquesta funció li passem un text i ens retorna una capçalera com la següent:
    # *********************************************************************************************************
    # ===================================================text==================================================
    # *********************************************************************************************************

    header = (
            ("*" * 105) + "\n" +
            str(text).center(105, "=") + "\n" +
            ("*" * 105)
    )

    return header


# COMPLETADA?
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    # A aquesta funció li passem una tupla amb textos, l'ample de cada columna, i el marge que ha d'haver-hi entre cada columna i ens retorna els textos formatats segons l'ample i el marge que hem indicat.
    
    # Extraer la longitud de la tupla de frases
    len_texts = len(tupla_texts)

    # Crear la lista columnas en base a las frases que tenemos que formatear
    columnas = [None] * len_texts
    
    # Inicializar variables
    palabra = ""
    fila = ""
    
    # For para extraer las frases de las tuplas y 
    # crear las filas que tendran que tener las columnas
    for i1 in range(len_texts):

        # Obtener la frase que vamos a seccionar de la tupla_texts
        frase = tupla_texts[i1]
        
        #Inizializar la lista columnas, y en la siguiente pasada reiniciarla
        columna = []
        palabras = []
                 
        # For para extraer las palabras de la frase y añadirlas a la lista palabras
        for i2 in range(len(frase)):
        
            # Detectar la letra de la iteracion actual
            letra = frase[i2]

            # Condicionales para crear la lista de palabras de la frase
            # Si la letra no es un espacio, añadirla a la palabra
            if letra != " ":
                palabra += letra

            # Si lo es, hay 2 opciones
            else:
                #Si la palabra no esta vacia, añadirla a la lista de palabras
                if palabra != "":
                    palabras.append(palabra)
                    palabra=""

                # Si esta vacia, no hacer nada y continuar el bucle
                else:
                    pass
        
        # Al acabar el bucle, añadir la ultima palabra a la lista y reiniciar la variable 
        palabras.append(palabra)
        palabra=""

        # For para pasar las palabras extraidas anteriormente y 
        # formatearlas en lineas del ancho de la columna, para poder 
        # crear las columnas para el string que devolvera la funcion
        for i2 in range(len(palabras)):

            #Condicionales para añadir palabra a la fila
            #Si en la fila no hay palabras se añade
            if fila == "":
                fila+=palabras[i2]

            #Si hay pueden pasar 2 cosas
            else:
                # Si la fila puede soportar un espacio y la palabra, esta se añade
                if (len(palabras[i2]) + 1) + len(fila) <= tupla_sizes[i1]:
                    fila+=(" "+palabras[i2])

                # Si no, la fila se añade a la columna, se reinicia y se añade la palabra a la nueva fila
                else:
                    columna.append(fila)
                    fila=""
                    fila+=palabras[i2]
            
            # En la iteracion final, se comprueba si la fila no estaba vacia,
            # se añade a la columna y se reinicia la variable
            if i2 == len(palabras)-1 and fila !="":
                columna.append(fila)
                fila=""

        # Introudcir la columna creada en la lista de columnas
        columnas[i1] = columna

    # Inicializar variables
    filas_max = 0

    # For para averiguar cuantas longitud de lineas hay
    for i1 in range(len(columnas)):
        
        # Condicional para actualizar la longitud maxima
        if len(columnas[i1]) > filas_max:
            filas_max = len(columnas[i1])
    
    # Inicializar variables
    fila_actual = ""
    linea = ""
    frase_formateada = ""

    #For para recorrer el maximo numero de filas que hemos sacado antes
    for i1 in range(filas_max):

        #For para recorrer el numero de columnas
        for i2 in range(len(columnas)):

            # Condicional comprobante de que existe esa fila en la columna que estamos y 
            # formatear la linea al tamaño de la tupla_sizes que le corresponde a esa columna
            if i1 < len(columnas[i2]):
                fila_actual = str(columnas[i2][i1]).ljust(tupla_sizes[i2])

            # Si no lo existe, rellenar el hueco con espacios
            else:
                fila_actual = " " * tupla_sizes[i2]

            # Sumar la fila actual a la linea que devolvera la funcion
            linea += fila_actual

            # Condicional para sumar los margenes a la linea si estan entre las columnas
            if i2 != len(columnas) - 1:
                linea += (" "*margin)
            
            # Si es el final, sumarle un salto de linea
            else:
                linea += "\n"

        # Sumar la linea formateada al string que devolver 
        # la funcion y resetear la linea para la siguiente
        frase_formateada += linea
        linea = ""

    # Devolver el sring completamente formateado
    return frase_formateada



# COMPLETADA
def getFormatedAdventures(adventures):
    # A aquesta funció li passem el diccionari adventures i retorna una cadena que una vegada impresa ens mostra: La
    # capçalera de la selecció d'aventures i les aventures amb id, títol i descripció de les aventures formatades en
    # columnes.
    t_name_columns=("Id Adventure", "Adventure","Description")
    t_size_columns=(15,30,50)
    cabecera=getHeadeForTableFromTuples(t_name_columns, t_size_columns,"Adventures")

    datos=""
    for adventureId in adventures:
        cont=0
        datos+=(str(adventureId).ljust(t_size_columns[cont]))
        for item in (adventures[adventureId]):
            cont+=1
            datos += (str(adventures[adventureId][item]).ljust(t_size_columns[cont]))
        datos+="\n"
    return cabecera+"\n"+datos

# COMPLETADA
def getFormatedAnswers(idAnswer, text, lenLine, leftMargin):
    # A aquesta funció li passem un id de resposta, el text de la resposta, longitud de la línia i marge a la dreta,
    # i ens retorna la resposta amb els paràmetres passats. Aquesta funció ens serà útil per a presentar les
    # respostes possibles en cadascun dels passos. Observem que en formatar les línies, no tallem cap paraula per la
    # meitat
    answer=("{}) {}".format(idAnswer,text))
    formatedAnswer=formatText(answer,lenLine)
    return formatedAnswer.ljust(leftMargin)


# COMPLETADA
def getHeadeForTableFromTuples(t_name_columns, t_size_columns, title=""):
    # Aquesta funció, rep una tupla amb els noms de les capçaleres de les columnes (t_name_columns) i una tupla amb
    # les seves grandàries t_size_columns i ens retorna una capçalera formatada segons els paràmetres passats.
    cabecera=""
    cabecera_ancho=0
    for i in range(0, len(t_name_columns)):
        t_name=t_name_columns[i]
        t_size=t_size_columns[i]
        cabecera_ancho+=t_size
        cabecera+=(str(t_name).ljust(t_size))
    return(title.center(cabecera_ancho,"=")+"\n"+cabecera+"\n"+"".center(cabecera_ancho,"*"))
# COMPLETADA
def getTableFromDict(tuple_of_keys, weigth_of_columns, dict_of_data):
    # A aquesta funció li passem com a paràmetres, un diccionari del tipus {id: {diccionari amb dades}}
    # Una tupla amb les keys que ens interessa.
    # Una tupla amb les grandàries de cada columna.
    # Per exemple:
    # tuple_of_keys = ("Username", "Name", "CharacterName", "date")
    # weigth_of_columns = (20, 30, 20, 20)
    # dict_of_data = {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
    #                     'date': datetime.datetime(2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName': 'Beowulf'},
    #                 5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
    #                     'date': datetime.datetime(2021, 11, 26, 13, 28, 36), 'idCharacter': 1, 'CharacterName': 'Beowulf'}}
    # I ens retorna un string que imprès té forma de taula, amb les dades corresponents a les keys que passem i formatades amb les grandàries donades
    datos = ""

    for dicto in dict_of_data:
        datos += str(dicto).ljust(10)
        for key in range(0, len(tuple_of_keys)):
            if tuple_of_keys[key] in dict_of_data[dicto]:
                if tuple_of_keys[key]=='date':
                    dict_of_data[dicto][tuple_of_keys[key]].strftime("%Y/%m/%d  %H:%M:%S")
                datos += str(dict_of_data[dicto][tuple_of_keys[key]]).ljust(weigth_of_columns[key])
        datos+="\n"
    return datos
# COMPLETADA
def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    # Aquesta funció ens prepara un menú en mode text.
    # El text ens indica les opcions que podem triar després d'indicar-nos què estem escollint una llista o diccionari
    # Aquest és el text TextOpts que passem.
    # Pasem també el text que volem veure, a la part on ens indica que escrivim la selecció.
    # Una llista d'excepcions , que donarà validesa a un valor del menú, per exemple 0 si
    # volem utilitzar l'opció 0 per a sortir o tornar enrere i no està dins de la nostra llista o
    # diccionari o qualsevol caràcter especial que vulguem utilitzar com a opció a escollir.
    # Per exemple:
    # textOpts = "\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
    # inputOptText = "\nElige tu opción:"
    # lista = [1,2,3,4]
    # exceptions = ["w","e",-1]
    # opc = getOpt(textOpts,inputOptText,lista,exceptions)
    # Ens mostrarà la sortida:
    # 1)Login
    # 2)Create user
    # 3)Show Adventures
    # 4)Exit
    #
    # Elige tu opción:
    # I ens retornarà l'opció seleccionada, o mostrarà un missatge d'error si l'opció no és
    # 1,2,3,4,”w,”,”e” ó -1
    # El paràmetre rangelist serà la llista d'opcions vàlides del nostre menú (a més a més de
    # les indicades en excepcions).
    # Si passem la variable diccionari, les seves claus seran opcions vàlides també.

    #Bucle
    flagMenu = True
    while flagMenu == True:

        #Menu
        print(textOpts)
        opt_str = input(inputOptText)

        # Comprobante int
        try:
            opt_int = int(opt_str)
            if opt_int in rangeList or opt_int in dictionary or opt_int in exceptions:
                return opt_int

        # Comprobante string
        except:
            if opt_str in rangeList or opt_str in dictionary or opt_str in exceptions:
                return opt_str
            else:
                print("\nOpcio no valida.")

        # Comprobante string del int
        else:
            if opt_str in rangeList or opt_str in dictionary or opt_str in exceptions:
                return opt_str
            else:
                print("\nOpcio no valida.")

# HACER #Para esto se necesitan los informes
def getFormatedTable(queryTable,title=""):
    # Aquesta funció rep una taula del tipus que retorna la funció "getTable" i ens formata el contingut de la taula per a presentar-lo per pantalla.
    # Aquesta funció ens servirà per mostrar els informes.
    # S’ha de tenir en compte que l’amplada màxima que es pot fer servir a la consola en el cas dels reports és de 120, per tant, haurem de dividir aquests 120 entre les columnes que tingui la taula que hem de mostrar.
    # Per exemple, si la funció getTable ens ha retornat:
    # (
    #   ('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA - DESCRIPCION', 'NUMERO VECES SELECCIONADA'), 
    #   ('10 - Todos los h├®roes necesitan su princesa', '101 - Son las 6 de la ma├▒ana, %personaje% est├í profundamente dormido. Le suena la alarma!', '101 - Apaga la alarma porque quiere dormir, han sido d├¡as muy duros y %personaje% necesita un descanso.', 7),
    #   ('10 - Todos los h├®roes necesitan su princesa', '103 - Nuestro h├®roe %personaje% se viste r├ípidamente y va an direcci├│n al ciber, hay mucho jaleo en la calle, tambi├®n mucha polic├¡a.', '108 - Entra en el ciber a revisar si la princesa Wyoming sigue dentro.', 5)
    # )
    # Aquesta funció ens retornarà un string que es pot imprimir.
    pass



# COMPLETADA
def checkPassword(password):
    # Funció que chequea si el format del password és correcte.
    # Un password correcte tindrà una longitud entre 8 i 12 caràcters.
    # Alguna lletra majúscula, alguna lletra minúscula, algun número, algun caràcter especial, sense espais.
    # Si alguna de les condicions no es compleix, la mateixa funció ens mostrarà un missatge informatiu i retornarà False.
    # En cas que el password compleixi tots els requeriments, ens retornarà True
    error_msg = ""
    upper_bool = False
    lower_bool = False
    number_bool = False
    specialchar_bool = False
    if len(password) < 8:
        error_msg = "El password té menys de 8 caràcters. "
    elif len(password) > 12:
        error_msg = "El password té més de 12 caràcters. "
    else:
        for a in password:
            if a == " ":
                error_msg = "El password no pot contenir espais. "
            if not upper_bool:
                if a.isupper():
                    upper_bool = True
            if not lower_bool:
                if a.islower():
                    lower_bool = True
            if not number_bool:
                if a.isnumeric():
                    number_bool = True
            if not specialchar_bool:
                if not a.isalnum():
                    if a.isascii():
                        specialchar_bool = True
        if upper_bool == False:
            error_msg = "El password no conté almenys una majúscula. "
        elif lower_bool == False:
            error_msg = "El password no conté almenys una minúscula. "
        elif number_bool == False:
            error_msg = "El password no conté almenys un número. "
        elif specialchar_bool == False:
            error_msg = "El password no conté almenys un caràcter especial. "
    if error_msg != "":
        print(error_msg)
        return False
    else:
        return True


# COMPLETADA
def checkUser(user):
    # Funció que chequea que un usuari tingui el format correcte. longitud entre 6 i 10 i alfanumèric.
    # Si alguna de les condicions no es compleix, la mateixa funció ens mostrarà un missatge informatiu i retornarà False.
    # En cas que el password compleixi tots els requeriments, ens retornarà True
    error_msg = ""
    alnum_bool = True
    if len(user) < 6:
        error_msg = "El nombre de usuario tiene menos de 6 carácteres. "
    elif len(user) > 10:
        error_msg = "El nombre de usuario tiene más de 10 carácteres. "
    elif not user.isalnum():
        error_msg = "El nom d'usuari només pot contenir caràcters alfanumérics. "
    if error_msg != "":
        print(error_msg)
        return False
    else:
        return True


# COMPLETADA
def userExists(user):
    # Funció que ens retorna True si l’usuari existeix, o False si no existeix.
    userlist=BBDD.getUsers()
    for name in userlist:
        if user==name:
            return True
    return False

# HACER Esto creo que hay que implementar el main, basicamente que sea el juego pero no puedas elegir opcion, coja automaticamente la de la tupla
def replay(choices):
    # Aquesta funció serà l'encarregada de fer-nos el replay d'una aventura ja jugada, una vegada hàgim triat el idGame que volem reviure.
    # Li passarem una tupla de tuples del tipus: ((pas, selecció), (pas, selecció),(pas, selecció)... )
    # Amb tots els passos i seleccions que es van fer en aquesta aventura i ens mostrarà l'aventura pas a pas
    # com si l'estiguéssim jugant de nou, però en comptes de demanar-nos triar un pas, ens demanarà que cliquem "Enter" per a continuar.
    pass

caca=((101,109),(120,192),(110,304))
replay(caca)