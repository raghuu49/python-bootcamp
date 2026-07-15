import sqlite3

def start_connection():
    con=sqlite3.connect('todo.db')
    con.execute('PRAGMA foreign_keys = ON')
    return con

#first table created (user_id|name)-> user_id automatically incrememnts
def create_tables():
    con=start_connection()
    cur=con.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE
            );
            ''')
    cur.execute(''' 
                CREATE TABLE IF NOT EXISTS tasks( 
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER, 
                task_text TEXT NOT NULL, 
                status BIT NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE );
                ''')
    con.commit()
    con.close()

def create_user(user_name): # None or last row id
    con=start_connection()
    cur=con.cursor()
    try:
        cur.execute("INSERT INTO users(username) VALUES(?)",(user_name,))
        con.commit()
        return cur.lastrowid
    except sqlite3.IntegrityError as e:
        return None
    finally:
        con.close()

def get_user(user_name): #if present then a tuple else empty tuple
    con=start_connection()
    cur=con.cursor()
    try:
        query='SELECT * FROM users where username= ?'
        res=cur.execute(query,(user_name,))
        return res.fetchone()
    finally:
        con.close()

def add_task(user_id,task_text): # if added then a number else None
    con=start_connection()
    cur=con.cursor()
    try:
        cur.execute("INSERT INTO tasks(user_id,task_text) VALUES(?,?)",(user_id,task_text))
        con.commit()
        return cur.lastrowid
    except sqlite3.IntegrityError as e:
        return None
    finally:
        con.close()

def get_tasks(userid): #if present then list else []
    con=start_connection()
    cur=con.cursor()
    try:
        query='SELECT * from tasks where user_id=?'
        res=cur.execute(query,(userid,))
        return res.fetchall()
    finally:
        con.close()

def update_task(taskid,status_): #return: if updated 1 else 0
    con=start_connection()
    cur=con.cursor()
    try:
        query='UPDATE tasks SET status=? WHERE task_id=?'
        cur.execute(query,(status_,taskid))
        con.commit()
        return cur.rowcount
    finally:
        con.close()
        
def delete_task(taskid): #return: if delelted 1 else 0
    con=start_connection()
    cur=con.cursor()
    try:
        query='DELETE FROM tasks WHERE task_id=?'
        cur.execute(query,(taskid,))
        con.commit()
        return cur.rowcount
    finally:
        con.close()

def delete_user(userid): #return: if deleted number else 0
    con=start_connection()
    cur=con.cursor()
    try:
        query='DELETE FROM users WHERE user_id=?'
        cur.execute(query,(userid,))
        con.commit()
        return cur.rowcount
    finally:
        con.close()