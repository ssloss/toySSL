#!/bin/bash

##############################
# Create Root CA Certificate #
##############################

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

##############################
# Create Client Certificates #
##############################
# Generate private key for the first client
openssl genpkey -algorithm RSA -out client1.key

# Create Certificate Signing Request (CSR) for the first client
openssl req -new -key client1.key -out client1.csr -subj "/CN=Client1/O=My Organization/OU=AllowedOU/C=US"

# Sign the first client CSR with the root CA key
openssl x509 -req -in client1.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client1.crt

# Generate private key for the second client
openssl genpkey -algorithm RSA -out client2.key

# Create Certificate Signing Request (CSR) for the second client
openssl req -new -key client2.key -out client2.csr -subj "/CN=Client2/O=My Organization/OU=WrongOU/C=US"

# Sign the second client CSR with the root CA key
openssl x509 -req -in client2.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client2.crt

echo "Certificates generated successfully."