import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho = int(input("Quantos caracteres na senha? "))
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
