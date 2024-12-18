import sqlite3

#database
db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
cursor = db.cursor()

def db_table_val(id_user: int, tag: str, topic: str, text: str):
    cursor.execute('INSERT INTO db_memory (id_user, tag, topic, text) VALUES (?, ?, ?, ?)', (id_user, tag, topic, text))
    db.commit()

