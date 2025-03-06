from PyQt5.QtWidgets import QTextEdit

class MarkdownEditor(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Write your Markdown here...")