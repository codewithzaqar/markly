from PyQt5.QtWidgets import QToolBar, QAction, QFileDialog, QMessageBox

class Toolbar(QToolBar):
    def __init__(self, parent):
        super().__init__("Toolbar", parent)
        self.parent = parent
        self.current_file = None

        # Create actions (without icons)
        self.open_action = QAction("Open", self)
        self.save_action = QAction("Save", self)
        self.save_as_action = QAction("Save As", self)

        # Connect actions to methods
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.save_as_action.triggered.connect(self.save_file_as)

        # Add actions to the toolbar
        self.addAction(self.open_action)
        self.addAction(self.save_action)
        self.addAction(self.save_as_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Markdown File", "", "Markdown Files (*.md);;All Files (*)")
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.parent.editor.setPlainText(content)
                    self.current_file = file_path
                    self.parent.update_status_bar(file_path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(self.parent.editor.toPlainText())
                QMessageBox.information(self, "Success", "File saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Markdown File", "", "Markdown Files (*.md);;All Files (*)")
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.parent.editor.toPlainText())
                self.current_file = file_path
                self.parent.update_status_bar(file_path)
                QMessageBox.information(self, "Success", "File saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")