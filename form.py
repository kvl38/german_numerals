# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(534, 193)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 150, 161, 28))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 70, 511, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_2.addWidget(self.textBrowser_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 511, 51))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.execute()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kovalev_hw1"))
        self.pushButton.setText(_translate("Dialog", "Выполнить перевод"))
        self.label_2.setText(_translate("Dialog", "                        Число"))
        self.label_3.setText(_translate("Dialog", "        Римские цифры"))
        self.label.setText(_translate("Dialog", "Введите число на немецком языке, слова разделяйте одинарным пробелом"))

    def execute(self):
        # self.pushButton.clicked.connect(lambda: self.cl())
        self.pushButton.clicked.connect(lambda: self.write(self.lineEdit.text()))

    def write(self,line):
        self.textBrowser_3.clear()
        self.textBrowser_2.clear()

        units_dict = {'null': 0,'ein': 1, 'einer': 1,'zwei': 2,'drei': 3,'vier': 4,
                      'fünf': 5,'sechs': 6,'sieben': 7,'acht': 8,'neun': 9}
        special_tens_dict = {'elf': 11, 'zwölf': 12, 'dreizehn': 13, 'vierzehn': 14, 'fünfzehn': 15
                           , 'sechszehn': 16, 'siebzehn': 17, 'achtzehn': 18, 'neunzehn': 19}
        dozens_dict = {'zehn': 10, 'zwanzig': 20, 'dreißig': 30, 'vierzig': 40,
                       'fünfzig': 50, 'sechzig': 60, 'siebzig': 70, 'achtzig': 80,
                  'neunzig': 90}
        sto_dict = {'hundert': 100}

        units = {'null': 0, 'einer': 1, 'ein': 1, 'zwei': 2, 'drei': 3, 'vier': 4,
                 'fünf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9,
                 'zehn': 10, 'elf': 11, 'zwölf': 12, 'dreizehn': 13, 'vierzehn': 14,
                 'fünfzehn': 15 , 'sechszehn': 16, 'siebzehn': 17, 'achtzehn': 18, 'neunzehn': 19,
                        'zwanzig': 20, 'dreißig': 30, 'vierzig': 40, 'fünfzig': 50, 'sechzig': 60,
                 'siebzig': 70, 'achtzig': 80, 'neunzig': 90, 'hundert': 100}

        line = self.lineEdit.text().split()
        count = 0

        flag = True
        units_count = 0
        special_tens_count = 0
        dozens_count = 0
        hundert_count = 0

        for i in range(len(line)):

            if len(line) == 1:
                if line[i] in units_dict or line[i] in special_tens_dict or line[i] in dozens_dict:
                    pass
                else:
                    self.textBrowser_3.setText("В данном случае могут стоять только единицы и числа [10-19,20,30,...,90]")
                    flag = False
                    break

            if len(line) >= 2:

                # десятки
                if line[i] in dozens_dict and i != len(line)-1 and line[i+1] in dozens_dict:
                    self.textBrowser_3.setText("Два разряда десятков не могут идти подряд")
                    flag = False
                    break

                if line[i] in dozens_dict and i != len(line)-1 and line[i+1] in special_tens_dict:
                    self.textBrowser_3.setText("Число [11-19] не может стоять после разряда десятков")
                    flag = False
                    break

                if line[i] in units_dict and i != len(line)-1 and line[i+1] in dozens_dict:
                    self.textBrowser_3.setText("Разряд десятков не может стоять после разряда единиц. Между числом единичного формата и числом десятичного формата необходимо поставить 'und'.")
                    flag = False
                    break

                if line[i] in dozens_dict and i != len(line)-1 and line[i+1] in units_dict:
                    self.textBrowser_3.setText("Разряд десятков не может стоять перед разрядом единиц")
                    flag = False
                    break

                if line[i] in dozens_dict and i != len(line)-1 and line[i+1] == 'und':
                    self.textBrowser_3.setText("'und' не может стоять после разряда десятков")
                    flag = False
                    break

                if line[i] in units_dict and i < len(line)-2 and line[i+1] == 'und' and line[i+2] == 'zehn':
                    self.textBrowser_3.setText("Неправильно образовано число [11-19]. Для обозначения этих чисел существуют специальные слова.")
                    flag = False
                    break

                if line[i] in dozens_dict and i != len(line)-1 and line[i+1] == 'hundert':
                    self.textBrowser_3.setText("Разряд сотен не может стоять после разряда десятков")
                    flag = False
                    break

                # единицы
                if line[i] in units_dict and i != len(line) - 1 and line[i + 1] in units_dict:
                    self.textBrowser_3.setText("Два разряда единиц не могут идти подряд.")
                    flag = False
                    break

                # 11-19
                if line[i] in special_tens_dict and i != len(line) - 1 and line[i + 1] in units_dict:
                    self.textBrowser_3.setText("Разряд единиц не может стоять после чисел [11-19]")
                    flag = False
                    break

                if line[i] in special_tens_dict and i != len(line) - 1 and line[i + 1] in dozens_dict:
                    self.textBrowser_3.setText("Разряд десятков не может стоять после чисел [11-19]")
                    flag = False
                    break

                if line[i] in special_tens_dict and i != len(line) - 1 and line[i + 1] == 'hundert':
                    self.textBrowser_3.setText("Разряд сотен не может стоять после чисел [11-19]")
                    flag = False
                    break

                if line[i] in special_tens_dict and i != len(line) - 1 and line[i + 1] in special_tens_dict:
                    self.textBrowser_3.setText("Числа [11-19] не могут идти подряд.")
                    flag = False
                    break

                if line[i] in units_dict and i != len(line) - 1 and line[i + 1] in special_tens_dict:
                    self.textBrowser_3.setText("Число [11-19] не может стоять после разряда единиц. Возможно необходимо поставить 'hundert' между ними.")
                    flag = False
                    break

                # und
                if i == 0 and line[i] == 'und':
                    self.textBrowser_3.setText("'und' не может стоять на первой позиции")
                    flag = False
                    break

                if line[i] == 'und' and i != len(line)-1 and line[i+1] == 'und':
                    self.textBrowser_3.setText("Ошибка: невозможно поставить два 'und' подряд")
                    flag = False
                    break

                if line[i] == 'und' and i != len(line) - 1 and line[i + 1] in units_dict:
                    self.textBrowser_3.setText("'und' не может стоять перед разрядом единиц")
                    flag = False
                    break

                if line[i] == 'und' and i != len(line) - 1 and line[i + 1] in special_tens_dict:
                    self.textBrowser_3.setText("'und' не может стоять перед числами [11-19]")
                    flag = False
                    break

                if line[i] == 'und' and i == len(line) - 1:
                    self.textBrowser_3.setText("'und' не может стоять на последнем месте. Возможно необходимо поставить разряд десятков после 'und'.")
                    flag = False
                    break

                if line[i] in special_tens_dict and i != len(line) - 1 and line[i + 1] == 'und':
                    self.textBrowser_3.setText("'und' не может стоять после чисел [11-19]")
                    flag = False
                    break

                if line[i] in dozens_dict and i != len(line) - 1 and line[i + 1] == 'und':
                    self.textBrowser_3.setText("'und' не может стоять после разряда десятков")
                    flag = False
                    break

                if line[i] == 'hundert' and i != len(line) - 1 and line[i + 1] == 'und':
                    self.textBrowser_3.setText("'und' не может стоять после разряда сотен")
                    flag = False
                    break

                if line[i] == 'und' and i != len(line) - 1 and line[i + 1] == 'hundert':
                    self.textBrowser_3.setText("'und' не может стоять перед разрядом сотен")
                    flag = False
                    break

                # сотни
                if line[i] == 'hundert' and i != len(line) - 1 and line[i + 1] == 'hundert':
                    self.textBrowser_3.setText("Ошибка: два разряда сотен не могут идти подряд.")
                    flag = False
                    break


                # all
                if line[i] not in units and line[i] != "und":
                    self.textBrowser_3.setText("Ошибка: слово " + line[i] + " введено некорректно.")
                    flag = False
                    break

            if line[i] in units_dict:
                units_count += 1
            if line[i] in special_tens_dict:
                special_tens_count += 1
            if line[i] in dozens_dict:
                dozens_count += 1
            if line[i] == 'hundert':
                hundert_count += 1

        if units_count > 2:
            self.textBrowser_3.setText("В числе не может быть больше 2-х разрядов единиц")
            flag = False
        if special_tens_count > 1:
            self.textBrowser_3.setText("В числе не могут встречаться числа [11-19] больше 1-го раза")
            flag = False
        if dozens_count > 1:
            self.textBrowser_3.setText("В числе не может быть больше 1-го разряда десятков")
            flag = False
        if hundert_count > 1:
            self.textBrowser_3.setText("В числе не может быть больше 1-го разряда сотен. Ошибка: 'hundert' встречается несколько раз.")
            flag = False


        if flag:
            if len(line) == 1:
                for it in range(len(line)):
                    new_line = "".join(line[it])
                    for i in units:
                        if new_line == i:
                            count += units[i]
            else:
                if line[1] == 'hundert':
                    new_line = "".join(line[0])
                    for i in units_dict:
                        if new_line == i:
                            count += units_dict[i] * 100
                    for it in range(2, len(line)):
                        new_line = "".join(line[it])
                        for i in units:
                            if new_line == i:
                                count += units[i]
                else:
                    for it in range(len(line)):
                        new_line = "".join(line[it])
                        for i in units:
                            if new_line == i:
                                count += units[i]

            self.textBrowser_3.setText(str(count))
            self.textBrowser_2.setText(self.rimskie(count))

    def rimskie(self, n):
        result = ''
        for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                                 'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
            result += n // arabic * roman
            n %= arabic
        return result

