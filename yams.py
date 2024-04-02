import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGroupBox, QGridLayout, QMessageBox
from random import randint

class YamsGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Yams Game')
        layout = QVBoxLayout()

        self.roll_button = QPushButton('Roll Dice', self)
        self.roll_button.clicked.connect(self.roll_dice)

        self.dice_layout = QGridLayout()

        self.result_label = QLabel('Result: ')

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.roll_button)
        button_layout.addWidget(self.result_label)

        layout.addLayout(button_layout)
        layout.addLayout(self.dice_layout)

        self.setLayout(layout)

        self.dice_values = [0] * 5

    def roll_dice(self):
        for i in range(5):
            self.dice_values[i] = randint(1, 6)

        self.display_dice()

    def display_dice(self):
        for i in range(5):
            dice_label = QLabel(str(self.dice_values[i]))
            self.dice_layout.addWidget(dice_label, 0, i)

    def closeEvent(self, event):
        confirm = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = YamsGame()
    game.show()
    sys.exit(app.exec_())
