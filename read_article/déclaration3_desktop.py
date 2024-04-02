from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel, QMessageBox
import os

articles = {}

# Ouverture du fichier
with open(os.path.join("declaration1789.txt"), "r") as file:
    text = file.read().split("Art. ")

    # Parcours du texte et stockage des articles dans le dictionnaire
    for article in text[1:]:
        # Séparation du numéro de l'article et du texte
        number, text = article.split(".", 1)
        # Stockage de l'article dans le dictionnaire
        articles[int(number)] = text.strip()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Création d'un label de bienvenue
        self.label = QLabel("Bienvenue, veuillez choisir un article :", self)
        self.label.move(100, 50)

        # Création d'un menu déroulant pour choisir un nombre entre 1 et 17
        self.combobox = QComboBox(self)
        self.combobox.move(50, 100)
        for i in range(1, 18):
            self.combobox.addItem(str(i))
        self.combobox.currentIndexChanged.connect(self.display_article)

        # Resize the window to auto size
        self.resize(0, 0)

    def display_article(self):
        # Ouverture d'une nouvelle fenêtre avec le texte de l'article lorsque l'utilisateur a choisi un article
        article_number = int(self.combobox.currentText())
        QMessageBox.information(self, f"Article {article_number}", articles[article_number])

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
