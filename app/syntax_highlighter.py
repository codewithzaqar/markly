from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor
from PyQt5.QtCore import QRegExp

class MarkdownHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.highlighting_rules = []

        # Headers (e.g., #, ##, ###)
        header_format = QTextCharFormat()
        header_format.setForeground(QColor(0, 0, 255))  # Blue
        header_format.setFontWeight(75)
        self.highlighting_rules.append((QRegExp("^#{1,6}\\s.*"), header_format))

        # Bold (e.g., **bold**)
        bold_format = QTextCharFormat()
        bold_format.setFontWeight(75)
        self.highlighting_rules.append((QRegExp("\\*\\*.*\\*\\*"), bold_format))

        # Italics (e.g., *italics*)
        italic_format = QTextCharFormat()
        italic_format.setFontItalic(True)
        self.highlighting_rules.append((QRegExp("\\*.*\\*"), italic_format))

        # Code (e.g., `code`)
        code_format = QTextCharFormat()
        code_format.setForeground(QColor(0, 128, 0))  # Green
        code_format.setFontFamily("Courier New")
        self.highlighting_rules.append((QRegExp("`.*`"), code_format))

        # Links (e.g., [text](url))
        link_format = QTextCharFormat()
        link_format.setForeground(QColor(0, 128, 128))  # Teal
        link_format.setFontUnderline(True)
        self.highlighting_rules.append((QRegExp("\\[.*\\]\\(.*\\)"), link_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)