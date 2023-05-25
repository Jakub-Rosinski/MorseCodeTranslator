from typing import List

from strategies.translating_strategy import TranslatingStrategy
from telegraph.encoder import encode
from telegraph.decoder import decode


class Encoder(TranslatingStrategy):
    def __init__(self, seq: str):
        super().__init__()
        self.seq = seq

    def prepare(self) -> List[str]:
        return [m.replace("'", "") for m in self.seq.split()]

    def translate(self) -> str:
        msg = self.prepare()
        msg = [" ".join(map(self.get_signal_from_letter, m)) for m in msg]
        return " / ".join(msg)

    @staticmethod
    def get_signal_from_letter(key: str) -> str:
        e = encode()
        return e[key.upper()]


class Decoder(TranslatingStrategy):
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

    @staticmethod
    def get_letter_from_signal(key: str) -> str:
        d = decode()
        return d[key]

