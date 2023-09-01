import ssl
import socket
import sys

def load_context(cert_file, key_file):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)
    context.load_verify_locations(cafile="ca.crt")
    return context

def connect_to_server(cert_choice):
    cert_file, key_file = ("client1.crt", "client1.key") if cert_choice == "1" else ("client2.crt", "client2.key")
    context = load_context(cert_file, key_file)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with context.wrap_socket(s, server_side=False, server_hostname='localhost') as ssl_sock:
            ssl_sock.connect(('localhost', 12345))
            server_cert = ssl_sock.getpeercert()
            print(f"Connected to server: {server_cert['subject']}")
            
            while True:
                msg = input("Enter a message to send to server (type 'exit' to quit): ")
                ssl_sock.sendall(msg.encode('utf-8'))
                if msg.lower() == 'exit':
                    break

if __name__ == "__main__":
    cert_choice = input("Which client certificate would you like to use? (1 for AllowedOU, 2 for WrongOU): ")
    connect_to_server(cert_choice)
