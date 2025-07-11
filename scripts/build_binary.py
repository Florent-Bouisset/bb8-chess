import subprocess
import sys


def build_binary(engine_name: str):
    entry_point = "main.py"
    output_name = f"bishop_b8_{engine_name}"

    # Build command with named binary
    cmd = [
        "pyinstaller",
        "--onefile",
        "--distpath",
        "dist/bin/",  # Executables go here
        "--workpath",
        "dist/temp/",  # Temporary build files
        "--specpath",
        "dist/specs/",  # .spec files
        "--name",
        output_name,
        entry_point,
    ]

    print(f"Building binary for engine '{engine_name}' as '{output_name}'...")
    subprocess.run(cmd, check=True)
    print("Build complete.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python build_binary.py <engine_name>")
        sys.exit(1)
    build_binary(sys.argv[1])
