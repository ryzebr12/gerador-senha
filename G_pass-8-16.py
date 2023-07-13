import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_8 = 8
tamanho_16 = 16

senha_8 = gerar_senha(tamanho_8)
senha_16 = gerar_senha(tamanho_16)

print(f"Senha de 8 dígitos: {senha_8}")
print(f"Senha de 16 dígitos: {senha_16}")
