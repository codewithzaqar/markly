from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QStringListModel, Qt

class AutoCompleter:
    def __init__(self, editor):
        self.editor = editor
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setModel(QStringListModel(self._get_completion_list()))
        self.editor.setCompleter(self.completer)

    def _get_completion_list(self):
        """Get a list of Markdown syntax elements for auto-completion."""
        return [
            "# Header 1",
            "## Header 2",
            "### Header 3",
            "#### Header 4",
            "##### Header 5",
            "###### Header 6",
            "**bold**",
            "*italic*",
            "~~strikethrough~~",
            "`inline code`",
            "```\ncode block\n```",
            "[link text](url)",
            "![alt text](image_url)",
            "- unordered list",
            "1. ordered list",
            "> blockquote",
            "---",  # Horizontal rule
        ]