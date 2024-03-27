from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta
from utils.helper import formata_float_str_moeda

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('========================================')
    print('================= ATM ==================')
    print('============== BankFacil ===============')
    print('========================================')
    print('============ Menu Principal ============')
    print('========================================')

    print('==     Selecione uma opção no menu:   ==')
    print('==          1 - Criar conta           ==')
    print('==         2 - Efetuar saque          ==')
    print('==        3 - Efetuar depósito        ==')
    print('==     4 - Efetuar transferência      ==')
    print('==        5 - Listar contas           ==')
    print('==       6 - Sair do sistema          ==')
    print('========================================')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_tranferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit()
    else:
        print(f'Você inseriu uma opção inválida.')
        print(f'Por favor insira uma opção entre 1 e 6.')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os seguintes dados do cliente: ')

    nome: str = input('Nome Completo: ')
    nome = nome.title()
    email: str = input('E-mail: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data de nascimento (dd/mm/aaaa): ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('--------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input(f'Informe o valor que deseja sacar entre R$ 10 '
                                       f'e R$ {formata_float_str_moeda(conta.saldo_total)}: '))

            conta.sacar(valor)

        else:
            print(f'Você digitou um número de conta inexistente ({numero}).')
            print('Você será redirecionado ao Menu Principal.')
    else:
        print('Ainda não existem contas cadastradas no sistema!')
        print("Para criar uma conta selecione a 'Opção (1)' no Menu Principal. ")
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input(f'Informe o valor que deseja depositar: '))

            conta.depositar(valor)
        else:
            print(f'Você digitou um número de conta inexistente ({numero}).')
            print('Você será redirecionado ao Menu Principal.')
    else:
        print('Ainda não existem contas cadastradas no sistema!')
        print("Para criar uma conta selecione a 'Opção (1)' no Menu Principal. ")
    sleep(2)
    menu()


def efetuar_tranferencia() -> None:
    if len(contas) > 0:

        numero_o: int = int(input('Informe o número da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input(f'Informe o número da contade destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input(f'Informe o valor que deseja tranferir: '))

                conta_o.transferir(conta_d, valor)
            else:
                print(f'foi informado um número inexistente para '
                      f'a conta de destino ({numero_d}).')
                print('Você será redirecionado ao Menu Principal.')
        else:
            print(f'Você digitou um número de conta inexistente ({numero_o}).')
            print('Você será redirecionado ao Menu Principal.')
    else:
        print('Ainda não existem contas cadastradas no sistema!')
        print("Para criar uma conta selecione a 'Opção (1)' no Menu Principal. ")
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('========================')
        print('== Listagem de Contas ==')
        print('========================')

        for conta in contas:
            print(conta)
            print('========================')
            sleep(1)
    else:
        print('Ainda não existem contas cadastradas no sistema!')
        print("Para criar uma conta selecione a 'Opção (1)' no Menu Principal. ")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
