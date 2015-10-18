# CLASE 7
# Autor: Abdel G. Martinez L.

import Cliente as c

if __name__ == '__main__':
    # Creamos un cliente
    Juan = c.Cliente("Juan Perez")
    # Dia 1: el cliente abre su cuenta corriente
    Juan.establecer_balance(500)
    # Dia 2: el cliente deposita $1500
    Juan.depositar(1500)
    print("Dia 1: " + Juan.nombre + ", tiene $" + str(Juan.mostrar_balance()) + " de saldo.")
    # Dia 3: el cliente deposita $670
    Juan.depositar(670)
    print("Dia 2: " + Juan.nombre + ", tiene $" + str(Juan.mostrar_balance()) + " de saldo.")
    # Dia 4: el cliente retira $250
    Juan.retirar(500)
    print("Dia 3: " + Juan.nombre + ", tiene $" + str(Juan.mostrar_balance()) + " de saldo.")
