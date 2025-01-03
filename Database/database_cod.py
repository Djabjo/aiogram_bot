import sqlite3

def input_all_lines_db(id_user: int, tag: str, topic: str, text: str):
    db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute('INSERT INTO db_memory (id_user, tag, topic, text) VALUES (?, ?, ?, ?)', (id_user, tag, topic, text))
    db.commit()
    db.close()

def tag_output_db(id_usert: int):
    db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT tag FROM db_memory WHERE id_user = ?", (id_usert,))
    row = cursor.fetchall()
    tag_add = []
    for tag in row:
        tag_add.append(tag[0])
    db.close()
    return tag_add
    
def topic_output_db(id_user: int, tag: str):
    db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM db_memory WHERE id_user = ? AND tag = ?", (id_user, tag))
    row = cursor.fetchall()
    topic_add = []
    for item in row:
        topic_add.append(str(item[3]))
    db.close()
    return topic_add

def text_topic_output_db(id_user: int, topic: str):
    db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM db_memory WHERE id_user = ? AND topic = ?", (id_user, topic))
    row = cursor.fetchall()
    trxt_topic_add = []
    for item in row:
        trxt_topic_add = item[4]
    db.close()
    return trxt_topic_add

def checking_the_availability_db(id_user: int):
    db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM db_memory WHERE id_user = ?", (id_user,))
    row = cursor.fetchall()
    db.close()
    return row

def del_last_commit_db(id_user: int, topic: str):
    db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute('DELETE FROM db_memory WHERE id_user = ? AND topic = ?', (id_user, topic))
    db.commit()
    db.close()