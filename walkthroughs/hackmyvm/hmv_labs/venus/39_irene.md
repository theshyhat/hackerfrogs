# Target user
adela
# Method of solve
Decrypt a encoded file using a private key
# Key command
openssl pkeyutl -decrypt -inkey id_rsa.pem -in pass.enc -out pass.txt
