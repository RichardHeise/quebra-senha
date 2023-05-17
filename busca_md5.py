import hashlib
import crypt
import time
import itertools

entrada = input()

def busca_dicio():
    with open("dicionario_completo.txt", "r") as dicio:
        for linha in dicio:
            if (hashlib.md5(linha.strip().encode()).hexdigest() == entrada):
                print(linha.strip())
                return 1
    return 0

def busca_passwords():
    with open("1MillionPasswords.txt", "r") as dicio:
        for linha in dicio:
            if (hashlib.md5(linha.strip().encode()).hexdigest() == entrada):
                print(linha.strip())
                return 1
    return 0

def brute_force():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    combinacoes = []
    for i in itertools.product(chars, repeat=5):
        combinacoes = ''.join(i)
        if hashlib.md5(combinacoes.encode()).hexdigest() == entrada:
            print(combinacoes)
            return 1
    return 0


def main():

    print("Buscando em dicionario...")
    tempo_total = time.time()
    result = busca_dicio()
    print(f"Tempo total: {time.time() - tempo_total:.02f} segundos")
    if result: exit(0)
    
    print("Buscando em banco de senhas...")
    tempo_total = time.time()
    result = busca_passwords()
    print(f"Tempo total: {time.time() - tempo_total:.02f} segundos")
    if result: exit(0)

    print("Buscando com força bruta...")
    tempo_total = time.time()
    result = brute_force()
    print(f"Tempo total: {time.time() - tempo_total:.02f} segundos")
    if result: exit(0)

    print("Senha não encontrada")
    exit(1)

if __name__ == "__main__":
    main()
