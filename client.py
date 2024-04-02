import socket
import threading

def authenticate_with_server():
    # Connect to the server
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9998)
    cs.connect(server_address)

    # Receive and print the initial message from the server
    initial_message = cs.recv(1024).decode()
    print("[C]: " + initial_message)

    # Send the username to the server
    username = input("Enter your username: ")
    cs.send(username.encode())

    # Receive and print the message asking for the password from the server
    password_prompt = cs.recv(1024).decode()
    print("[C]: " + password_prompt)

    # Send the password to the server
    password = input("Enter your password: ")
    cs.send(password.encode())

    # Receive and print the authentication result from the server
    auth_result = cs.recv(1024).decode()
    print("[C]: " + auth_result)

    # Close the client socket
    cs.close()

if __name__ == "__main__":
    authenticate_thread = threading.Thread(target=authenticate_with_server)
    authenticate_thread.start()