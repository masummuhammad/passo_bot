import PySimpleGUI as sg
layout=[
        [sg.Text('Email',justification='center')],
        [sg.Input(justification='center',key='email')],
        [sg.Text('Password',justification='center')],
        [sg.Input(justification='center',key='pass')],
    
        [sg.Text('Id Number')],
        [sg.Input(key='id')],
      
        [sg.Text('Fullname')],
        [sg.Input(key='name')],
        [sg.Text('Card number')],
        [sg.Input(key='card')],
        [sg.OptionMenu(default_value=1,values=(1,2,3,4,5,6,7,8,9,10,11,12),key='month'),sg.OptionMenu(default_value=2023,values=(2024,2025,2026,2027,2028,2029,2030,2031,2032,2033),key='year')],
        
        [sg.Input('VCC',size=(20,10),key='vcc'),sg.Button('Add',key='addcard')],
        

]

second_layout=[
        [sg.Text('Event Name')],
        [sg.Input(key='event_name')],
        [sg.Text('Category')],
        [sg.Input(key='category')],
        [sg.Text('Quantity'),sg.OptionMenu(default_value=1,values=(1,2,3,4,5),key='qty')],
        [sg.Button('Start process',key='start')],
        [sg.Output(size=(90,25))]

]

