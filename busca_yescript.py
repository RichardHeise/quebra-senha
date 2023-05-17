import crypt
import time
import itertools

entrada = input()

salt = entrada.split('$')[0] + '$'
salt += entrada.split('$')[1] + '$'
salt += entrada.split('$')[2] + '$'
salt += entrada.split('$')[3]
hashIn = entrada.split('$')[4].rsplit(':')[0]

hashIn = salt + '$' + hashIn

def busca_dicio():
    with open("dicionario_completo.txt", "r") as dicio:
        for linha in dicio:
            if crypt.crypt(linha.strip(), salt) == hashIn:
                print(linha.strip())
                return 1
    return 0

def busca_passwords():
    with open("1MillionPasswords.txt", "r") as dicio:
        for linha in dicio:
            if crypt.crypt(linha.strip(), salt) == hashIn:
                print(linha.strip())
                return 1
    return 0

def brute_force():
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    combinacoes = []
    for tamanho in range(7,8):
        for i in itertools.product(chars, repeat=tamanho):
            combinacoes = ''.join(i)
            print(combinacoes)
            if crypt.crypt(combinacoes, salt) == hashIn:
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

    print("Buscando com força bruta(vai demorar alguns dias, é sério)...")
    tempo_total = time.time()
    result = brute_force()
    print(f"Tempo total: {time.time() - tempo_total:.02f} segundos")
    if result: exit(0)

    print("Senha não encontrada")
    exit(1)

if __name__ == "__main__":
    main()
