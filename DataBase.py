#Biblioteca 
import sqlite3

#Conexão
conn = sqlite3.connect('UserData.db')

#Criação do cursor
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

