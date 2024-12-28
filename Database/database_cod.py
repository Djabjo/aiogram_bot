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



def tag_output(id_usert: int):
    cursor.execute("SELECT DISTINCT tag FROM db_memory WHERE id_user = ?", (id_usert,))
    row = cursor.fetchall()
    tag_add = []
    for tag in row:
        tag_add.append(tag[0])
    return tag_add

def topic_output(id_user: int, tag: str):
    cursor.execute("SELECT * FROM db_memory WHERE id_user = ? AND tag = ?", (id_user, tag))
    row = cursor.fetchall()
    topic_add = []
    for item in row:
        topic_add.append(str(item[3]))
    return topic_add

def text_topic_output(id_user: int, topic: str):
    cursor.execute("SELECT * FROM db_memory WHERE id_user = ? AND topic = ?", (id_user, topic))
    row = cursor.fetchall()
    trxt_topic_add = []
    for item in row:
        trxt_topic_add = item[4]
    return trxt_topic_add
    
