import PySimpleGUI as sg
from rentabilidade import lib


def tela():
    layout1 = [[sg.T('Escolha como deseja calcular o rendimento')],
               [sg.B('Importar Tabela', key='escolha1'), sg.B('Inserir Dados', key='escolha2')],
               [sg.Text('')],
               [sg.Button('Enviar Dados', key='enviarDados1'), sg.Button('Sair', key='Sair1')]
               ]
    layout2 = [[sg.T('Escolha como deseja calcular o rendimento')],
               [sg.B('Importar Tabela', key='escolha1'), sg.B('Inserir Dados', key='escolha2')],
               [sg.Text('Escolha o arquivo CSV', size=(20, 0)), sg.FileBrowse(key='filePath')],
               [sg.Button('Enviar Dados', key='enviarDados2'), sg.Button('Sair', key='Sair2')]
               ]

    layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-')]]

    # janela
    janela = sg.Window("Escolher modo").layout(layout)
    # extrair dados

    i = 0
    layout = 1

    while True:
        event, values = janela.Read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Sair1', 'Sair2'):
            break
        if event == 'escolha1':
            janela[f'-COL{layout}-'].update(visible=False)
            layout = layout + 1 if layout < 2 else 1
            #janela = sg.Window("teste", layout)
            janela[f'-COL{layout}-'].update(visible=True)
            #janela.extend_layout(janela, [[sg.Text('Escolha o arquivo CSV',size=(20,0)), sg.FileBrowse(key='filePath')]])
        if event == 'escolha2':
            janela.extend_layout(janela, [[sg.T('Data'), sg.I(key=f'-IN-{i}-',size=(10,0)),sg.T('Aporte'),sg.I(key=f'-AP-{i}',size=(10,0))]])
            i += 1
        if event == 'enviarDados2' or event == 'enviarDados1':
            break
    janela.close()
    return values

def telaSaida(txt):
    frame_layout = [[sg.T(txt)]]

    layout = [[sg.T('Seus Resultados Foram:')],
             [sg.Frame('', frame_layout, font='Any 12', title_color='blue')],
             [sg.Button('Sair', key='Sair')]]

    while True:
        janela = sg.Window('Teste', layout)
        event, values = janela.Read()
        if event == 'Sair':
            break
        janela.close()

