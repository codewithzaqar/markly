from PyQt5.QtWidgets import QTextBrowser
from markdown2 import markdown

class MarkdownPreview(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Preview will appear here...")

    def update_preview(self):
        markdown_text = self.parent().parent().editor.toPlainText()
        html = markdown(markdown_text)
        self.setHtml(html)