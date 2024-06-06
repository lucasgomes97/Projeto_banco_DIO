from models.cliente import Cliente
from models.conta import Conta

jessica: Cliente = Cliente('Jessica Jones', 'jaacaboujessica@gmail.com', '123.125.125-99', '02/08/2000')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '234.654.852-88', '08/09/1898')

print(jessica)
print(angelina)

contaf: Conta = Conta(jessica)
contaa: Conta = Conta(angelina)

print(contaf)
print(contaa)