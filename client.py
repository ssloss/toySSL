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
        with context.wrap_socket(s, server_side=False) as ssl_sock:
            ssl_sock.connect(('localhost', 12345))
            
            # Check if server's certificate OU is as expected
            server_cert = ssl_sock.getpeercert()
            # Perform additional checks on server_cert if needed
            
            print(f"Connected to server: {server_cert['subject']}")
            # Add your client logic here
            # ...

if __name__ == "__main__":
    connect_to_server()
