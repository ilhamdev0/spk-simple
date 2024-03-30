from abc import (
    ABC,
    abstractmethod,
)

class Input(ABC):
    @abstractmethod
    def filetidakada(self):
        pass

    @abstractmethod
    def open(self):
        pass

class Output(ABC):
    @abstractmethod
    def save(self):
        pass

class Config(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def verify(self):
        pass

class Logic(ABC):
    @abstractmethod
    def normalizer_max(self):
        pass

    @abstractmethod
    def normalizer_min(self):
        pass

    @abstractmethod
    def score(self):
        pass

    @abstractmethod
    def topscore(self):
        pass