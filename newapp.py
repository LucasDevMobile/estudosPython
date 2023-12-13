from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [

    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)
while True:
    eventos,valores = janela.read()
    if eventos== sg.WINDOW_CLOSED:
        break
    if eventos=='Entrar':
        if valores['usuario']!='Lucas' or valores['senha'] !='1234':
            print('Usuario ou senha invalidos')
    if eventos=='Entrar':
        if valores['usuario']== 'Lucas' and valores['senha']== '1234':
            print('bem vindo')
            break
            