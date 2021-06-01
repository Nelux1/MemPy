
import PySimpleGUI as sg

def layout2():
# if want to split, can't add newline after + to do it
 layout = [[sg.Button(i) for i in range(4)]] + [[sg.OK('Pista')]]

 window = sg.Window('Generated Layouts', layout)

 event, values = window.read()

 print(event, values)
 window.close()

layout2()