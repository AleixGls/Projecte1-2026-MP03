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
    pass

# HACER
def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
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
    pass