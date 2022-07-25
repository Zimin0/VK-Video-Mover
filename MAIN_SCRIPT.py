from tkinter import *
from api_func import main

window = Tk()
window.title('Vk tools')
window.geometry("600x600")
FONT = "Arial 18"
COLOR = "#ffd962"



entry_list = [] # list of inputs fields
def take_text(main): 
    global entry_list
    data = []
    for entr in entry_list: # order =  link, amount, token
        data.append(entr.get())  
    
    value_error,  name, last_name, id  = main(data) 

    ##### ERROR CATCH #####
    errors = {
        0: "Успешно перемещено {} видео.".format(data[1]),
        1: "Вы ввели больше 200.",
        2: "Неправильно набран токен.",
        3: "Неправильная ссылка.",
        4: "Пустое поле."
    }
    l4.configure(text=errors[value_error], font=FONT) 
    #######################
        

def help():
    text = '''1) Чтобы скопировать ссылку - включите английский язык. 
              2) Ваш токен нужно получить по ссылке: https://vkhost.github.io/
              Нажмите VK Admin, далее кнопку разрешить. 
              Скопируйте часть адресной строки от access_token= до &expires_in. 
              Возможны потери в кол-ве перемещаемых видео.'''

    l4.configure(text=text, font="Arial 12") 
    l4.place(x=0, y=300)
    


Label(window, text="Ссылка на альбом:",  font=FONT).place(x=10, y=20) 
e1 = Entry(window)
entry_list.append(e1)
e1.place(x=240, y=28)

Label(window, text="Сколько видео переместить ( <200 ):",  font=FONT).place(x=10, y=60)
e2 = Entry(window)
entry_list.append(e2)
e2.place(x=440, y=68)

Label(window, text="Ваш токен vk:",  font=FONT).place(x=10, y=100)
e3 = Entry(window)
entry_list.append(e3)
e3.place(x=170, y=108)

l4 = Label(window, text="",  font=FONT)
l4.place(x=150, y=400)


start_bt = Button(window, text='Начать', command=lambda: take_text(main), font="Arial 18",bg=COLOR) 
start_bt.place(x=250, y=500)

help_bt = Button(window, text="?", command=help, font="Arial 20", bg=COLOR)
help_bt.place(x=560, y=0)

window.mainloop()
