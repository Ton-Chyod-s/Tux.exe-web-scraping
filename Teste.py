import PySimpleGUI as sg


themes = sg.theme_list()
selected_theme = 'Reds'
current_them = sg.theme()
sg.theme(selected_theme)

layout = [
        [sg.T('User Setting:')],
        [sg.Text('Select Theme:'), 
        sg.Combo(values=themes, default_value=selected_theme, size=(15, 1), enable_events=True, key='select_theme')],
        [sg.I('this is input')], 
        [sg.B('Hello'), sg.Button(' about ', key='about')]
    ]

window = sg.Window('', layout=layout)

while True:
    e, v= window.read()
    if e is None:
        break
        
    elif e == 'select_theme':
        selected_theme = v['select_theme']
        window.close()
        sg.theme('selected_theme')
        layout = [[sg.T('User Setting:')],[sg.Text('Select Theme:'), sg.Combo(values=themes,default_value=selected_theme, size=(15, 1), enable_events=True, key='select_theme')],[sg.I('this is input')], [sg.B('Hello'), sg.Button(' about ', key='about')]]
        window = sg.Window('',layout)


