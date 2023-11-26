import hashlib

senha = "senha_muito_dificil".encode()
hash= hashlib.sha256(senha).hexdigest()

f = open("hash_armazenado.txt", "w")
f.write(hash)
f.close()