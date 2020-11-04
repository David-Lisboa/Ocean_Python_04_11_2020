# Importando bibliotecas

# import datetime
#
# data_criada = datetime.date.today()
# print(data_criada)
#
# data_criada = datetime.datetime.now()  # data e hora a partir da zona 0
# print(data_criada)

import datetime as dt  # renomeando a biblioteca datetime para dt

data_criada = dt.date.today()
print(data_criada)

data_criada = dt.datetime.now()  # data e hora a partir da zona 0
print(data_criada)

data_criada = dt.datetime.now()  # data e hora a partir da zona 0
print(data_criada.month)  # mostrar só o mes

agora = dt.datetime.now()
dia_atual = agora.day
mes_atual = agora.month
ano_atual = agora.year

print(f'{}')