# HACER
def formatText(text,lenLine,split):
    # A aquesta funció li passem un text, i ens retorna el mateix text de manera que cada línia té com a màxim lenline d'ample, entre línia i línia coŀloquem el separador "split", que normalment serà un salt de línia.
    # No es tallen les paraules, sempre s'arrodoneix a l'últim espai abans de lenline.
    pass

# COMPLETADA
def getHeader(text):
    # Aquesta funció li passem un text i ens retorna una capçalera com la següent:
    # *********************************************************************************************************
    # ===================================================text==================================================
    # *********************************************************************************************************

    header = (
        ("*"*105)                 + "\n" + 
        str(text).center(105,"=") + "\n" + 
        ("*"*105)
    )

    return header

# HACER
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    # A aquesta funció li passem una tupla amb textos, l'ample de cada columna, i el marge que ha d'haver-hi entre cada columna i ens retorna els textos formatats segons l'ample i el marge que hem indicat.
    pass

# HACER
def getFormatedAdventures(adventures):
    # A aquesta funció li passem el diccionari adventures i retorna una cadena que una vegada impresa ens mostra:
    # La capçalera de la selecció d'aventures i les aventures amb id, títol i descripció de les aventures formatades en columnes.
    pass

# HACER
def getFormatedAnswers(idAnswer,text,lenLine,leftMargin):
    # A aquesta funció li passem un id de resposta, el text de la resposta, longitud de la línia i marge a la dreta, i ens retorna la resposta amb els paràmetres passats.
    # Aquesta funció ens serà útil per a presentar les respostes possibles en cadascun dels passos.
    # Observem que en formatar les línies, no tallem cap paraula per la meitat
    pass

# HACER
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    # Aquesta funció, rep una tupla amb els noms de les capçaleres de les columnes (t_name_columns) i una tupla amb les seves grandàries t_size_columns i ens retorna una capçalera formatada segons els paràmetres passats.
    pass

# HACER
def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    # A aquesta funció li passem com a paràmetres, un diccionari del tipus {id: {diccionari amb dades}}
    # Una tupla amb les keys que ens interessa.
    # Una tupla amb les grandàries de cada columna.
    # Per exemple:
    # tuple_of_keys = (“Username”,”Name”,”CharacterName”,”date”)
    # weigth_of_columns = (20, 30, 20, 20)
    # dict_of_data = {
    #     4: {
    #         'idUser': 2, 
    #         'Username': 'Jordi', 
    #         'idAdventure': 1, 
    #         'Name': 'Este muerto esta muy vivo',
    #         'date': datetime.datetime(2021, 11, 28, 18, 17, 20),
    #         'idCharacter': 1, 
    #         'CharacterName': 'Beowulf'
    #     }, 
    #     5: {
    #         'idUser': 2, 
    #         'Username': 'Jordi',
    #         'idAdventure': 1,
    #         'Name': 'Este muerto esta muy vivo', 
    #         'date': datetime.datetime(2021, 11, 26, 13, 28, 36), 
    #         'idCharacter': 1,
    #         'CharacterName': 'Beowulf'
    #     }
    # }
    # I ens retorna un string que imprès té forma de taula, amb les dades corresponents a les keys que passem i formatades amb les grandàries donades
    pass

# HACER
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


    pass

# HACER
def getFormatedTable(queryTable,title=""):
    pass

# HACER
def checkPassword(password):
    # Funció que chequea si el format del password és correcte.
    # Un password correcte tindrà una longitud entre 8 i 12 caràcters.
    # Alguna lletra majúscula, alguna lletra minúscula, algun número, algun caràcter especial, sense espais.
    # Si alguna de les condicions no es compleix, la mateixa funció ens mostrarà un missatge informatiu i retornarà False.
    # En cas que el password compleixi tots els requeriments, ens retornarà True
    pass

# HACER
def checkUser(user):
    # Funció que chequea que un usuari tingui el format correcte. longitud entre 6 i 10 i alfanumèric.
    # Si alguna de les condicions no es compleix, la mateixa funció ens mostrarà un missatge informatiu i retornarà False.
    # En cas que el password compleixi tots els requeriments, ens retornarà True
    pass

# HACER
def userExists(user):
    # Funció que ens retorna True si l’usuari existeix, o False si no existeix.
    pass

# HACER
def replay(choices):
    # Aquesta funció serà l'encarregada de fer-nos el replay d'una aventura ja jugada, una vegada hàgim triat el idGame que volem reviure.
    # Li passarem una tupla de tuples del tipus:
    # ((pas, selecció), (pas, selecció),(pas, selecció)... )
    # Amb tots els passos i seleccions que es van fer en aquesta aventura i ens mostrarà l'aventura pas a pas com si l'estiguéssim jugant de nou, però en comptes de demanar-nos triar un pas, ens demanarà que cliquem "Enter" per a continuar.
    pass