""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    | $  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\  $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @                      ELIAS KARIMZADEH                            @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @              GitHub: github.com/EliasKarimzadeh                  @ \ $ |
    | $ \ @             Linkdin: in/elias-karimzadeh-a7a9b8283               @ / $ |
    | $ / @            Instagram : instagram.com/elyaskarymzade              @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |        
    | $ \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ $ |
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|"""

import tkinter as tk
from tkinter import ttk

Calculator = tk.Tk()
Calculator.title('Calculator')

lbl_qetion = tk.Label(
    master=Calculator,
    width=20,
    text=''
)
lbl_qetion.grid(row=0 , column=0, columnspan=4)


lbl_anser = tk.Label(
    master=Calculator,
    text='Powwer by Elias Karimzadeh'
)
lbl_anser.grid(row=1 , column=0, columnspan=4)


############ fanctions ##############
def back(exite):
    if len(exite) > 0:
        return exite[:-1]     
    
def check_point():
    for a in lbl_qetion['text'][::-1]:
        if a == '.':
            return False
        elif a in ['+','-','*','/']:
            return True
        else:
            return True     
         
def calc():
    lbl_anser['text'] = eval(lbl_qetion['text'])

def input_user(input_num):
    if lbl_qetion['text'] == '0':
        lbl_qetion['text'] =  ''
        
    if input_num in ['+','-','*','/'] :
        if lbl_qetion['text'][-1:] in ['+','-','*','/']:
            chang_argument  = back(lbl_qetion['text'])
            chang_argument += input_num
            lbl_qetion['text'] = chang_argument
            
        elif len(lbl_qetion['text']) == 0 :
            pass
        else:
            lbl_qetion['text']+= input_num 
                
    elif input_num == 'c':
        lbl_qetion['text'] = ''
        
    elif input_num == 'Back':
        back_str = back(lbl_qetion['text'])
        lbl_qetion['text'] = back_str
        
    elif input_num == '=':
        calc()
    
    elif input_num =='.':
        if check_point() == True :
            lbl_qetion['text']+= input_num  
        else:
            pass
    
    else:
        lbl_qetion['text']+= input_num
        
         
############ button ###########
dict_list_button = [
     {'text' : 'C',
     'command' : lambda: input_user('c'),
     'columnspan': 1,
     'rowspan': 1,}

     ,
     {'text' : '*',
     'command' : lambda: input_user('*'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '/',
     'command' : lambda: input_user('/'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : 'Back',
     'command' : lambda: input_user('Back'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '1',
     'command' : lambda: input_user('1'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '2',
     'command' : lambda: input_user('2'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '3',
     'command' : lambda: input_user('3'),
     'columnspan': 1,
     'rowspan': 1,} 
     ,
     {'text' : '+',
     'command' : lambda: input_user('+'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '4',
     'command' : lambda: input_user('4'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '5',
     'command' : lambda: input_user('5'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '6',
     'command' : lambda: input_user('6'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '-',
     'command' : lambda: input_user('-'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '7',
     'command' : lambda: input_user('7'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '8',
     'command' : lambda: input_user('8'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '9',
     'command' : lambda: input_user('9'),
     'columnspan': 1,
     'rowspan': 1,}
     ,
     {'text' : '=',
     'command' : lambda: input_user('='),
     'columnspan': 1,
     'rowspan': 2,}
     ,
    {'text' : '.',
     'command' : lambda: input_user('.'),
     'columnspan': 1,
     'rowspan': 1,}
    ,
     {'text' : '0',
     'command' : lambda: input_user('0'),
     'columnspan': 2,
     'rowspan': 1,}
]

list_button_save = []

for btn in dict_list_button:
    btnm = ttk.Button(
        master=Calculator,
        text= btn['text'],
        command=btn['command']
    )
    list_button_save.append(btnm)

for index,gridbtn in enumerate(list_button_save):
    gridbtn.grid(
        row=(index//4)+2,
        column=index%4,
        columnspan=dict_list_button[index]['columnspan'],
        rowspan=dict_list_button[index]['rowspan'],
        ipadx=1,
        ipady=10,
        sticky='wens',
    )
 
Calculator.mainloop()