#!/bin/bash

# Create Root CA Certificate

# Generate private key for root CA
openssl genpkey -algorithm RSA -out ca.key

# Create self-signed root CA certificate
openssl req -new -x509 -key ca.key -out ca.crt -subj "/CN=Root CA/O=My Organization/C=US"

# Create Server Certificate

# Generate private key for the server
openssl genpkey -algorithm RSA -out server.key

# Create Certificate Signing Request (CSR) for the server
openssl req -new -key server.key -out server.csr -subj "/CN=localhost/O=My Organization/C=US"

# Sign the server CSR with the root CA key
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt

# Create Client Certificate with OU='AllowedOU'

# Generate private key for the client
openssl genpkey -algorithm RSA -out client.key

# Create Certificate Signing Request (CSR) for the client
openssl req -new -key client.key -out client.csr -subj "/CN=Client/O=My Organization/OU=AllowedOU/C=US"

# Sign the client CSR with the root CA key
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt

echo "Certificates generated successfully."
