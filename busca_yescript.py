import crypt
import time
import itertools

tempo_dicio = tempo_banco = tempo_brute = 0

# Função para obter o salt e o hash da entrada fornecida
def get_salt_and_hash(entrada):
    parts = entrada.split('$')
    salt = '$'.join(parts[:4])
    hashIn = parts[4].rsplit(':')[0]
    hashIn = salt + '$' + hashIn
    return salt, hashIn

# Função para buscar no dicionário
def busca_dicio(salt, hashIn):
    with open("dicionario_completo.txt", "r") as dicio:
        for linha in dicio:
            # Remover espaços em branco no início e no final da linha
            stripped_line = linha.strip()
            # Verificar se a linha criptografada corresponde ao hash da entrada
            if crypt.crypt(stripped_line, salt) == hashIn:
                print(stripped_line)
                return True
    return False

# Função para buscar em banco de senhas
def busca_passwords(salt, hashIn):
    with open("1MillionPasswords.txt", "r") as dicio:
        for linha in dicio:
            # Remover espaços em branco no início e no final da linha
            stripped_line = linha.strip()
            # Verificar se a linha criptografada corresponde ao hash da entrada
            if crypt.crypt(stripped_line, salt) == hashIn:
                print(stripped_line)
                return True
    return False

# Função para busca por força bruta
def brute_force(salt, hashIn):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    max_length = 7
    for tamanho in range(1, max_length+1):
        for combination in itertools.product(chars, repeat=tamanho):
            # Gerar a combinação atual
            combinacoes = ''.join(combination)
            # Verificar se a combinação criptografada corresponde ao hash da entrada
            if crypt.crypt(combinacoes, salt) == hashIn:
                print(combinacoes)
                return True
    return False

def main():
    # Le entrada
    entrada = input()
    salt, hashIn = get_salt_and_hash(entrada)

    # Buscar no dicionário
    print("Buscando em dicionario...")
    tempo_dicio = time.time()
    result = busca_dicio(salt, hashIn)
    tempo_dicio = time.time() - tempo_dicio
    print(f"Tempo dicionário: {tempo_dicio:.02f} segundos")
    print(f"Tempo total: {tempo_dicio:.02f} segundos")
    if result:
        exit(0)

    # Buscar em banco de senhas
    print("Buscando em banco de senhas...")
    tempo_banco = time.time()
    result = busca_passwords(salt, hashIn)
    tempo_banco = time.time() - tempo_banco
    print(f"Tempo banco de senhas: {tempo_banco:.02f} segundos")
    print(f"Tempo total: {tempo_dicio + tempo_banco:.02f} segundos")
    if result:
        exit(0)

    # Buscar por força bruta
    print("Buscando com força bruta (vai demorar alguns dias, é sério)...")
    tempo_brute = time.time()
    result = brute_force(salt, hashIn)
    tempo_brute = time.time() - tempo_brute
    print(f"Tempo força bruta: {tempo_brute:.02f} segundos")
    print(f"Tempo total: {tempo_dicio + tempo_banco + tempo_brute:.02f} segundos")
    if result:
        exit(0)

    # Se a senha não for encontrada
    print("Senha não encontrada")
    exit(1)

if __name__ == "__main__":
    main()
