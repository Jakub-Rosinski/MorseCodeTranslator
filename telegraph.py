from chart import Chart
from typing import List
from itertools import chain


class Telegraph(Chart):

    def __init__(self):
        super().__init__()
        self.encoder = Chart()
        self.decoder = Chart(swap=True)


class Encoder(Telegraph):
    seq = None

    def __init__(self, seq: str):
        super().__init__()
        self.seq = seq

    def encode(self) -> str:
        msg = self.prepare()
        msg = [" ".join(map(self.get_signal_from_letter, m)) for m in msg]
        return " / ".join(msg)

    def prepare(self) -> List[str]:
        return [m.replace("'", "") for m in self.seq.split()]

    def get_signal_from_letter(self, key: str) -> str:
        return self.encoder[key.upper()]


class Decoder(Telegraph):
    def __init__(self, seq):
        super().__init__()
        self.seq = seq

    def decode(self, msg: List[str]) -> str:
        return

    def get_letter_from_signal(self, key: str) -> str:
        return self.decoder[key]

