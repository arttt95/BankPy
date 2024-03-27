from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:

    contador: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.contador
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.contador += 1

    def __str__(self: object) -> str:
        return (f'Número da Conta: {self.numero}\n'
                f'Cliente: {self.cliente.nome}\n'
                f'Saldo Total: {formata_float_str_moeda(self.saldo_total)}')

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!')
            print(f'Seu novo saldo é de {formata_float_str_moeda(self.saldo)} '
                  f'e o saldo + limite é de {formata_float_str_moeda(self.saldo_total)}.')
        else:
            print(f'O valor precisa ser maior que R$ 0,00 para realizar um depósito.')

    def sacar(self: object, valor: float) -> None:
        if 10 < valor <= self.saldo_total:
            if valor <= self.saldo:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite += restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print(f'Saque realizado com sucesso.')
            print(f'Seu saldo atual é de R$ {formata_float_str_moeda(self.saldo)} '
                  f'e saldo + limite é de R$ {formata_float_str_moeda(self.saldo_total)}')
        else:
            print(f'O valor para saque precisa ser maior que R$ 10,00 '
                  f'e menor ou igual a {formata_float_str_moeda(self.saldo_total)}.')

    def transferir(self: object, conta_destino: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saldo_total = self._calcula_saldo_total
                conta_destino.saldo += valor
                conta_destino.saldo_total = conta_destino._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite += restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                conta_destino.saldo += valor
                conta_destino.saldo_total = conta_destino._calcula_saldo_total
            print(f'Transferência realizada com sucesso.')
            print(f'Seu saldo atual é de R$ {formata_float_str_moeda(self.saldo)} '
                  f'e saldo + limite é de R$ {self.saldo_total}')
        else:
            print(f'O valor para transferência precisa ser maior que R$ 0,00 '
                  f'e menor ou igual a {formata_float_str_moeda(self.saldo_total)}.')
