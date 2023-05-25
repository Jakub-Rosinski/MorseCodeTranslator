from abc import ABC, abstractmethod


class TranslatingStrategy(ABC):
    @abstractmethod
    def translate(self) -> str:
        pass
