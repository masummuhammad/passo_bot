
import PySimpleGUI as sg
import sqlite3 
import os

conn=sqlite3.connect('DB2.db')
c=conn.cursor()
c.execute('create table if not exists user_data(email text primary key,pass text,event_name text,quantity integer,category integer,priority_display_serial integer,priority1_display_value text,card_holder_fullname text,card_number text,month text,year text,cvv text)')
c.execute('drop table if exists current_user;')
c.execute('create table current_user(email text);')
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

c.execute('select email from user_data;')
try:
    emails=c.fetchall()[0]
except IndexError:
    emails=[]
right_click_menu = ['', ['Copy', 'Paste']]
layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('PassoAPI Bot', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Email'),sg.Text("  "*34),sg.Text("Saved Emails")],
    [sg.InputText(key='email',right_click_menu=right_click_menu),sg.Combo(emails, size=(20, 1),key='combo'),sg.Button('Get',key='get')],
    [sg.Text('Password'),sg.Text('  '*31),sg.Text("Card hloder's fullname")],
    [sg.InputText(key='pass',right_click_menu=right_click_menu),sg.InputText(key="card_holder_fullname",right_click_menu=right_click_menu)],
    [sg.Text('Event name'),sg.Text("  "*29),sg.Text("Card number")],
    [sg.InputText(key='event_name',right_click_menu=right_click_menu),sg.InputText(key='card_number',right_click_menu=right_click_menu)],
    [sg.Text('Quantity'),sg.Text("  "*32),sg.Text("Expiry month")],
    [sg.InputText(key='quantity',right_click_menu=right_click_menu),sg.InputText(key='month',right_click_menu=right_click_menu)],
    [sg.Text('Category'),sg.Text("  "*31),sg.Text("Expiry year")],
    [sg.InputText(key='category',right_click_menu=right_click_menu),sg.InputText(key='year',right_click_menu=right_click_menu)],
    [sg.Text('Priority display serial'),sg.Text("  "*22),sg.Text("CVV")],
    [sg.InputText(key='priority_display_serial',right_click_menu=right_click_menu),sg.InputText(key='cvv',right_click_menu=right_click_menu)],
    
    [sg.Text('Priority1 display value')],
    [sg.InputText(key='priority1_display_value',right_click_menu=right_click_menu)],
    
    
    
    [sg.Text('_' * 80)],
    
    [sg.Button('Start Process',tooltip='Click to start the bot',size=(80,2),key='start')]]

window = sg.Window('Passo-bot', layout,
    default_element_size=(40, 1), grab_anywhere=False,finalize=True)

event, values = window.read()
while True:
    event, values = window.read()   
    
    cl=False
    if event=='get':
        combo_email=values['combo']
        c.execute("select * from user_data where email='%s';"%combo_email)
        data=c.fetchall()[0]
       # ('batunal1415@gmail.com', 'Mustafa3434', 'Galatasaray A.S', 1, 4, 2, '35234', 'can eker', '4526454', '3', '2523', '345')

        window['email'].update(data[0])
        window['pass'].update(data[1])
        window['event_name'].update(data[2])
        window['quantity'].update(data[3])
        window['category'].update(data[4])
        window['priority_display_serial'].update(data[5])
        window['priority1_display_value'].update(data[6])
        window['card_holder_fullname'].update(data[7])
        window['card_number'].update(data[8])
        window['month'].update(data[9])
        window['year'].update(data[10])
        window['cvv'].update(data[11])
        window.refresh()
        
    if event=='start':
        
        for key in values.keys():
            if (values[key]==' ' or values[key]=='') and key!='combo':
                print("Empty input field is not allowed! Try again")
                cl=True
                break
        if cl:
            window.close()
            break
        c.execute("insert into current_user(email) values('%s');"%values['email'])
        c.execute("select * from user_data where email='%s';"%values['email'])

        if len(c.fetchall()):
            c.execute(F"update user_data set pass='{values['pass']}',event_name='{values['event_name']}',quantity={values['quantity']},category={values['category']},priority_display_serial={values['priority_display_serial']},priority1_display_value='{values['priority1_display_value']}',card_holder_fullname='{values['card_holder_fullname']}',card_number='{values['card_number']}',month='{values['month']}',year='{values['year']}',cvv='{values['cvv']}' where email='{values['email']}';")
            conn.commit()
        else:
            query=F"insert into user_data values ('{values['email']}','{values['pass']}','{values['event_name']}',{values['quantity']},{values['category']},{values['priority_display_serial']},'{values['priority1_display_value']}','{values['card_holder_fullname']}','{values['card_number']}','{values['month']}','{values['year']}','{values['cvv']}');"
            c.execute(query)   
            conn.commit()
        window.close()
        sg.Popup('Keep your eyes on the terminal window','To start please click>>>>>> ok <<<<<<')
        
        print(os.system('python3 main.py'))
    ############copy/paste#######
    ##########################
    if event in ('Copy', 'Paste'):
        widget = window.find_element_with_focus().widget
        if event == 'Copy' and widget.select_present():
            text = widget.selection_get()
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(text)
        elif event == 'Paste':
            if widget.select_present():
                widget.delete(sg.tk.SEL_FIRST, sg.tk.SEL_LAST)
            widget.insert(sg.tk.INSERT, window.TKroot.clipboard_get())
    if event == sg.WIN_CLOSED or event == 'Exit':     
      break
    
window.close()


    