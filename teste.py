from models.cliente import Cliente
from models.conta import Conta

itachi: Cliente = Cliente('Itachi Uchiha', 'itc.uchiha@gmail.com',
                         '123.456.789-00', '11/11/2011')

goku: Cliente = Cliente('Goku Kakaroto', 'dbz@gmail.com',
                        '987.654.321-00', '12/12/2012')

# print(itachi)
# print(goku)

contaf: Conta = Conta(goku)
contab: Conta = Conta(itachi)

# print(contaf)
# print(contab)

