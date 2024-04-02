import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTableWidget, QTableWidgetItem
import random

class YamsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yams")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Bienvenue dans le jeu de Yams !", self)
        self.label.setGeometry(50, 50, 300, 30)

        self.button = QPushButton("Lancer les dés", self)
        self.button.setGeometry(150, 150, 100, 30)
        self.button.clicked.connect(self.lancer_des)
        self.scores_table = QTableWidget(self)
        self.scores_table.setGeometry(200, 500, 400, 200)
        self.scores_table.setColumnCount(2)
        self.scores_table.setHorizontalHeaderLabels(["Combinaison", "Score"])

        # Add rows for each possible combination
        combinations = ["As", "Deux", "Trois", "Quatre", "Cinq", "Six", "Brelan", "Carré", "Full", "Petite Suite", "Grande Suite", "Yams", "Chance"]
        for i, combination in enumerate(combinations):
            self.scores_table.insertRow(i)
            self.scores_table.setItem(i, 0, QTableWidgetItem(combination))

        # Connect the table item selection event to a function
        self.scores_table.itemSelectionChanged.connect(self.display_score)

    def display_score(self):
        selected_items = self.scores_table.selectedItems()
        if selected_items:
            selected_combination = selected_items[0].text()
            # Calculate the score for the selected combination
            score = self.calculate_score(selected_combination)
            self.scores_table.setItem(selected_items[0].row(), 1, QTableWidgetItem(str(score)))

    def calculate_score(self, combination):
        # Implement the logic to calculate the score for each combination
        # ...
        pass

    
    def lancer_des(self):
        # Simulate rolling 5 dice
        dice_results = [random.randint(1, 6) for _ in range(5)]

        # Display the results
        result_text = "Résultats du lancer : " + ", ".join(str(result) for result in dice_results)
        self.label.setText(result_text)
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YamsWindow()
    window.show()
    sys.exit(app.exec_())