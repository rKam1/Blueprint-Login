import threading
import sqlite3
import hashlib
import socket

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9998)
ss.bind(server_binding)
ss.listen()

def authenticate_user(username, password):
    # Connect to the database
    conn = sqlite3.connect('test_database.db')
    cursor = conn.cursor()

    # Execute a SELECT query to fetch the user's password from the database
    cursor.execute("SELECT Password FROM users WHERE Username = ?", (username,))
    fetched_password = cursor.fetchone()

    # Close the database connection
    conn.close()

    # If the user exists and the password matches, return True; otherwise, return False
    if fetched_password and fetched_password[0] == password:
        return True
    else:
        return False

def start_connection(client):
    # Ask for the username
    msg = "Please enter your username: "
    client.send(msg.encode())
    username = client.recv(1024).decode().strip()

    # Ask for the password
    msg = "Please enter your password: "
    client.send(msg.encode())
    password = client.recv(1024).decode().strip()

    # Authenticate the user
    if authenticate_user(username, password):
        msg = "Authentication successful!"
    else:
        msg = "Incorrect username or password. Please try again."
    
    # Send authentication result to the client
    client.send(msg.encode())
    print("[S]: Authentication result sent to client")

    # Close the client socket
    client.close()
    print("[S]: Client connection closed")

while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()
    ss.close()