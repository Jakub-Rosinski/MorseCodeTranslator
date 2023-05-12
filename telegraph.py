from chart import Chart
from typing import List
from abc import ABC, abstractmethod


class Telegraph(Chart):

    def __init__(self):
        super().__init__()
        self.encoder = Chart()
        self.decoder = Chart(swap=True)


class TranslatingStrategy(ABC):
    @abstractmethod
    def prepare(self) -> List[str]:
        pass

    @abstractmethod
    def translate(self) -> str:
        pass


class Translator:
    def __init__(self, translating_strategy: TranslatingStrategy):
        self.translating_strategy = translating_strategy

    def translate(self):
        return self.translating_strategy.translate()


class Encoder(TranslatingStrategy, Telegraph):
    def __init__(self, seq: str):
        super().__init__()
        self.seq = seq

    def prepare(self) -> List[str]:
        return [m.replace("'", "") for m in self.seq.split()]

    def translate(self) -> str:
        msg = self.prepare()
        msg = [" ".join(map(self.get_signal_from_letter, m)) for m in msg]
        return " / ".join(msg)

    def get_signal_from_letter(self, key: str) -> str:
        return self.encoder[key.upper()]


class Decoder(TranslatingStrategy, Telegraph):
    def __init__(self, seq: str):
        super().__init__()
        self.seq = seq

    def prepare(self) -> List[List[str]]:
        msg = [s.strip() for s in self.seq.split("/")]
        msg = [s.split(" ") for s in msg]
        return msg

    def translate(self) -> str:
        msg = self.prepare()
        msg = ["".join(map(self.get_letter_from_signal, m)) for m in msg]
        return " ".join(msg).title()

    def get_letter_from_signal(self, key: str) -> str:
        return self.decoder[key]

