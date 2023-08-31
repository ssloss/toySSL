import ssl
import socket

# Load server's certificate and key
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Require client certificate
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile="ca.crt")

def verify_client_ou(cert):
    # Extract the subject from the client's certificate
    subject = dict(x[0] for x in cert['subject'])
    # Check if the OU is 'AllowedOU'
    return subject.get('organizationalUnitName') == 'AllowedOU'

def handle_client(conn):
    # Get the client's certificate
    client_cert = conn.getpeercert()
    if not client_cert:
        print('No client certificate provided')
        return
    if not verify_client_ou(client_cert):
        print('Client certificate OU is not allowed')
        return
    print('Client certificate OU is allowed')
    # Handle the client connection here
    # ...

def start_server():
    with socket.socket() as s:
        s.bind(('localhost', 12345))
        s.listen()
        print('Server listening on localhost:12345')
        with context.wrap_socket(s, server_side=True) as ssock:
            conn, addr = ssock.accept()
            with conn:
                print('Connected by', addr)
                handle_client(conn)

if __name__ == "__main__":
    start_server()
