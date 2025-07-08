from engine import UCIEngine
import sys
import traceback


def main():
    engine = UCIEngine()
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

    if hasattr(engine, "log") and engine.debug:
        engine.log("crash", f"{exception}\n{tb_str}")
    else:
        # Fallback to stderr or a default log
        with open("crash_fallback.log", "a") as f:
            f.write(f"CRASH: {exception}\n{tb_str}")


if __name__ == "__main__":
    main()
