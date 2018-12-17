import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
import random



class Example(QWidget):
    _elems = dict()

    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        start_layout = QVBoxLayout()

        label = QLabel(self)
        label.setText("Привет, игрок")

        name_label = QLabel(self)
        name_label.setText("Введите имя: ")

        name_input = QLineEdit(self)

        btn1 = QPushButton('сохранить', self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.hello)

        btn2 = QPushButton('начать игру', self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.begin)

        start_layout.addWidget(label)
        start_layout.addWidget(name_label)
        start_layout.addWidget(name_input)
        start_layout.addWidget(btn1)
        start_layout.addWidget(btn2)

        self.setLayout(start_layout)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Быки Коровы')
        self.show()

        self._elems["label"] = label
        self._elems["name_label"] = name_label
        self._elems["name_input"] = name_input
        self._elems["btn1"] = btn1
        self._elems["btn2"] = btn2
        self._elems["layout"] = start_layout
        
        self.label_b = QLabel(self)
        self.label_b.setText('Быки')
        self.label_b.move(50,150)
        
        self.label_k = QLabel(self)
        self.label_k.setText('Коровы')
        self.label_k.move(50, 160)
        


    def hello(self):
        name = self._elems["name_input"].text()
        self._elems["label"].setText("Привет, {}".format(name))

    def get_try(self):
        number = self._elems["name_input"].text()
        self.corova_or_bik(number)

    def begin(self):
        self._elems["number"] = self.choisenumber()
        self._elems["btn2"].deleteLater()

        btn3 = QPushButton('угадать', self)
        btn3.resize(btn3.sizeHint())
        btn3.clicked.connect(self.get_try)

        self._elems["layout"].addWidget(btn3)

        self.update()

    def choisenumber(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        number = []
        while len(number) < 4:
            c = random.choice(a)
            if c not in number:
                number.append(c)
        return number

    def corova_or_bik(self, input2):
        number = self._elems["number"]
        input2 = [input2[0], input2[1], input2[2], input2[3]]
        bik = 0
        korova = 0
        for i in range(4):
            if int(input2[i]) == number[i]:
                bik += 1
            elif int(input2[i]) in number:
                korova += 1
        if bik == 4:
            print('Вы угадали!')
        else:
            print(bik, korova)
        self.bik == bik
        self.korova == korova
    
    def counting_b(self):
        c_bik = self.bik
        self.label_b.setText('Быки:', c_bik)
    def counting_k(self):
        c_korova = self.korova
        self.label_k.setText('Коровы:', c_korova)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
