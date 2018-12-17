import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from random import choice



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
        
        self.btn_b = QPushButton('Быки', self)
        self.btn_b.resize(self.btn_b.sizeHint())
        self.btn_b.move(100, 150)
        
        self.btn_k = QPushButton('Коровы', self)
        self.btn_k.resize(self.btn_k.sizeHint())
        self.btn_k.move(100,200)
        
        
    def count_b(self):
        self.btn_b.setText('Быки:', self.bik)
        

    def count_k(self):
        self.btn_b.setText('Коровы:', self.korova)
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
        self.bik = 0
        self.korova = 0
        for i in range(4):
            if int(input2[i]) == number[i]:
                self.bik += 1
                self.btn_b.connect(self.count_b)
            elif int(input2[i]) in number:
                self.korova += 1
                self.btn_k.connect(self.count_k)
        if self.bik == 4:
            print('Вы угадали!')
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
