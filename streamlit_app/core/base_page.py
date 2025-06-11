from abc import ABC, abstractmethod


class Page(ABC):
    def __init__(self):
        self.title = 'Default Title'

    @abstractmethod
    def render(self):
        pass
