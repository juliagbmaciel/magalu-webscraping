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
        """
        cria tela do tkinter
        """
        self.janela.title('MAGAZINELUIZA')
        self.janela.geometry('700x700')
        self.janela.configure(background='#f0f0f0')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)
        self.janela.minsize(width=700, height=700)

    def cria_navbar(self):
        """
        Cria barra de navegação
        """
        self.nav = Image.open("nav.png")
        self.imagem_nav = ImageTk.PhotoImage(self.nav)
        self.frame_0 = Label(self.janela, image=self.imagem_nav, )
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=0.1)
        self.botoes()

    def botoes(self):
        """
        define os botões da tela
        """
        fonte = ('Inter', 16)
        self.btHome = Button(self.frame_0, text='HOME', font=fonte, fg='white', background='#0087FD', relief='flat', command=self.home)
        self.btHome.place(relx=0.3, rely=0.25, relwidth=0.15, relheight=0.43)
        self.btTvs = Button(self.frame_0, text='TVS', font=fonte, fg='white', background='#0087FD', relief='flat', command=self.command_tvs)
        self.btTvs.place(relx=0.5, rely=0.25, relwidth=0.15, relheight=0.43)
        self.btMarcas = Button(self.frame_0, text='BRANDS', font=fonte, fg='white', background='#0087FD', relief='flat', command=self.command_brand)
        self.btMarcas.place(relx=0.7, rely=0.25, relwidth=0.15, relheight=0.43)


    def home(self):
        """
        exibe aba(tela) "home" do tkinter
        """
        self.cria_navbar()
        self.imagem = Image.open("home.png")
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)
        frame = Frame(self.janela, background='#000')
        frame.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.1)
        self.label_imagem = Label(frame, image=self.imagem_tk)
        self.label_imagem.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)

    def command_brand(self):
        """
        exibe tela "brands" quando o usuario clicar no botão,
        mostra tvs de acordo com a marca
        """
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
        """
        Inicia webscrap das marcas das tvs caso solicitado
        """
        j = Marcas()

    def webscrapp_tvs(self):
        """
        Inicia webscrap das tvs caso solicitado
        """
        j = Tvs()

    def tabela(self):
        """
        Cria tabela de acordo com as marcas
        """
        self.lista_frame2(True)
        self.selecionar_opcao()

    def command_tvs(self):
        """
        cria aba(tela) quando o botão tvs é clicado, feito pra mostrar as 10 primeiras tvs do site
        """
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
        """
        cria tabela das 10 primeiras tvs mostradas no site
        """
        self.lista_frame2(False)
        self.selecionar_tvs()

    def lista_frame2(self, s):
        """
        cria tabela de acordo com a variavel enviada como parametro, se s for true, entao a tabela é de acordo com marca,
        se s for false, então a tabela mostra todas as 10 primeiras tvs
        :param s: valida qual tabela será criada, valores true ou false
        """
        if s:
            self.listatvs = ttk.Treeview(self.tvsframe, height=3,
                                         columns=('col1',
                                                  'col2',
                                                  'col3'))
        else:
            self.listatvs = ttk.Treeview(self.alltvsframe, height=3,
                                         columns=('col1',
                                                  'col2',
                                                  'col3'))
        self.listatvs.heading('#0', text='')
        self.listatvs.heading('#1', text='NOME')
        self.listatvs.heading('#2', text='PREÇO')

        self.listatvs.column('#0', width=5)
        self.listatvs.column('#1', width=530)
        self.listatvs.column('#2', width=80)

        self.listatvs.place(rely=0.3, relx=0.03,
                            relwidth=0.93, relheight=0.4)

    def selecionar_opcao(self):
        """
        Insere dados do banco na tabela, de acordo com a marca escolhida
        """
        self.brand = self.combobox.get()
        print(self.brand)
        self.listatvs.delete(*self.listatvs.get_children())
        cursor.execute(f"Select nome, preco from {self.brand}")
        linhas = cursor.fetchall()
        for i in linhas:
            self.listatvs.insert(parent='', index=0, values=i)

    def selecionar_tvs(self):
        """
        Insere dados do banco na tabela, das 10 primeiras tvs do site
        """
        self.listatvs.delete(*self.listatvs.get_children())
        cursor.execute(f"Select nome, preco from tvs")
        linhas = cursor.fetchall()
        for i in linhas:
            self.listatvs.insert(parent='', index=0, values=i)


jan = Aplicacao()
jan.tela()