import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
<<<<<<< Updated upstream
    tamanho = int(input("Quantos caracteres na senha? "))
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
=======
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
    # 🔽🔽 Adicionando a cópia automática para o clipboard 🔽🔽
    pyperclip.copy(senha)
    print("\n📋 A senha foi copiada para a área de transferência!")

    # Commit 1: Melhorando a exibição da senha gerada
    print("\n✅ Sua senha segura é:")
    print(f"🔑 {senha}")

    # Pergunta se o usuário quer gerar outra senha
    continuar = input("Deseja gerar outra senha? (s/n): ").strip().lower()
    if continuar != 's':
        print("👋 Obrigado por usar o gerador de senhas!")
>>>>>>> Stashed changes
