from PyQt5.QtCore import QTimer

class AutoSaveManager:
    def __init__(self, parent):
        self.parent = parent
        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_save)
        self.timer.start(30000)  # Auto-save every 30 seconds

    def auto_save(self):
        """Auto-save the current file."""
        if self.parent.toolbar.current_file:
            try:
                with open(self.parent.toolbar.current_file, "w", encoding="utf-8") as file:
                    file.write(self.parent.editor.toPlainText())
                self.parent.status_bar.showMessage("Auto-saved successfully!")
            except Exception as e:
                self.parent.status_bar.showMessage(f"Auto-save failed: {e}")