class ContaCorrente:
    def __init__(self, codigo) -> None:
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self) -> str:
        return f'[>>Código {self.codigo} Saldo {self.saldo}<<]'


conta_do_lucas = ContaCorrente(2069)
print(conta_do_lucas)
conta_do_lucas.deposita(500)
print(conta_do_lucas)

conta_da_dani = ContaCorrente(2069)
print(conta_da_dani)
conta_da_dani.deposita(900)
print(conta_da_dani)

print('=================================================')


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_do_lucas, conta_da_dani]
# print(contas)
# for conta in contas:
#     print(conta)
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])
