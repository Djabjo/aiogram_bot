import sqlite3

#database
db = sqlite3.connect('Chat_history.db', check_same_thread=False)
cursor = db.cursor()

def db_table_val(titul: str, text: str):
    cursor.execute('INSERT INTO db (titul, text) VALUES (?, ?, ?, ?)', (titul, text))
    db.commit()