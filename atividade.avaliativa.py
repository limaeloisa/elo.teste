class ContaBancaria:
    def _init_(self, nome, numero_conta, tipo_conta, deposito_inicial=0):
        # Inicializa o saldo com o depósito inicial, se for válido, ou com zero
        self.nome = nome
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        if deposito_inicial >= 100:
            self.saldo = deposito_inicial
            print(f"Conta criada para {self.nome} com depósito inicial de R$ {deposito_inicial}.")
        elif deposito_inicial > 0:
            print("O depósito inicial deve ser maior ou igual a R$ 100.")
            self.saldo = 0
        else:
            self.saldo = 0

    # Métodos get e set para cada atributo
    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getNumero(self):
        return self.numero_conta

    def setNumero(self, numero):
        self.numero_conta = numero

    def getTipoConta(self):
        return self.tipo_conta

    def setTipoConta(self, tipo_conta):
        self.tipo_conta = tipo_conta

    def verificarSituacao(self):
        if self.saldo > 0:
            print(f"O saldo da conta {self.numero_conta} está positivo.")
        elif self.saldo < 0:
            print(f"O saldo da conta {self.numero_conta} está negativo.")
        else:
            print(f"A conta {self.numero_conta} está sem saldo.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
            print(f"Saldo após saque: R$ {self.saldo}")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido.")

    def mostrar_saldo(self):
        print(f"O saldo atual da conta número {self.numero_conta} é: R$ {self.saldo}")


# Criando uma conta com os dados fornecidos pelo usuário
nome_titular = input("Digite o nome do titular da conta: ")
numero_conta = input("Digite o número da conta com 10 dígitos: ")
tipo_conta = input("Digite o tipo da conta (ex: Corrente, Poupança): ")

resposta = input("Deseja fazer um depósito inicial? (sim ou não): ")

if resposta == 'sim':
    print("O valor mínimo para o primeiro depósito é de 100 (CEM) reais.")
    valor_inicial = float(input("Sabendo o valor mínimo, deposite o seu valor inicial: "))
    conta = ContaBancaria(nome_titular, numero_conta, tipo_conta, valor_inicial)
elif resposta == 'não':
    print("Conta criada sem depósito inicial.")
    conta = ContaBancaria(nome_titular, numero_conta, tipo_conta)
else:
    print("Erro no sistema, por favor tente novamente!")
    exit()

# Realizando depósito
valor_deposito = float(input("Digite o valor para depósito: "))
conta.depositar(valor_deposito)
print()

# Fazendo saque
valor_saque = float(input("Digite o valor para saque: "))
conta.sacar(valor_saque)
print()

# Mostrando saldo final
conta.mostrar_saldo()

# Verificando situação da conta
conta.verificarSituacao()

# Alterando o tipo de conta
novo_tipo_conta = input("Digite o novo tipo de conta: ")
conta.setTipoConta(novo_tipo_conta)

# Exibindo o novo tipo de conta
print(f"O novo tipo de conta é: {conta.getTipoConta()}")

#Alunos: Maria Eloisa De Lima Silva e Saul Vitorio Batista Reis Do Nascimento
