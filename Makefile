# Makefile

# Run the engine in development mode
dev:
	poetry run python main.py

# Build the smart engine as binary
build-smart:
	poetry run python scripts/build_binary.py smart

# Build the random engine
build-random:
	poetry run python scripts/build_binary.py random

# Clean up previous builds
clean:
	rm -rf dist build *.spec

# Rebuild everything
rebuild: clean build-smart build-random
