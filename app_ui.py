from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

from parametrs import TABLE_PARAMETRS, TEXT_PARAMETRS, NUMBER_SIZE

from DXFgenerator import dxf_generator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(518, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/img/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(253, 255, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMinimumSize(QtCore.QSize(500, 137))
        self.Logo.setMaximumSize(QtCore.QSize(500, 137))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Logo.setFont(font)
        self.Logo.setStyleSheet("")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/img/img/logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.Logo.setObjectName("Logo")
        self.verticalLayout.addWidget(self.Logo)
        self.Header = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        self.Header.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Header.setFont(font)
        self.Header.setStyleSheet(
            "color: rgb(253, 255, 252);\n" "background-color: rgb(166, 29, 43);"
        )
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setObjectName("Header")
        self.verticalLayout.addWidget(self.Header)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 10, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.basic_number_error = QtWidgets.QLabel(self.centralwidget)
        self.basic_number_error.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.basic_number_error.setFont(font)
        self.basic_number_error.setStyleSheet("color: rgb(166, 29, 43);")
        self.basic_number_error.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.basic_number_error.setObjectName("basic_number_error")
        self.gridLayout.addWidget(self.basic_number_error, 4, 2, 1, 1)
        self.file_name_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.file_name_input.sizePolicy().hasHeightForWidth()
        )
        self.file_name_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.file_name_input.setFont(font)
        self.file_name_input.setObjectName("file_name_input")
        self.gridLayout.addWidget(self.file_name_input, 1, 2, 1, 1)
        self.file_name_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.file_name_label.sizePolicy().hasHeightForWidth()
        )
        self.file_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.file_name_label.setFont(font)
        self.file_name_label.setStyleSheet("color: rgb(64, 64, 63);")
        self.file_name_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.file_name_label.setObjectName("file_name_label")
        self.gridLayout.addWidget(self.file_name_label, 1, 1, 1, 1)
        self.file_name_error = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.file_name_error.sizePolicy().hasHeightForWidth()
        )
        self.file_name_error.setSizePolicy(sizePolicy)
        self.file_name_error.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.file_name_error.setFont(font)
        self.file_name_error.setStyleSheet("color: rgb(166, 29, 43);")
        self.file_name_error.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.file_name_error.setObjectName("file_name_error")
        self.gridLayout.addWidget(self.file_name_error, 2, 2, 1, 1)
        self.basic_number_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.basic_number_label.sizePolicy().hasHeightForWidth()
        )
        self.basic_number_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.basic_number_label.setFont(font)
        self.basic_number_label.setStyleSheet("color: rgb(64, 64, 63);")
        self.basic_number_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.basic_number_label.setObjectName("basic_number_label")
        self.gridLayout.addWidget(self.basic_number_label, 3, 1, 1, 1)
        self.basic_number_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.basic_number_input.sizePolicy().hasHeightForWidth()
        )
        self.basic_number_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.basic_number_input.setFont(font)
        self.basic_number_input.setObjectName("basic_number_input")
        self.gridLayout.addWidget(self.basic_number_input, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color: rgb(27, 153, 139);")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy)
        self.btn_generate.setMinimumSize(QtCore.QSize(150, 30))
        self.btn_generate.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_generate.setFont(font)
        self.btn_generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_generate.setStyleSheet(
            """
            QPushButton {
            background-color: rgb(64, 64, 63); 
            color: rgb(253, 255, 252);
        }
        QPushButton:hover {
            background-color: rgb(27, 153, 139);
            border: none;
        }
        """
        )
        self.btn_generate.setAutoDefault(False)
        self.btn_generate.setDefault(False)
        self.btn_generate.setFlat(False)
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout.addWidget(self.btn_generate)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setMinimumSize(QtCore.QSize(150, 30))
        self.btn_exit.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet(
            """
            QPushButton {
            background-color: rgb(64, 64, 63); 
            color: rgb(253, 255, 252);
        }
        QPushButton:hover {
            background-color: rgb(166, 29, 43);
            border: none;
        }
        """
        )
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QDoors - D-numbres"))
        self.Header.setText(
            _translate("MainWindow", "Генератор DFX файла с номерами дверей")
        )
        self.file_name_label.setText(_translate("MainWindow", "Название файла: "))
        self.basic_number_label.setText(_translate("MainWindow", "Базовый номер: "))
        self.btn_generate.setText(_translate("MainWindow", "Сгенерировать"))
        self.btn_exit.setText(_translate("MainWindow", "Выйти"))

    def add_functions(self):
        self.btn_exit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_generate.clicked.connect(self.run_app)

    def run_app(self):
        _translate = QtCore.QCoreApplication.translate
        if self.fields_validation():
            number = self.basic_number_input.text().strip()
            file_name = self.file_name_input.text().strip()
            result = dxf_generator(number, file_name, TABLE_PARAMETRS, TEXT_PARAMETRS)
            if result:
                self.label_status.setStyleSheet("color: rgb(27, 153, 139);")
                self.label_status.setText(
                    _translate(
                        "MainWindow",
                        f"Файл {file_name}.dxf успешно сгенерирован.",
                    )
                )

            else:
                self.label_status.setStyleSheet("color: rgb(166, 29, 43);")
                self.label_status.setText(
                    _translate(
                        "MainWindow",
                        "Возникла ошибка. Возможно открыт файл с таким же названием",
                    )
                )

    def empty_input_validation(self, input_field, error_field):
        _translate = QtCore.QCoreApplication.translate
        if not input_field.text().strip():
            error_field.setText(_translate("MainWindow", "Заполните поле"))
            return False
        else:
            error_field.setText(_translate("MainWindow", ""))
            return True

    def numer_size_validation(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.basic_number_input.text().strip()) != NUMBER_SIZE:
            self.basic_number_error.setText(
                _translate("MainWindow", f"Должно быть {NUMBER_SIZE} знаков")
            )
            return False
        return True

    def digits_validation(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            number = int(self.basic_number_input.text().strip())
        except ValueError:
            self.basic_number_error.setText(
                _translate("MainWindow", "Вы ввели не число")
            )
            return False
        else:
            return True

    def fields_validation(self):
        res1 = self.empty_input_validation(self.file_name_input, self.file_name_error)

        if not self.empty_input_validation(
            self.basic_number_input, self.basic_number_error
        ):
            return False

        if not self.numer_size_validation():
            return False

        if not self.digits_validation():
            return False

        return True
