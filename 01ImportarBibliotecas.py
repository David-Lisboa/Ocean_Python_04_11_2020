# Importando bibliotecas

import datetime

data_criada = datetime.date.today()
print(data_criada)

data_criada = datetime.datetime.now()  # data e hora a partir da zona 0
print(data_criada)

from datetime import datetime as dt  # renomeando a biblioteca datetime para dt

data_criada = dt.today()
print(data_criada)

data_criada = dt.now()  # data e hora a partir da zona 0
print(data_criada)

data_criada = dt.now()  # data e hora a partir da zona 0
print(data_criada.month)  # mostrar só o mes

agora = dt.now()
dia_atual = agora.day
mes_atual = agora.month
ano_atual = agora.year

print(f"{dia_atual}/{mes_atual}/{ano_atual}")
print(agora.timetz())
print(agora.strftime('%d/%m/%y - %a'))
print(f'{1:04d}-{2941:04d}-{33:04d}')   # colocar ou tirar zeros da formatação
