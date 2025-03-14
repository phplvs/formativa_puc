import random
import string


def gerar_senha(tamanho=12, incluir_simbolos=True):

    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


if __name__ == "__main__":
    print("🔐 Gerador de Senhas Seguras 🔐")

    # Commit 3: Garantir que a senha tenha entre 8 e 20 caracteres
    while True:
        try:
            tamanho = int(input("Quantos caracteres na senha? (8-20): "))
            if 8 <= tamanho <= 20:
                break
            else:
                print("⚠️ Digite um número entre 8 e 20.")
        except ValueError:
            print("⚠️ Por favor, insira um número válido.")

    # Commit 2: Adicionar opção de incluir símbolos
    incluir_simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'

    senha = gerar_senha(tamanho, incluir_simbolos)

    # Commit 1: Melhorando a exibição da senha gerada
    print("\n✅ Sua senha segura é:")
    print(f"🔑 {senha}")