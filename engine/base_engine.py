from abc import ABC, abstractmethod
import sys
from datetime import datetime
from pathlib import Path


class BaseEngine(ABC):
    def __init__(self, debug=False, log_path=None):
        self.debug = debug
        self.log_path = log_path
        if self.debug:
            if getattr(sys, "frozen", False):
                # Running as compiled executable
                base_dir = Path(sys.executable).resolve().parent
            else:
                # Running from source
                base_dir = Path(__file__).resolve().parent.parent

            logs_dir = base_dir / "logs"
            logs_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.log_path = log_path or logs_dir / f"uci_engine_{timestamp}.log"
            print(self.log_path)

            with open(self.log_path, "w") as f:
                f.write(f"--- UCI Engine Log Started: {datetime.now()} ---\n")

    def log(self, direction, message):
        if self.debug:
            with open(self.log_path, "a") as f:
                f.write(f"[{direction.upper()}] {message}\n")

    def _respond(self, message):
        print(message, flush=True)
        self.log("out", message)

    @abstractmethod
    def run(self):
        pass
