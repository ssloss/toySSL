import ssl
import socket

# Create a default SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Load client's certificate and key
context.load_cert_chain(certfile="client.crt", keyfile="client.key")

# Load the CA certificate to verify the server's certificate
context.load_verify_locations(cafile="ca.crt")

def connect_to_server():
    # Create a socket and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Wrap the socket in an SSL context
        with context.wrap_socket(s, server_side=False, server_hostname='localhost') as ssl_sock:
            ssl_sock.connect(('localhost', 12345))
            
            # Check if server's certificate OU is as expected
            server_cert = ssl_sock.getpeercert()
            # Perform additional checks on server_cert if needed
            
            print(f"Connected to server: {server_cert['subject']}")

            # Toy echo client just for demonstration purposes
            while True:
                msg = input("Enter a message to send to server (type 'exit' to quit): ")
                ssl_sock.sendall(msg.encode('utf-8'))
                if msg.lower() == 'exit':
                    break
if __name__ == "__main__":
    connect_to_server()
