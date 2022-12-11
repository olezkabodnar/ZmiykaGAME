import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

#cursor.execute("""create table users(login text, password text, email text, name text)""")
def register():
    print("Hello")
    login = input("Enter your login: ")
    password = input ("Enter your password: ")
    email = input("Enter your email: ")
    name = input("Enter your name: ")
    cursor.execute("INSERT into users values (?, ?, ?, ?)", (login, password, email, name))
    conn.commit()

def get():
    cursor.execute("select * from users where login = ? and password = ?" ,"Oleg")
    return  cursor.fetchall()

def edit():
    cursor.execute("UPDATE_users_set name = ?",("Oleg,") )

cursor.execute("UPDATE users set name = ?",("Oleg",))
