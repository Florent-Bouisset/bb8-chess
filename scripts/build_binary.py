import subprocess


def run():
    print("Building binary with PyInstaller...\n")

    # Build a single executable from main.py
    subprocess.run(["pyinstaller", "--onefile", "main.py"])
