# Form implementation generated from reading ui file 'janela_pesquisa.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector
conexao = mysql.connector.connect(
    host='localhost', user='root',
    password='', database='escola'
)
cursor = conexao.cursor()
print('conectado ao DB')
from PyQt6 import QtCore,QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

class Ui_Pesquisa_aluno(object):
    def setupUi(self, Pesquisa_aluno):
        Pesquisa_aluno.setObjectName("Pesquisa_aluno")
        Pesquisa_aluno.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=Pesquisa_aluno)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_nome = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.horizontalLayout.addWidget(self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.horizontalLayout.addWidget(self.lineEdit_nome)
        self.pushButton_pesquisar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")

        self.pushButton_pesquisar.clicked.connect(self.pesquisar)


        self.horizontalLayout.addWidget(self.pushButton_pesquisar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        Pesquisa_aluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pesquisa_aluno)
        QtCore.QMetaObject.connectSlotsByName(Pesquisa_aluno)

    def retranslateUi(self, Pesquisa_aluno):
        _translate = QtCore.QCoreApplication.translate
        Pesquisa_aluno.setWindowTitle(_translate("Pesquisa_aluno", "Pesquisa de Alunos"))
        self.label_nome.setText(_translate("Pesquisa_aluno", "Nome:"))
        self.lineEdit_nome.setText(_translate("Pesquisa_aluno", ""))
        self.pushButton_pesquisar.setText(_translate("Pesquisa_aluno", "Pesquisar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Pesquisa_aluno", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Pesquisa_aluno", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Pesquisa_aluno", "Curso"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Pesquisa_aluno", "Turno"))

    def pesquisar(self):
        nome = self.lineEdit_nome.text() #captura o texto digitado
        sql = '''SELECT * FROM aluno WHERE NOME LIKE %s'''
        cursor.execute(sql,("%" + nome + "%",))
        dados = cursor.fetchall()
        print(dados)

        self.tableWidget.setRowCount(len(dados))
        cont=0 #contador de linhas
        for linha in dados:
            codigo = QTableWidgetItem(str(linha[0]))
            nome = QTableWidgetItem(linha[1])
            curso = QTableWidgetItem(linha[2])
            turno = QTableWidgetItem(linha[3])

            self.tableWidget.setItem(cont,0,codigo)
            self.tableWidget.setItem(cont,1,nome)
            self.tableWidget.setItem(cont,2,curso)
            self.tableWidget.setItem(cont,3,turno)
            cont+=1
        self.tableWidget.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pesquisa_aluno = QtWidgets.QMainWindow()
    ui = Ui_Pesquisa_aluno()
    ui.setupUi(Pesquisa_aluno)
    Pesquisa_aluno.show()
    sys.exit(app.exec())
