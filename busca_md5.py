import hashlib
import time
import itertools

# Obter entrada do usuário
entrada = input()
tempo_dicio = tempo_banco = tempo_brute = 0

# Função para buscar no dicionário
def busca_dicio():
    with open("dicionario_completo.txt", "r") as dicio:
        for linha in dicio:
            # Remover espaços em branco no início e no final da linha
            stripped_line = linha.strip()
            # Calcular o hash MD5 da linha
            hashed_line = hashlib.md5(stripped_line.encode()).hexdigest()
            # Verificar se o hash calculado é igual à entrada fornecida
            if hashed_line == entrada:
                print(stripped_line)
                return True
    return False

# Função para buscar em banco de senhas
def busca_passwords():
    with open("1MillionPasswords.txt", "r") as dicio:
        for linha in dicio:
            # Remover espaços em branco no início e no final da linha
            stripped_line = linha.strip()
            # Calcular o hash MD5 da linha
            hashed_line = hashlib.md5(stripped_line.encode()).hexdigest()
            # Verificar se o hash calculado é igual à entrada fornecida
            if hashed_line == entrada:
                print(stripped_line)
                return True
    return False

# Função para busca por força bruta
def brute_force():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    max_length = 5
    for tamanho in range(1, max_length+1):
        for combination in itertools.product(chars, repeat=tamanho):
            # Gerar a combinação atual
            combinacoes = ''.join(combination)
            # Calcular o hash MD5 da combinação atual
            hashed_comb = hashlib.md5(combinacoes.encode()).hexdigest()
            # Verificar se o hash calculado é igual à entrada fornecida
            if hashed_comb == entrada:
                print(combinacoes)
                return True
    return False

def main():

    # Buscar no dicionário
    print("Buscando em dicionario...")
    tempo_dicio = time.time()
    result = busca_dicio()
    tempo_dicio = time.time() - tempo_dicio
    print(f"Tempo dicionário: {tempo_dicio:.02f} segundos")
    print(f"Tempo total: {tempo_dicio:.02f} segundos")
    if result:
        exit(0)

    # Buscar em banco de senhas
    print("Buscando em banco de senhas...")
    tempo_banco = time.time()
    result = busca_passwords()
    tempo_banco = time.time() - tempo_banco
    print(f"Tempo banco de senhas: {tempo_banco:.02f} segundos")
    print(f"Tempo total: {tempo_dicio + tempo_banco:.02f} segundos")
    if result:
        exit(0)

    # Buscar por força bruta
    print("Buscando com força bruta...")
    tempo_brute = time.time()
    result = brute_force()
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
