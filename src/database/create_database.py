import sqlite3
from config.path import DATABASE

path_db = DATABASE / "database.db"

def create_database(db_path=path_db):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        telefone TEXT,
        sigla TEXT
    );
    """)

    conn.commit()
    conn.close()


def insert_user(name, email, telefone, sigla, db_path=path_db):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (name, email, telefone, sigla)
    VALUES (?, ?, ?, ?)
    """, (name, email, telefone, sigla))

    conn.commit()
    conn.close()


def insert_multiple_users():
    usuarios = [
        ("Gustavo Santos", "gustavo@example.com", "1199999-0000", "PR"),
        ("Mariana Silva", "mariana@example.com", "1198888-1111", "RJ"),
        ("Pedro Oliveira", "pedro@gmail.com", "1197777-2222", "MG"),
        ("Ana Costa", "ana.costa@hotmail.com", "1196666-3333", "BA"),
        ("Lucas Ferreira", "lucas.f@example.com", "1195555-4444", "SP"),
    ]

    for user in usuarios:
        insert_user(*user)


def database_run():
    create_database()
    insert_multiple_users()
    print("\nBanco de dados criado com sucesso!\n")
