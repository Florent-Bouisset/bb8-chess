from abc import ABC, abstractmethod
from .logger import log


class BaseEngine(ABC):
    def __init__(self, debug=False):
        self.debug = debug

    def _respond(self, message):
        print(message, flush=True)
        log("out", message)

    @abstractmethod
    def run(self):
        pass
