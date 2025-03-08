import enchant
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
from PyQt5.QtWidgets import QTextEdit

class SpellChecker:
    def __init__(self, editor):
        self.editor = editor
        self.dictionary = enchant.Dict("en_US")  # Default to US English
        self.editor.textChanged.connect(self._check_spelling)

    def _check_spelling(self):
        """Check the spelling of the text in the editor."""
        cursor = self.editor.textCursor()
        cursor.movePosition(cursor.Start)
        self.editor.setExtraSelections([])

        while not cursor.atEnd():
            cursor.movePosition(cursor.EndOfWord, cursor.KeepAnchor)
            word = cursor.selectedText()

            if word and not self.dictionary.check(word):
                self._highlight_word(cursor)

            cursor.movePosition(cursor.NextWord)

    def _highlight_word(self, cursor):
        """Highlight a misspelled word."""
        format = QTextCharFormat()
        format.setUnderlineColor(QColor(255, 0, 0))  # Red underline
        format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)

        selection = QTextEdit.ExtraSelection()
        selection.cursor = cursor
        selection.format = format

        self.editor.setExtraSelections(self.editor.extraSelections() + [selection])