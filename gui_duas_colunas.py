import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QKeyEvent, QPixmap


class GuiDuasColunas(QWidget):

    def __init__(self):

        super().__init__()

        self.total = 0.0
        self.linha = 0
        self.setGeometry(100,100,500,600)
        self.setWindowTitle("Caixa da Padaria")
        
        layoutVerEs = QVBoxLayout()
        layoutVerDi = QVBoxLayout()
        layoutHor = QHBoxLayout()

        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#807462}")
        labelColEsq.setFixedWidth(790)

        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#b8faff}")
        labelColDir.setFixedWidth(790)

        LabelLogo = QLabel()
        LabelLogo.setPixmap(QPixmap("to.png"))
        LabelLogo.setScaledContents(True)
        
        labelCodigo = QLabel("Código do Produto: ")
        labelCodigo.setStyleSheet("QLabel{color:#e8fdff;font-size:10pt; }")
        self.codigoEdit = QLineEdit()
        self.codigoEdit.setFixedHeight(20)
        self.codigoEdit.setStyleSheet("QLineEdit{padding:20px;font-size:10pt; width:400}")

        labelNomeProduto = QLabel("Nome do Produto: ")
        labelNomeProduto.setStyleSheet("QLabel{color:#e8fdff;font-size:10pt}")
        self.nomeProdutoEdit = QLineEdit()
        self.nomeProdutoEdit.setFixedHeight(20)
        self.nomeProdutoEdit.setStyleSheet("QLineEdit{padding:20px;font-size:10pt; width:400}")

        labelDescProduto = QLabel("Descrição: ")
        labelDescProduto.setStyleSheet("QLabel{color:#e8fdff;font-size:10pt}")
        self.descProdutoEdit = QLineEdit()
        self.descProdutoEdit.setFixedHeight(40)
        self.descProdutoEdit.setStyleSheet("QLineEdit{padding:20px;font-size:10pt; width:400}")

        labelQuantProduto = QLabel("Quantidade: ")
        labelQuantProduto.setStyleSheet("QLabel{color:#e8fdff;font-size:10pt}")
        self.quantProdutoEdit = QLineEdit()
        self.quantProdutoEdit.setFixedHeight(20)
        self.quantProdutoEdit.setStyleSheet("QLineEdit{padding:20px;font-size:10pt; width:400}")

        labelPreco = QLabel("Preco: ")
        labelPreco.setStyleSheet("QLabel{color:#e8fdff;font-size:10pt}")
        self.precoEdit = QLineEdit()
        self.precoEdit.setFixedHeight(20)
        self.precoEdit.setStyleSheet("QLineEdit{padding:20px;font-size:10pt; width:400}")

        labelSubTotal = QLabel("SubTotal: ")
        labelSubTotal.setStyleSheet("QLabel{color:#e8fdff;font-size:10pt}")
        self.subTotalEdit = QLineEdit("Aperte F3 para calcular o SubTotal")
        self.subTotalEdit.setEnabled(False)
        self.subTotalEdit.setFixedHeight(20)
        self.subTotalEdit.setStyleSheet("QLineEdit{color:#a69785;padding:20px;font-size:10pt; width:400}")


        layoutVerEs.addWidget(LabelLogo)

        layoutVerEs.addWidget(labelCodigo)
        layoutVerEs.addWidget(self.codigoEdit)

        layoutVerEs.addWidget(labelNomeProduto)
        layoutVerEs.addWidget(self.nomeProdutoEdit)
        
        layoutVerEs.addWidget(labelDescProduto)
        layoutVerEs.addWidget(self.descProdutoEdit)

        layoutVerEs.addWidget(labelQuantProduto)
        layoutVerEs.addWidget(self.quantProdutoEdit)

        layoutVerEs.addWidget(labelPreco)
        layoutVerEs.addWidget(self.precoEdit)

        layoutVerEs.addWidget(labelSubTotal)
        layoutVerEs.addWidget(self.subTotalEdit)

        labelColEsq.setLayout(layoutVerEs)


        # Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(10)


        # criando o cabecalho para a tabela resumo
        titulos = ["Código", "Nome Poduto", "Quatidade", "Preço Unitário", "Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)

        labelTotalPagar = QLabel("Total a Pagar")
        labelTotalPagar.setStyleSheet("QLabel{color:#00695c;font-size:25pt}")
        self.totalPagarEdit = QLineEdit("0,00")
        self.totalPagarEdit.setEnabled(False)
        self.totalPagarEdit.setStyleSheet("QLineEdit{padding:10px;font-size:70pt; width:400}")


        layoutVerDi.addWidget(self.tbResumo)
        layoutVerDi.addWidget(labelTotalPagar)
        layoutVerDi.addWidget(self.totalPagarEdit)


        labelColDir.setLayout(layoutVerDi)


        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)


        self.setLayout(layoutHor)



        # Capturando a tecla que o usuário está digitando e 
        # chamando a função(keyPressEvent) para executar um comando quando esta tecla
        # for acionada. 

        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):
        
        
        if (e.key() == Qt.Key_F2) :  
            print(' Você teclou F2')

            self.tbResumo.setItem(self.linha,0,QTableWidgetItem(str(self.codigoEdit.text())))
            self.tbResumo.setItem(self.linha,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,2,QTableWidgetItem(str(self.quantProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,3,QTableWidgetItem(str(self.precoEdit.text())))
            self.tbResumo.setItem(self.linha,4,QTableWidgetItem(str(self.subTotalEdit.text())))

            self.linha+=1

            self.total+=float(self.subTotalEdit.text())
            self.totalPagarEdit.setText(str(self.total))

            # Limpar os LineEdit

            self.codigoEdit.setText("")
            self.nomeProdutoEdit.setText("")
            self.descProdutoEdit.setText("")
            self.quantProdutoEdit.setText("")
            self.precoEdit.setText("")
            self.subTotalEdit.setText("Aperte F3 para calcular o SubTotal")
        
        elif(e.key() == Qt.Key_F3): 
            qtd = self.quantProdutoEdit.text()
            prc = self.precoEdit.text()
            res = float(qtd) * float(prc)
            self.subTotalEdit.setText(str(res))


app = QApplication(sys.argv)

janela = GuiDuasColunas()
janela.show()

app.exec_()