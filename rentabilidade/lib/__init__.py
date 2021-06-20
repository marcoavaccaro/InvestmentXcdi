import datetime
from workalendar.america import Brazil as Brd
import pandas as pd

cal = Brd()

def importar_csv():
    arq = pd.read_csv(r'C:\Users\marco\PycharmProjects\calcular_dias_uteis\aportes.csv', index_col=False, header=None)
    arqCSV = arq.to_dict()
    list1 = list()
    for c in range(0, len(arqCSV[0])):
        list1.append(arqCSV[0][c].split(';'))
    return list1


def dias_uteis(lst, c=0):
    day, month, year = map(int, lst[c][0].split('/'))
    dataInicio = datetime.date(year, month, day)
    return cal.get_working_days_delta(dataInicio, datetime.datetime.today())


def excluir_dias_irrelevantes(tabela, dias_uteis):
    tabela = tabela.tail(dias_uteis)
    tabela = tabela.reset_index()
    tabela = tabela.drop('index', axis=1)
    return tabela


def extrair_dict(data_frame):
    testex = data_frame.to_dict('list')
    return testex['valor']


def excluir_dias_lista(lst, dias_uteis):
    dias_a_excluir = len(lst) - dias_uteis
    #print(dias_a_excluir)
    for c in range(0, dias_a_excluir):
        del lst[0]
    return lst


def calcular_taxa_equivalente(lista_juros):
    valor_base = valor_referencia = 1
    for c in range(0, len(lista_juros)):
        valor_base = valor_base + (valor_base * lista_juros[c] / 100)
    taxa_equivalente = (valor_base / valor_referencia) - 1
    return taxa_equivalente * 100


def render_investimento(aporte, taxa):
    aporte = int(aporte)
    valor_rendido = aporte + (aporte * taxa / 100)
    return valor_rendido


