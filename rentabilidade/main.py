import urllib.request
import pandas as pd
import lib

#teste de commit
link = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

lista_de_aportes = lib.importar_csv()
dias_uteis_periodo = lib.dias_uteis(lib.importar_csv())


f = urllib.request.urlopen(link)
myfile = pd.read_json(f.read())
tabela = lib.excluir_dias_irrelevantes(myfile, dias_uteis_periodo)
lista_juros = lib.extrair_dict(tabela)


aportes = 0
valor_final = 0
for c in range(0, len(lista_de_aportes)):
    diasUteis = lib.dias_uteis(lista_de_aportes, c)
    listaDeJurosFiltrado = lib.excluir_dias_lista(lista_juros, diasUteis)
    aportes = aportes+int(lista_de_aportes[c][1])
    valor_final = valor_final + lib.render_investimento(lista_de_aportes[c][1], lib.calcular_taxa_equivalente(listaDeJurosFiltrado))

print(f'Com os seus investimentos que totalizaram R${aportes},00 desde {lista_de_aportes[0][0]}, hoje você teria R${valor_final:.2f} se tivesse investido no CDI.\n'
      f'Uma rentabilidade de R${valor_final-aportes:.2f} ou {(valor_final/aportes-1)*100:.3f}% no período')

