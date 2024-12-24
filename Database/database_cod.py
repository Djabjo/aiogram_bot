import sqlite3

#database
db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
cursor = db.cursor()

def db_table_val(id_user: int, tag: str, topic: str, text: str):
    cursor.execute('INSERT INTO db_memory (id_user, tag, topic, text) VALUES (?, ?, ?, ?)', (id_user, tag, topic, text))
    db.commit()

def del_last_commit(id_user: int, topic: str):
    cursor.execute('DELETE FROM db_memory WHERE id_user = ? AND topic = ?', (id_user, topic))
    db.commit()
id = 7469819884

def tag_output(id: int):
    cursor.execute("SELECT DISTINCT id_user, tag FROM db_memory")
    row = cursor.fetchone()
    print(row)

tag_output(id)
