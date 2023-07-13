import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Escolha o tamanho da senha (8 ou 16): "))

if tamanho == 8 or tamanho == 16:
    senha = gerar_senha(tamanho)
    print(f"Senha de {tamanho} dígitos: {senha}")
else:
    print("Tamanho inválido. Escolha entre 8 ou 16 dígitos.")
