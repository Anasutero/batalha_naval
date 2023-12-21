#importe das biliotecas
from PyQt5 import QtWidgets , uic, QtCore
import random
import sys

#criação da classe e execução das telas
class telas:
    def __init__(self) :

        self.app = QtWidgets.QApplication([])
        self.inicio = uic.loadUi("telas/batalha.ui")
        self.inicio.show()
        self.tabela_jogo = uic.loadUi("telas/tabela_jogo.ui")
        self.ganhador = uic.loadUi("telas/ganhador.ui")
        self.perdedor= uic.loadUi("telas/perdedor.ui")
        self.inicio.botao_jogar.clicked.connect(self.mudar_tela)
        self.inicio.botao_sair.clicked.connect(self.fechar_tela)

       #comando para sair
        self.ganhador.sair.clicked.connect(self.fechar_tela)
        self.perdedor.sair_2.clicked.connect(self.fechar_tela)

       #comando para jogar novamente
        self.ganhador.jogar_novamente.clicked.connect(self.again)
        self.perdedor.jogar_novamente_2.clicked.connect(self.again)


        self.tentativas_max = 15
        self.tentativas = 0


        coordenadasLetras = ["a", "b", "c", "d", "e", "f", "g", "h"]
        coordenadasNumeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
        sorteio = []

        sorteio1 = random.sample(coordenadasLetras, 4)

        while True:
            sorteio2 = random.sample(coordenadasNumeros, 4)
            if int(sorteio2[1]) > 6:
                continue
            if int(sorteio2[2]) > 5:
                continue
            if int(sorteio2[3]) > 4:
                continue
            else:
                break

        for i in range(len(sorteio1)):
            sorteio.append(f"{sorteio1[i]}{sorteio2[i]}")

        print(sorteio)

        self.barcos = []

        for a in range(len(sorteio)):
            if a == 0:
                for i in range(len(sorteio)):
                    self.barcos.append(sorteio[i])

            if a == 1:
                print("\nCOMEÇA O 2")
                separado = list(sorteio[a])
                print(separado)
                self.barcos.append(f"{separado[0]}{int(separado[1]) + 1}")
                print(self.barcos)

            if a == 2:
                for i in range(2):
                    print("\nCOMEÇA O 3")
                    separado = list(sorteio[a])
                    print(separado)
                    self.barcos.append(f"{separado[0]}{int(separado[1]) + (i + 1)}")
                    print(self.barcos)

            if a == 3:
                for i in range(3):
                    print("\nCOMEÇA O 4")
                    separado = list(sorteio[a])
                    print(separado)
                    self.barcos.append(f"{separado[0]}{int(separado[1]) + (i + 1)}")
                    print(self.barcos)

        for button in self.tabela_jogo.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.selecionarBotao)

        self.app.exec()

        sys.exit(self.app.exec_())

        # criação das funções
    def restart(self):
        QtCore.QCoreApplication.quit()  # permite sair da aplicação
        QtCore.QProcess.startDetached(sys.executable, sys.argv)  # permite que o programa incie novamente antes de sair por completo da aplicação

    def again(self):
        self.restart()
    def mudar_tela(self):
        self.inicio.close()
        self.tabela_jogo.show()

    def fechar_tela(self):
        self.inicio.close()
        self.ganhador.close()
        self.tabela_jogo.close()
        self.perdedor.close()


    def selecionarBotao(self):
        sender = self.inicio.sender()
        senderCoordenada = sender.objectName()

        if self.tentativas < self.tentativas_max:

            if senderCoordenada in self.barcos:
                sender.setStyleSheet("background-image: url('imagens/explosao.png'); border: none")
                self.barcos.remove(senderCoordenada)

                if len(self.barcos) == 0:
                    self.inicio.close()
                    self.ganhador.show()


            else:
                sender.setStyleSheet("background-image: url('imagens/errou.png'); border: none")
                self.tentativas += 1
                print(self.tentativas)

        else:
            self.tabela_jogo.close()
            self.perdedor.show()



#colocar a classe para ser executada
if __name__  == '__main__':
    c = telas()