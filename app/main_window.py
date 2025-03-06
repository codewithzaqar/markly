from PyQt5.QtWidgets import QMainWindow, QSplitter
from PyQt5.QtCore import Qt
from .markdown_editor import MarkdownEditor
from .markdown_preview import MarkdownPreview
from .toolbar import Toolbar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markly")
        self.setGeometry(100, 100, 800, 600)

        self.toolbar = Toolbar(self)
        self.addToolBar(self.toolbar)

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