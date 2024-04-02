import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QInputDialog

class TodoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.todo_list = []

        self.setWindowTitle("Todo List")
        self.layout = QVBoxLayout()

        self.task_label = QLabel("Task:")
        self.task_input = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)
        self.edit_button = QPushButton("Edit Task")
        self.edit_button.clicked.connect(self.edit_task)

        self.task_list = QListWidget()

        self.layout.addWidget(self.task_label)
        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.task_list)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.task_input.text()
        self.todo_list.append(task)
        self.task_list.addItem(task)

    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item is not None:
            task = selected_item.text()
            self.todo_list.remove(task)
            self.task_list.takeItem(self.task_list.row(selected_item))

    def edit_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item is not None:
            task = selected_item.text()
            new_task, ok = QInputDialog.getText(self, "Edit Task", "Enter new task:", QLineEdit.Normal, task)
            if ok and new_task:
                self.todo_list.remove(task)
                self.todo_list.append(new_task)
                selected_item.setText(new_task)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoListApp()
    todo_app.show()
    sys.exit(app.exec())