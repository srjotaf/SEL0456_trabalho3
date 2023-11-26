import hashlib

class senha:
    def __init__(self,valor_digitado) -> None:
        self.valor = valor_digitado
        self.correta = False

    def __repr__(self):
        # return f'A senha digitada é : {self.valor}'
        pass

    def logar(self) -> None:
        f = open("hash_armazenado.txt", "r")
        hash=f.readline()
        f.close()

        hash_da_senha_digitada = hashlib.sha256(self.valor.encode()).hexdigest()

        if (hash == hash_da_senha_digitada): 
            # print('Senha correta')
            self.correta = True
        
        else:
            # print('Senha incorreta')
            pass


f = open("senha_errada.txt", "r")
temp = f.readline()
f.close()

senha1 = senha(temp)
print(senha1)
senha1.logar()

f = open("senha_correta.txt", "r")
temp = f.readline()
f.close()

senha2 = senha(temp)
print(senha2)
senha2.logar()

