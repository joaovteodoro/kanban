import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #ARMAZENANDO O ITEM SELECIONADO
        self.item_selecionado_a_fazer = None
        self.item_selecionado_fazendo = None

        #CRIANDO OS LAYOUTS
        layout_principal = QtWidgets.QVBoxLayout(self) #adiciona self ao layout principal
        layout_listas = QtWidgets.QHBoxLayout()
        layout_botoes = QtWidgets.QHBoxLayout()

        #CRIANDO AS LISTAS
        self.lista_a_fazer = QtWidgets.QListWidget()
        self.lista_fazendo = QtWidgets.QListWidget()
        self.lista_feito = QtWidgets.QListWidget()

        #CONECTANDO O CLIQUE DOS ITENS À FUNÇÕES DE SELEÇÃO
        self.lista_a_fazer.itemClicked.connect (self.selecionando_a_fazer) #ItemClicked seleciona o botão clicado
        self.lista_fazendo.itemClicked.connect (self.selecionando_fazendo) 

        #ADICIONANDO AS LISTAS ÀS COLUNAS 
        layout_listas.addWidget(self.lista_a_fazer)
        layout_listas.addWidget(self.lista_fazendo)
        layout_listas.addWidget(self.lista_feito)

        #CRIANDO OS BOTÕES
        self.button_fazer = QtWidgets.QPushButton("A fazer")
        self.button_fazendo = QtWidgets.QPushButton("Fazendo")
        self.button_feito = QtWidgets.QPushButton("Feito") 

        # ADICIONANDO OS BOTÕES AO LAYOUT LINHAS_BOTOES
        layout_botoes.addWidget(self.button_fazer)
        layout_botoes.addWidget(self.button_fazendo)
        layout_botoes.addWidget(self.button_feito)

        #CONECTANDO OS BOTÕES AOS RESPECTIVOS MÉTODOS
        self.button_fazer.clicked.connect(self.inserir_atividade)
        self.button_fazendo.clicked.connect(self.mover_para_fazendo)
        self.button_feito.clicked.connect(self.mover_para_feito)

        # ADICIONANDO AS DUAS LINHAS AO LAYOUT PRINCIPAL
        layout_principal.addLayout(layout_listas) #para adicionar layout, não é addWidget, e sim adicionar layout
        layout_principal.addLayout(layout_botoes)

    #################################

    #METODOS DOS BOTÕES

    def inserir_atividade(self): 
        # Criar o diálogo de entrada de texto
        texto, ok = QtWidgets.QInputDialog.getText(self, 'Adicionar tarefa',"")
        
        if ok:
            # Adicionar o item à lista
            self.lista_a_fazer.addItem(texto)
            self.renumerar_lista(self.lista_a_fazer)
            print(f"Nome inserido: {texto}")
        else:
            print("A entrada foi cancelada")

    def mover_para_fazendo(self):
        if self.item_selecionado_a_fazer:
            texto = self.item_selecionado_a_fazer.text()
            # Remover da lista "a fazer"
            self.lista_a_fazer.takeItem(self.lista_a_fazer.row(self.item_selecionado_a_fazer))
            self.renumerar_lista(self.lista_a_fazer)
            # Adicionar à lista "fazendo"
            self.lista_fazendo.addItem(texto)
            self.renumerar_lista(self.lista_fazendo)
            self.item_selecionado_a_fazer = None       

    def mover_para_feito(self):
        if self.item_selecionado_fazendo:
            texto = self.item_selecionado_fazendo.text()
            # Remover da lista "a fazer"
            self.lista_fazendo.takeItem(self.lista_fazendo.row(self.item_selecionado_fazendo))
            self.renumerar_lista(self.lista_fazendo)
            # Adicionar à lista "fazendo"
            self.lista_feito.addItem(texto)
            self.renumerar_lista(self.lista_feito)
            self.item_selecionado_fazendo = None       

    ######################################

    #METODOS SELECIONANDO OS CLIQUES
    
    def selecionando_a_fazer(self, item):
        self.item_selecionado_a_fazer = item    

    def selecionando_fazendo(self, item):
        self.item_selecionado_fazendo = item     

    ######################################

    #METODOS PARA RENUMERAR LISTA

    def renumerar_lista(self, lista):
        for i in range(lista.count()):
            item = lista.item(i)
            texto = item.text()
            if ". " in texto:
                texto_original = texto.split(". ", 1)[1] #seleciona o texto original, retirando a numeração antiga, que é identificada pelo caractére antes do ". "
            else:
                texto_original = texto  # Caso o texto não tenha um número
            item.setText(f"{i + 1}. {texto_original}")



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv) 
    janela = MyWidget()

    janela.adjustSize()
    janela.show()
    app.exit(app.exec())