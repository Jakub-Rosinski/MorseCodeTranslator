from strategies.translating_strategy import TranslatingStrategy


class Translator:
    def __init__(self, translating_strategy: TranslatingStrategy):
        self.translating_strategy = translating_strategy

    def translate(self):
        return self.translating_strategy.translate()
