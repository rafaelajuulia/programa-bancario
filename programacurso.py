class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(('Depósito', valor))

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            self.extrato.append(('Saque', -valor))

    def visualizar_extrato(self):
        print(f'Extrato de {self.titular}:')
        for operacao, valor in self.extrato:
            print(f'{operacao}: {valor}')
        print(f'Saldo atual: {self.saldo}')

# Exemplo de uso
conta = ContaBancaria('João')
conta.depositar(1000)
conta.sacar(200)
conta.visualizar_extrato()
