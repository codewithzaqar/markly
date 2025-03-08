from PyQt5.QtGui import QPalette, QColor

class ThemeManager:
    def __init__(self, parent):
        self.parent = parent
        self.current_theme = "light"  # Track the current theme
        self.themes = {
            "light": self._apply_light_theme,
            "dark": self._apply_dark_theme,
            "custom": self._apply_custom_theme,
        }

    def apply_theme(self, theme_name):
        """Apply a theme by name."""
        if theme_name in self.themes:
            self.themes[theme_name]()
            self.current_theme = theme_name  # Update the current theme
        else:
            self._apply_light_theme()
            self.current_theme = "light"

    def is_dark_theme(self):
        """Check if the current theme is dark."""
        return self.current_theme == "dark"

    def _apply_light_theme(self):
        """Apply the light theme."""
        light_palette = QPalette()
        light_palette.setColor(QPalette.Window, QColor(240, 240, 240))
        light_palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Base, QColor(255, 255, 255))
        light_palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
        light_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        light_palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Text, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Button, QColor(240, 240, 240))
        light_palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        light_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        light_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.parent.setPalette(light_palette)

    def _apply_dark_theme(self):
        """Apply the dark theme."""
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        self.parent.setPalette(dark_palette)

    def _apply_custom_theme(self):
        """Apply a custom theme."""
        # Load custom theme from a CSS file
        with open("styles/themes/custom_theme.css", "r") as file:
            self.parent.setStyleSheet(file.read())