from abc import ABC, abstractmethod


class Page(ABC):
    def __init__(self) -> None:
        self.title = 'Default Title'

    @abstractmethod
    def render(self) -> None:
        pass
