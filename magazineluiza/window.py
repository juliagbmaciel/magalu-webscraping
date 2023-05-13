from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from connect import connection
from webscrapping import Marcas, Tvs


cursor = connection.cursor()
janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.home()
        janela.mainloop()

    def tela(self):
        self.janela.title('MAGAZINELUIZA')
        self.janela.geometry('700x700')
        self.janela.configure(background='#f0f0f0')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)
        self.janela.minsize(width=700, height=700)

    def cria_navbar(self):
        self.nav = Image.open("nav.png")
        self.imagem_nav = ImageTk.PhotoImage(self.nav)
        self.frame_0 = Label(self.janela, image=self.imagem_nav, )
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=0.1)
        self.botoes()

    def botoes(self):
        fonte = ('Inter', 16)
        self.btHome = Button(self.frame_0, text='HOME', font=fonte, fg='white', background='#0087FD', relief='flat', command=self.home)
        self.btHome.place(relx=0.3, rely=0.25, relwidth=0.15, relheight=0.43)
        self.btTvs = Button(self.frame_0, text='TVS', font=fonte, fg='white', background='#0087FD', relief='flat', command=self.command_tvs)
        self.btTvs.place(relx=0.5, rely=0.25, relwidth=0.15, relheight=0.43)
        self.btMarcas = Button(self.frame_0, text='BRANDS', font=fonte, fg='white', background='#0087FD', relief='flat', command=self.command_brand)
        self.btMarcas.place(relx=0.7, rely=0.25, relwidth=0.15, relheight=0.43)


    def home(self):
        self.cria_navbar()
        self.imagem = Image.open("home.png")
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)
        frame = Frame(self.janela, background='#000')
        frame.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.1)
        self.label_imagem = Label(frame, image=self.imagem_tk)
        self.label_imagem.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)

    def command_brand(self):
        self.tvsframe = Frame(self.janela, background='#f0f0f0')
        self.tvsframe.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.09)
        self.search = Image.open("search.png")
        self.search_tk = ImageTk.PhotoImage(self.search)
        label = Label(self.tvsframe, image=self.search_tk)
        label.place(relx=0, relwidth=1.0, relheight=0.1)
        self.frame_combo = Frame(label, background='#000')
        self.frame_combo.place(rely=0.31, relx=0.47, relheight=0.4, relwidth=0.3)
        self.combobox = ttk.Combobox(self.frame_combo,
                                     values=['Samsung', 'LG', 'TCL', 'Multilaser'], state="readonly", width=21, font=('sans-serif', 12), background='#fff')
        self.combobox.place( width=0.7)
        self.combobox.grid(column=0, row=1)
        self.combobox.current(1)
        self.bt = Image.open("lupa.png")
        self.bt_tk = ImageTk.PhotoImage(self.bt)
        self.btSearch = Button(label, image=self.bt_tk, relief='flat', background='#0087FD', command=self.tabela)
        self.btSearch.place(rely=0.21, relx=0.8, relheight=0.5, relwidth=0.04)
        self.btvalues = Button(self.tvsframe, text='Pegar valores em tempo real', font=('Inter', 8, 'bold'), fg='white', relief='groove', background='#0087FD', command=self.webscrapp_marcas)
        self.btvalues.place(rely=0.12, relx=0.05, relheight=0.05, relwidth=0.3)

    def webscrapp_marcas(self):
        j = Marcas()

    def webscrapp_tvs(self):
        j = Tvs()

    def tabela(self):
        self.lista_frame2(True)
        self.selecionar_opcao()

    def command_tvs(self):
        self.cria_navbar()
        self.alltvsframe = Frame(self.janela, background='#f0f0f0')
        self.alltvsframe.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.1)
        self.btvalues_tvs = Button(self.alltvsframe, text='Pegar valores em tempo real', font=('Inter', 8, 'bold'), fg='white', relief='groove', background='#0087FD', command=self.webscrapp_tvs)
        self.btvalues_tvs.place(rely=0.2, relx=0.16, relheight=0.05, relwidth=0.3)
        self.btatualiza = Button(self.alltvsframe, text='Atualizar', font=('Inter', 8, 'bold'), fg='white', relief='groove', background='#0087FD', command=self.tabela_2)
        self.btatualiza.place(rely=0.2, relx=0.05, relheight=0.05, relwidth=0.1)
        self.lista_frame2(False)
        self.selecionar_tvs()

    def tabela_2(self):
        self.lista_frame2(False)
        self.selecionar_tvs()

    def lista_frame2(self, s):
        if s:
            self.listaCli = ttk.Treeview(self.tvsframe, height=3,
                                         columns=('col1',
                                                  'col2',
                                                  'col3'))
        else:
            self.listaCli = ttk.Treeview(self.alltvsframe, height=3,
                                         columns=('col1',
                                                  'col2',
                                                  'col3'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='NOME')
        self.listaCli.heading('#2', text='PREÇO')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=530)
        self.listaCli.column('#2', width=80)

        self.listaCli.place( rely=0.3, relx=0.03,
                            relwidth=0.93, relheight=0.4)

    def selecionar_opcao(self):
        self.brand = self.combobox.get()
        print(self.brand)
        self.listaCli.delete(*self.listaCli.get_children())
        cursor.execute(f"Select nome, preco from {self.brand}")
        linhas = cursor.fetchall()
        for i in linhas:
            self.listaCli.insert(parent='', index=0, values=i)

    def selecionar_tvs(self):
        self.listaCli.delete(*self.listaCli.get_children())
        cursor.execute(f"Select nome, preco from tvs")
        linhas = cursor.fetchall()
        for i in linhas:
            self.listaCli.insert(parent='', index=0, values=i)


jan = Aplicacao()
jan.tela()