import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P5_VertcialSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_integrantes = {
            1: ["Angel", "Futbol", 20, "O+", ":/LOGOS/Angel.jpeg"],
            2: ["Jorge", "Juegos", 20, "O+", ":/LOGOS/Jorge.png"],
            3: ["Paniagua", "Chambear", 20, "O+", ":/LOGOS/Paniagua.jpeg"],
            4: ["Sheko", "Gym", 22, "O+", ":/LOGOS/Sheko.jpeg"]
        }

        self.img_persona.setMinium = (1)
        self.img_persona.setMaxium = (4)
        self.img_persona.setStep = (1)
        self.img_persona.setValue = (1)
        self.img_persona.valueChanged.connect(self.cambia)

        def cambia(self):
            print("Text: " + self.combo_persona.currentIndexText())
            print("Index: " + str(self.combo_persona.currentIndexIndex()))
            print("Data: " + str(self.combo_persona.currentIndexData()))

            dataClave = self.combo_persona.currentData()
            imagen = self.datos_persona[dataClave][-1]
            self.img_persona.setPixmap(QtGui.QPixmap(imagen))

    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

