import sqlite3

conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)")

user_credentials = [
    ('Alice', 'password123'),
    ('Bob', 'securepass'),
    ('Charlie', 'qwerty'),
    ('David', '123456'),
    ('Eve', 'letmein'),
    ('Frank', 'password123'),
    ('Grace', 'pass123')
]



for user, password in user_credentials:
    cursor.execute("INSERT OR IGNORE INTO users (Username, Password) VALUES (?, ?)", (user, password))

cursor.execute("SELECT * FROM users")
allresponses = cursor.fetchall() 

conn.commit()
conn.close()