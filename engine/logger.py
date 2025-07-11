from datetime import datetime
from pathlib import Path
import sys


def setup_logger(log_path=None):
    if getattr(sys, "frozen", False):
        # Running as compiled executable
        base_dir = Path(sys.executable).resolve().parent
    else:
        # Running from source
        base_dir = Path(__file__).resolve().parent.parent

    logs_dir = base_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    actual_log_path = log_path or logs_dir / f"uci_engine_{timestamp}.log"

    print("in main", actual_log_path)

    with open(actual_log_path, "w") as f:
        f.write(f"--- UCI Engine Log Started: {datetime.now()} ---\n")

    def log(direction, message):
        with open(actual_log_path, "a") as f:
            f.write(f"[{direction.upper()}] {message}\n")

    return log


log = setup_logger()
