import threading
import time

# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: programa desenvolvido para demonstrar condicao de disputa. Metodos p1 e p2, indefinidamente, incrementam
#             a variavel global 'numero'. Como nao hah exclusao mutua, pode haver condicao de corrida.

numero = 0
mutex = threading.Semaphore(1)


# Codigo estah pulando numeros, e repetindo numeros entre threads

# Optei por criar uma função genérica de p1 e p2
def pn(n=""):
    global numero
    while True:
        global mutex
        mutex.acquire()
        numero += 1
        # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
        print(f'P{n}:', numero)
        mutex.release()
        # Troca de time.sleep(1) pra depois pelo motivo explicado em sala (que só uma thread ficaria executando, sendo melhor simular o clock da CPU dessa forma ao usar mutex)
        time.sleep(1)

# def p1():
#     global numero
#     while True:
#         numero += 1
#         time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
#         print('P1:', numero)


# def p2():
#     global numero
#     while True:
#         numero += 1
#         time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
#         print('P2:', numero)


t_p1 = threading.Thread(target=pn, args=("1"))
t_p2 = threading.Thread(target=pn, args=("2"))

print("Carlos André Martins da Silva")

t_p1.start()
t_p2.start()
