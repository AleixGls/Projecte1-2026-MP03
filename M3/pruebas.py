import pymysql

try:
    conn = pymysql.connect(
        host='chooseyourstory-database.cbim0ycisox3.eu-north-1.rds.amazonaws.com',
        user='admin',
        password='Jefecolorado123!',
        database='mydb')

    cursor = conn.cursor()
    consulta = "SELECT * FROM Users;"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    print(resultados)
except Exception as e:
    print(f'Error al conectar con la BBDD en la función loadBBDD_players(): {e}')
    _ = input('Enter to Continue')

