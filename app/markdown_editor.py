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