# -*- coding: utf-8 -*-
import MySQLdb

def connect_db(host,user,passwd,db):
    try:
        conn = MySQLdb.connect(host=host,user=user,passwd=passwd,
                            db=db)
        return conn
    except:
        print ('Erro na conexão ao banco')

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def retrieve_midia(id,cursor):
    # select photo column of a specific author
    query = "SELECT * FROM Midia WHERE id = %s"

    try:
        print ('Chegou até aqui')
        cursor.execute(query,(id,))
        midia = cursor.fetchone()
        # write blob data into a file
        write_file(midia[1], '/home/pedrohenique/' + midia[2] + "." + midia[3])

    except:
        print('Erro na query do banco')

def insert_midia(filename,type,path,conn):
    data = open(path + "/" + filename + '.' + type,'rb').read()
    query = "INSERT INTO Midia (mid,name,type) VALUES (%s,%s,%s)"
    cursor = conn.cursor()
    cursor.execute(query, (data,filename,type))
    conn.commit()
