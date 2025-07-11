from engine.random_engine import RandomEngine
from engine.smart_engine.engine import SmartEngine

import sys
import traceback


import sys
from engine.logger import log


def get_engine(name: str):
    if name == "random":
        return RandomEngine()
    elif name == "smart":
        return SmartEngine()
    else:
        raise ValueError(f"Unknown engine: {name}")


def main(args=sys.argv):
    engine_name = sys.argv[1] if len(sys.argv) > 1 else "smart"
    engine = get_engine(engine_name)
    try:
        engine.run()
    except Exception as e:
        log_crash(engine, e)
        sys.exit(1)

    engine.run()


def log_crash(engine, exception):
    tb_str = "".join(
        traceback.format_exception(type(exception), exception, exception.__traceback__)
    )
    print(f"[CRASH] {exception}")
    log("crash", f"{exception}\n{tb_str}")


if __name__ == "__main__":
    main()
