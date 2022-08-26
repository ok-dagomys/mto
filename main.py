import sys

import pandas as pd
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QItemDelegate, QLineEdit, QTableWidget, QHeaderView, QTableWidgetItem, QWidget, QVBoxLayout, \
    QPushButton, QApplication

import cfg


class FloatDelegate(QItemDelegate):
    def __init__(self):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor


class TableWidget(QTableWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.setStyleSheet('font-size: 25px;')

        # set table dimension
        n_rows, n_columns = self.df.shape
        columns_name = self.df.columns
        self.setColumnCount(n_columns)
        self.setRowCount(n_rows)

        self.setHorizontalHeaderLabels(columns_name)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setItemDelegateForColumn(1, FloatDelegate())

        # data insertion
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

        self.cellChanged[int, int].connect(self.update_df)

    def update_df(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text


class DataEditor(QWidget):
    data = pd.read_excel(cfg.src, header=None, index_col=None)
    rem_words = ['Наименвание', 'Кол-во']
    for word in rem_words:
        data = data.mask(data == word)
    data = data[[1, 3]].dropna(axis=0, how='all').reset_index(drop=True)
    data.columns = ['name', 'amount']

    df = pd.DataFrame(data)

    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)

        main_layout = QVBoxLayout()

        self.table = TableWidget(DataEditor.df)
        main_layout.addWidget(self.table)

        button_display = QPushButton('Display document')
        button_display.setStyleSheet('font-size: 30px')
        button_display.clicked.connect(self.display_data)
        main_layout.addWidget(button_display)

        button_save = QPushButton('Save document')
        button_save.setStyleSheet('font-size: 30px')
        button_save.clicked.connect(self.save_data)
        main_layout.addWidget(button_save)

        button_convert = QPushButton('Convert document')
        button_convert.setStyleSheet('font-size: 30px')
        button_convert.clicked.connect(self.convert_data)
        main_layout.addWidget(button_convert)

        self.setLayout(main_layout)

    def display_data(self):
        print(self.table.df)

    def save_data(self):
        self.table.df.to_excel("warehouse.xlsx")
        print('All data saved.')

    def convert_data(self):
        print(self.table.df)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    engine = DataEditor()
    engine.show()

    sys.exit(app.exec_())
