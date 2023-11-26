import hashlib

class senha:
    def __init__(self,valor_digitado) -> None:
        self.valor = valor_digitado

    def __repr__(self) -> str:
        return f'A senha digitada é : {self.valor}'
    
    def logar(self) -> str:
        f = open("hash_armazenado.txt", "r")
        hash=f.readline()
        f.close()

        hash_da_senha_digitada = hashlib.sha256(self.valor.encode()).hexdigest()

        if (hash == hash_da_senha_digitada): 
            print('Senha correta')
        
        else:
            print('Senha incorreta')


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

