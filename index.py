#bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

#Criação da janela
jan = Tk() 

#Nome da janela
jan.title('Acess Painel') 

#Dimensões
jan.geometry('600x300') 

#Cor da janela
jan.configure(background='white') 

#Com isso faz com que a janela não possa ser alterada de tamanho
jan.resizable(width=False, height=False) 

#Cria uma transparencia na janela
jan.attributes('-alpha', 0.9)

#Carrega o icone da janela 
jan.iconbitmap(default='icons\LogoIcon.ico')

#Carregando imagem
logo = PhotoImage(file='icons\logo.png')

#Criação do frame esquerdo para dividir a janela (esquerda logo)
LeftFrame = Frame (jan, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

#Criação do frame direito para dividir a janela (direta conteudo)
RightFrame = Frame(jan, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

#Definição do local da imagem 
LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)

#Definição do local da textbox Username
UserLabel = Label(RightFrame, text='Username:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg="White")
UserLabel.place(x=5, y=100)

#Definição do local do campo que o usuario vai digitar
UserEntry = Entry(RightFrame, width=32)
UserEntry.place(x=150,y=115)

#Definição do local da textbox Senha
PassLabel = Label(RightFrame, text='Password:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White' )
PassLabel.place(x=5,y=150)

#Definição do local do campo que o usuario vai digitar/Função show retorna * no lugar do texto
PassEntry = Entry(RightFrame,width=34, show='*')
PassEntry.place(x=140,y=165)

#Def para verificar no banco e logar
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User,Pass))
    print('Selecionou')
    #Fetchone - Apenas um / Fetchall - Todos / Fetchmany - Varios
    VerifyLogin = DataBase.cursor.fetchone() 
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title='Login Info', message='Acesso Confirmado. Bem Vindo!')
    #Manipula os erros 
    except: 
        messagebox.showinfo(title='Login Info', message='Acesso Negado.')

#Botões - Login e Register
LoginButton = ttk.Button(RightFrame, text='Login', width=30, command=Login)
LoginButton.place(x= 100, y=225)

#Removendo botões para login
def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    
#Inserindo botões de cadastro
    NomeLabel = Label(RightFrame, text='Name:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE',fg='White')
    NomeLabel.place(x=5,y=5)

    NomeEntry = Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=18)

    EmailLabel = Label(RightFrame, text='Email:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
    EmailLabel.place(x=5, y=55)

    EmailEntry = Entry(RightFrame, width=41)
    EmailEntry.place(x=90, y=66)

#Insert no banco de dados para captação de dados
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if(Name == '' and Email == '' and User == '' and Pass ==''):
            messagebox.showerror(title='Register Error', message='Preencha Todos os Campos')
        else:    
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)
            """, (Name, Email, User, Pass))

#Salva alterações feitas no banco de dados
            DataBase.conn.commit()
            messagebox.showinfo(title='Register Info', message='Acount Created')

    Register = ttk.Button(RightFrame, text='Register', width=30, command=RegisterToDataBase)
    Register.place(x=100,y=225)

    def BackToLogin():
        #Removendo botões
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo os botões 
        LoginButton.place(x=100)
        RegisterButton.place(x=100)
        
    Back = ttk.Button(RightFrame, text='Back', width=30, command=BackToLogin)
    Back.place(x=100,y=260)

RegisterButton = ttk.Button(RightFrame, text='Register', width=30, command=Register)
RegisterButton.place(x=100, y=260)

#O que estiver fora desse mainloop vai estar fora da janela
jan.mainloop()


