from PyQt5.QtWidgets import QMainWindow, QSplitter, QStatusBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from .markdown_editor import MarkdownEditor
from .markdown_preview import MarkdownPreview
from .toolbar import Toolbar
from .theme_manager import ThemeManager
from .export_manager import ExportManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markly")
        self.setGeometry(100, 100, 800, 600)

        self.theme_manager = ThemeManager(self)

        self.export_manager = ExportManager(self)

        self.toolbar = Toolbar(self)
        self.addToolBar(self.toolbar)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("No file opened")

        # Create a splitter to divide the window into two parts
        splitter = QSplitter(Qt.Horizontal)

        # Create the Markdown editor and preview
        self.editor = MarkdownEditor()
        self.preview = MarkdownPreview()

        # Connect the editor's text change signal to the preview's update slot
        self.editor.textChanged.connect(self.preview.update_preview)

        # Add the editor and preview to the splitter
        splitter.addWidget(self.editor)
        splitter.addWidget(self.preview)

        # Set the splitter as the central widget
        self.setCentralWidget(splitter)

        # Apply the default theme
        self.theme_manager.apply_theme("light")

        # Set up keyboard shortcuts
        self._setup_shortcuts()

    def _setup_shortcuts(self):
        """Set up keyboard shortcuts for common actions."""
        self.toolbar.new_action.setShortcut(QKeySequence("Ctrl+N"))
        self.toolbar.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.toolbar.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.toolbar.save_as_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.toolbar.export_html_action.setShortcut("Ctrl+E")
        self.toolbar.export_pdf_action.setShortcut(QKeySequence("Ctrl+P"))

    def update_status_bar(self, file_path):
        """Update the status bar with the current file path."""
        if file_path:
            self.status_bar.showMessage(f"Editing: {file_path}")
        else:
            self.status_bar.showMessage("No file opened")