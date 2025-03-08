import enchant

class LanguageManager:
    def __init__(self, spell_checker):
        self.spell_checker = spell_checker
        self.languages = ["en_US", "en_GB", "es_ES", "fr_FR", "de_DE"]  # Add more language as needed

    def set_language(self, language_code):
        """Set the spell-checking language."""
        if language_code in self.languages:
            self.spell_checker.dictionary = enchant.Dict(language_code)