from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QRegExp
from .syntax_highlighter import MarkdownHighlighter

class MarkdownEditor(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Write your Markdown here...")
        self.setFont(QFont("Courier New", 12))

        # Initialize syntax highlighter
        self.highlighter = MarkdownHighlighter(self.document())

    def setCompleter(self, completer):
        """Set the completer for the editor."""
        self.completer = completer
        self.completer.setWidget(self)
        self.completer.activated.connect(self.insertCompletion)

    def insertCompletion(self, completion):
        """Insert the selected completion into the editor."""
        cursor = self.textCursor()
        cursor.insertText(completion)