class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
    
    def __str__(self):
        
        return f'O titular da conta é {self.titular} e o seu saldo é de {self.saldo} e seu estado esta como {self.ativo}'
    def switch_conta(self):
        self.ativo = not self.ativo

Conta1 = ContaBancaria("João", '100,95')
Conta2 = ContaBancaria("Julia", "200,21")
Conta1.switch_conta()


print(Conta1)
print(Conta2)
