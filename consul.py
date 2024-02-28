import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QKeyEvent, QPixmap


class GuiDuasColunas(QWidget):

    def __init__(self):

        super().__init__()


        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa da Padaria")

        
        layoutVerEs = QVBoxLayout()
        layoutVerDi = QVBoxLayout()
        layoutHor = QHBoxLayout()


        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#00695c;}")
        labelColEsq.setFixedWidth(800)

        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#e0e0e0}")
        labelColEsq.setFixedWidth(800)

        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("logo_padaria.png"))
        labelLogo.setScaledContents(True)


        labelCodigo = QLabel("Código do Produto:")
        labelCodigo.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.codigoEdit = QLineEdit()
        self.codigoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelNomeProduto = QLabel("Nome do Produto:")
        labelNomeProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.nomeProdutoEdit = QLineEdit()
        self.nomeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelDescricaoProduto = QLabel("Descrição do Produto:")
        labelDescricaoProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.descricaoProdutoEdit = QLineEdit()
        self.descricaoProdutoEdit.setFixedHeight(100)
        self.descricaoProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelQuantidadeProduto = QLabel("Quantidade do Produto:")
        labelQuantidadeProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.quantidadeProdutoEdit = QLineEdit()
        self.quantidadeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelPrecoProduto = QLabel("Preço Unitário do Produto:")
        labelPrecoProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.precoProdutoEdit = QLineEdit()
        self.precoProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelSubTotalProduto = QLabel("SubTotal:")
        labelSubTotalProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.subTotalProdutoEdit = QLineEdit()
        self.subTotalProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")


        layoutVerEs.addWidget(labelLogo)

        layoutVerEs.addWidget(labelCodigo)
        layoutVerEs.addWidget(self.codigoEdit)

        layoutVerEs.addWidget(labelNomeProduto)
        layoutVerEs.addWidget(self.nomeProdutoEdit)

        layoutVerEs.addWidget(labelDescricaoProduto)
        layoutVerEs.addWidget(self.descricaoProdutoEdit)

        layoutVerEs.addWidget(labelQuantidadeProduto)
        layoutVerEs.addWidget(self.quantidadeProdutoEdit)

        layoutVerEs.addWidget(labelPrecoProduto)
        layoutVerEs.addWidget(self.precoProdutoEdit)

        layoutVerEs.addWidget(labelSubTotalProduto)
        layoutVerEs.addWidget(self.subTotalProdutoEdit)

        labelColEsq.setLayout(layoutVerEs)


        # Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(10)


        # criando o cabecalho para a tabela resumo
        titulos = ["Código","Nome Produto","Quantidade","Preço Unitário","Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)

        labelTotalPagar = QLabel("Total a Pagar")
        labelTotalPagar.setStyleSheet("QLabel{color:#00695c;font-size:25pt}")
        totalPagarEdit = QLineEdit("0,00")
        totalPagarEdit.setStyleSheet("QLineEdit{padding:10px;font-size:70pt; width:400}")


        layoutVerDi.addWidget(self.tbResumo)
        layoutVerDi.addWidget(labelTotalPagar)
        layoutVerDi.addWidget(totalPagarEdit)


        labelColDir.setLayout(layoutVerDi)


        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)


        self.setLayout(layoutHor)


        # Capturando a tecla que o usuário está digitando e 
        # chamando a função(keyPressEvent) para executar um comando quando esta tecla
        # for acionada. 
        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):
        print("event", e)
        if (e.key() == Qt.Key_F2) :   
            print(' Você teclou F2')

            self.tbResumo.setItem(0,0,QTableWidgetItem(str(self.codigoEdit.text())))
            self.tbResumo.setItem(0,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(0,2,QTableWidgetItem(str(self.quantidadeProdutoEdit.text())))
            self.tbResumo.setItem(0,3,QTableWidgetItem(str(self.precoProdutoEdit.text())))
            self.tbResumo.setItem(0,4,QTableWidgetItem(str(self.subTotalProdutoEdit.text())))



app = QApplication(sys.argv)

janela = GuiDuasColunas()
janela.show()

app.exec_()
