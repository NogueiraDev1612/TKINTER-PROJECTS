from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image #importamos para abrir abrir umagem como backgroud
import pyperclip

##Funções

#Essa função chama o selecionador de cores do windows
def obter_cor1():
    cor1 = askcolor()                      #askcolor() chama o seletor de cores do dispositivo, seleciona uma cor e passa para a variavel: cor1
    hex_cor1 = cor1[1].upper()                          #selecina o valor retornado em hex e armazena na variavel ; upper retorna as strings fornecidas como maisculas ;
    label_cor1['bg'] = hex_cor1                         #adicionamos um o valor de cores em label_1, atualizando o backgroud da label

    info_cor1.delete(0,END)                             #apagamos as informações no espaço Entry 1
    info_cor1.insert(0,hex_cor1)                        #inserimos as informações de cores no espaço Entry 1

    pyperclip.copy(hex_cor1)

    info_cor1['bg'] = "#93FE83"                         #transformar o backgroud de entry 1 em verde
    info_cor2['bg'] = "#d9d9d9"                          #transforma o backgroud de entry 2 em cinza
    info_cor3['bg'] = "#d9d9d9"                          #transforma o backgroud de entry e em cinza


def obter_cor2():
    cor2 = askcolor()                      #askcolor() chama o seletor de cores do dispositivo, seleciona uma cor e passa para a variavel: cor1
    hex_cor2 = cor2[1].upper()                          #selecina o valor retornado em hex e armazena na variavel ; upper retorna as strings fornecidas como maisculas ;
    label_cor2['bg'] = hex_cor2                         #adicionamos um o valor de cores em label_1, atualizando o backgroud da label

    info_cor2.delete(0,END)                             #apagamos as informações no espaço Entry 1
    info_cor2.insert(0,hex_cor2)                        #inserimos as informações de cores no espaço Entry 1

    pyperclip.copy(hex_cor2)

    info_cor1['bg'] = "#d9d9d9"                         #transformar o backgroud de entry 1 em cinza
    info_cor2['bg'] = "#93FE83"                          #transforma o backgroud de entry 2 em verde
    info_cor3['bg'] = "#d9d9d9"                          #transforma o backgroud de entry e em cinza



def obter_cor3():
    cor3 = askcolor()                      #askcolor() chama o seletor de cores do dispositivo, seleciona uma cor e passa para a variavel: cor1
    hex_cor3 = cor3[1].upper()                          #selecina o valor retornado em hex e armazena na variavel ; upper retorna as strings fornecidas como maisculas ;
    label_cor3['bg'] = hex_cor3                         #adicionamos um o valor de cores em label_1, atualizando o backgroud da label

    info_cor3.delete(0,END)                             #apagamos as informações no espaço Entry 1
    info_cor3.insert(0,hex_cor3)                        #inserimos as informações de cores no espaço Entry 1


    pyperclip.copy(hex_cor3)

    info_cor1['bg'] = "#d9d9d9"                        #transformar o backgroud de entry 1 em cinza
    info_cor2['bg'] = "#d9d9d9"                          #transforma o backgroud de entry 2 em cinza
    info_cor3['bg'] = "#93FE83"                          #transforma o backgroud de entry e em verde










master = Tk()

master.geometry('767x485+402+216')                             #Posiciona a tela
master.title('Selecionador de Cores')
#master.iconbitmap(default-"path")                             #muda o icone
master.resizable(width=True,height=True )                      #estudar o que esse comando faz

#importar imagens
img_backgroud = ImageTk.PhotoImage(Image.open("fundo.png"))


###Label - chama imagens ou texto

#importa imagem de fundo na janela principal,
label_backgroud = Label(master, image=img_backgroud)
label_backgroud.pack()

#cor 1 - onde fica a cor selecionada pelo usuario
label_cor1 = Label(master, bg='#d9d9d9')
label_cor1.place(width=668, height=104, x=9, y=13)

#cor 2 - onde fica a cor selecionada pelo usuario
label_cor2 = Label(master, bg='#d9d9d9')
label_cor2.place(width=668, height=102, x=9, y=192)

#cor 3 - onde fica a cor selecionada pelo usuario
label_cor3 = Label(master, bg='#d9d9d9')
label_cor3.place(width=668, height=104, x=9, y=369)




##Botões

#botão 1
bt1 = Button(master,text='COR 1',command=obter_cor1)
bt1.place(width=62, height=59, x=693, y=35)

#botão 2
bt2 = Button(master,text='COR 2',command=obter_cor2)
bt2.place(width=60, height=56, x=694, y=215)

#botão 3
bt3 = Button(master,text='COR 3',command=obter_cor3)
bt3.place(width=63, height=59, x=691, y=389)


#Caixas de entrada

#retorna informação 1
info_cor1 = Entry(master, bg="#e5e5e9", justify="center", font=('Calibri',19))
info_cor1.place(width=403, height=29, x=103, y=50)

#retorna informação 2
info_cor2 = Entry(master, bg="#e5e5e9", justify="center", font=('Calibri',19))
info_cor2.place(width=403, height=29, x=103, y=230)

#retorna informação 3
info_cor3 = Entry(master, bg="#e5e5e9", justify="center", font=('Calibri',19))
info_cor3.place(width=403, height=29, x=103, y=410)














'''#metodo para medidas nas telas
master.bind('<Button-1>', position.inicio_place)
master.bind('<ButtonRelease-1>', lambda arg: position.fim_place(arg, master))
master.bind('<*>Button-2>', lambda arg: position.para_geometry(master))'''

master.mainloop()
