import sys
import chess
import chess.engine
import random
from datetime import datetime
from pathlib import Path


class UCIEngine:
    def __init__(self, debug=True, log_path=None):
        self.board = chess.Board()
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

    def mockResponse(self):
        self._respond("info string Available processors: 0-9")
        self._respond("info string Using 1 thread")
        self._respond(
            "info string NNUE evaluation using nn-1c0000000000.nnue (133MiB, (22528, 3072, 15, 32, 1))"
        )
        self._respond(
            "info string NNUE evaluation using nn-37f18f62d772.nnue (6MiB, (22528, 128, 15, 32, 1))"
        )
        self._respond(
            "info depth 1 seldepth 4 multipv 1 score cp -27 nodes 24 nps 12000 hashfull 0 tbhits 0 time 2 pv e7e5"
        )
        self._respond(
            "info depth 2 seldepth 3 multipv 1 score cp -20 nodes 48 nps 24000 hashfull 0 tbhits 0 time 2 pv e7e5"
        )
        self._respond(
            "info depth 3 seldepth 4 multipv 1 score cp -20 nodes 72 nps 36000 hashfull 0 tbhits 0 time 2 pv e7e5 a2a3 a7a6"
        )
        self._respond(
            "info depth 4 seldepth 5 multipv 1 score cp -8 nodes 134 nps 44666 hashfull 0 tbhits 0 time 3 pv e7e5"
        )
        self._respond(
            "info depth 5 seldepth 7 multipv 1 score cp -7 nodes 765 nps 109285 hashfull 0 tbhits 0 time 7 pv c7c6 g1f3 d7d5"
        )
        self._respond(
            "info depth 6 seldepth 10 multipv 1 score cp -34 nodes 3031 nps 216500 hashfull 1 tbhits 0 time 14 pv c7c5"
        )
        self._respond(
            "info depth 7 seldepth 9 multipv 1 score cp -35 nodes 3759 nps 234937 hashfull 1 tbhits 0 time 16 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4"
        )
        self._respond(
            "info depth 8 seldepth 14 multipv 1 score cp -49 nodes 7465 nps 339318 hashfull 1 tbhits 0 time 22 pv c7c5 b1c3 e7e6 g1f3 b8c6 d2d4 c5d4 f3d4"
        )
        self._respond(
            "info depth 9 seldepth 14 multipv 1 score cp -49 nodes 10144 nps 362285 hashfull 3 tbhits 0 time 28 pv e7e5 g1f3 b8c6 b1c3 f8b4 c3d5 b4c5 d2d4 c5d4 f3d4 c6d4"
        )
        self._respond(
            "info depth 10 seldepth 14 multipv 1 score cp -52 nodes 11559 nps 385300 hashfull 4 tbhits 0 time 30 pv e7e5 g1f3 b8c6 b1c3 f8b4 c3d5 b4c5 d2d4 c5d4 c2c3"
        )
        self._respond(
            "info depth 11 seldepth 20 multipv 1 score cp -46 nodes 16637 nps 426589 hashfull 5 tbhits 0 time 39 pv e7e5 g1f3 b8c6 b1c3 g8f6 d2d4 e5d4 f3d4 f8b4 d4c6 b7c6"
        )
        self._respond(
            "info depth 12 seldepth 19 multipv 1 score cp -46 nodes 24069 nps 491204 hashfull 7 tbhits 0 time 49 pv e7e5 g1f3 b8c6 b1c3 g8f6 f1b5 f8c5 e1g1 e8g8 b5c6 d7c6 f3e5"
        )
        self._respond(
            "info depth 13 seldepth 19 multipv 1 score cp -25 nodes 42026 nps 600371 hashfull 12 tbhits 0 time 70 pv e7e5 g1f3 b8c6 b1c3 g8f6 f1b5 f8b4 a2a3 b4c3"
        )
        self._respond(
            "info depth 14 seldepth 19 multipv 1 score cp -30 nodes 48777 nps 641802 hashfull 14 tbhits 0 time 76 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4 g8f6 d4c6 b7c6 f1d3 d7d5 e4d5 d8e7 d3e2 c6d5 e1g1"
        )
        self._respond(
            "info depth 15 seldepth 24 multipv 1 score cp -35 nodes 93272 nps 728687 hashfull 30 tbhits 0 time 128 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4 f8c5 d4c6 b7c6 b1c3 g8f6 c3a4 c5d6 f1d3 e8g8 e1g1 f8e8"
        )
        self._respond(
            "info depth 16 seldepth 22 multipv 1 score cp -33 nodes 99791 nps 739192 hashfull 35 tbhits 0 time 135 pv e7e5 g1f3 b8c6 f1c4 d7d6 e1g1 f8e7 d2d4 e5d4 f3d4 g8f6 d4c6 b7c6 b1c3 e8g8 c4d3"
        )
        self._respond(
            "info depth 17 seldepth 26 multipv 1 score cp -36 nodes 166478 nps 808145 hashfull 53 tbhits 0 time 206 pv e7e5 g1f3 b8c6 f1b5 a7a6 b5a4 f8e7 e1g1 g8f6"
        )
        self._respond(
            "info depth 18 seldepth 28 multipv 1 score cp -36 nodes 236227 nps 837684 hashfull 75 tbhits 0 time 282 pv e7e5 g1f3 b8c6 f1b5 a7a6 b5a4 g8f6 e1g1 f6e4 d2d4 b7b5 a4b3 d7d5 d4e5 c8e6 b1d2 e4c5 c2c3 d5d4 b3e6 c5e6 f3d4 c6d4 c3d4 d8d4"
        )
        self._respond(
            "info depth 19 seldepth 30 multipv 1 score cp -39 nodes 329264 nps 855231 hashfull 114 tbhits 0 time 385 pv e7e5 g1f3 b8c6 f1b5 a7a6 b5a4 g8f6 e1g1 f6e4 d2d4 b7b5 a4b3 d7d5 d4e5 c8e6 b1d2 e4c5 c2c3 c5b3 d2b3 f8e7 f3d4 c6d4 c3d4 e8g8 f2f4 a6a5"
        )
        self._respond(
            "info depth 20 seldepth 33 multipv 1 score cp -40 nodes 452720 nps 873976 hashfull 169 tbhits 0 time 518 pv c7c5 g1f3 d7d6 b1c3 e7e5 f1c4 f8e7 d2d3 g8f6 a2a4 e8g8 h2h3 b8c6"
        )
        self._respond(
            "info depth 21 seldepth 33 multipv 1 score cp -39 nodes 597818 nps 890935 hashfull 228 tbhits 0 time 671 pv e7e5 g1f3 d7d6 d2d4 e5d4 f3d4 g8f6 f1d3 f8e7 e1g1 e8g8 c2c4 b8c6 d3c2 c6d4 d1d4 f6d7 b1c3 e7f6"
        )
        self._respond(
            "info depth 22 seldepth 33 multipv 1 score cp -40 nodes 771145 nps 890467 hashfull 298 tbhits 0 time 866 pv e7e5 g1f3 b8c6 f1b5 a7a6 b5a4 g8f6 e1g1 b7b5 a4b3 f6e4 d2d4 d7d5 d4e5 c8e6 b1d2 e4c5 c2c3 c5b3 d2b3 f8e7 a2a4 b5a4 b3d4 d8d7 d4e6 f7e6"
        )
        self._respond(
            "info depth 23 seldepth 37 multipv 1 score cp -41 nodes 900899 nps 899100 hashfull 342 tbhits 0 time 1002 pv e7e5 g1f3 b8c6 f1b5 a7a6 b5a4 g8f6 e1g1 b7b5 a4b3 f6e4 d2d4 d7d5 d4e5 c8e6 c2c3 f8e7 b1d2 e4c5 b3c2 e6g4 h2h3 g4h5 g2g4 h5g6"
        )
        self._respond(
            "info depth 24 seldepth 34 multipv 1 score cp -41 nodes 915189 nps 901664 hashfull 345 tbhits 0 time 1015 pv e7e5 g1f3 b8c6 f1b5 a7a6 b5a4 g8f6 e1g1 b7b5 a4b3 f6e4 d2d4 d7d5 d4e5 c8e6 c2c3 f8e7 b1d2 e4c5 b3c2 e6g4 h2h3 g4h5 g2g4 h5g6 d2b3 g6c2"
        )
        self._respond(
            "info depth 25 seldepth 39 multipv 1 score cp -40 nodes 1081503 nps 899752 hashfull 404 tbhits 0 time 1202 pv e7e5 g1f3 b8c6 f1b5 a7a6 b5a4 g8f6 e1g1 f6e4 d2d4 b7b5 a4b3 d7d5 d4e5 c8e6 c2c3 f8c5 b1d2 e8g8 b3c2 f7f5 e5f6 e4f6 a2a4 h7h6 h2h3 c5d6 a4b5 a6b5 a1a8 d8a8"
        )
        self._respond(
            "info depth 26 seldepth 38 multipv 1 score cp -33 nodes 1467519 nps 906995 hashfull 514 tbhits 0 time 1618 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4 f8c5 d4b3 c5b6 a2a4 d8h4 d1f3 a7a5 g2g3 h4f6 f3e2 g8e7 b1c3"
        )
        self._respond(
            "info depth 27 seldepth 36 multipv 1 score cp -32 nodes 2344465 nps 891770 hashfull 736 tbhits 0 time 2629 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4 f8b4 c2c3 b4c5 d4c6 b7c6 f1d3 g8e7 e1g1 e7g6 b1d2 d7d6 d2b3 c5b6 b3d4 g6e5 d3e2 e8g8"
        )
        self._respond(
            "info depth 28 seldepth 42 multipv 1 score cp -30 nodes 2833721 nps 878945 hashfull 820 tbhits 0 time 3224 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4 f8c5 d4b3 c5b6 d1e2 c6d4 b3d4 b6d4 c2c3 d4b6 a2a4 a7a6 a4a5 b6a7 c1e3 a7e3 e2e3 g8f6 f1d3 f6g4 e3d4"
        )
        self._respond(
            "info depth 29 seldepth 35 multipv 1 score cp -27 nodes 3424376 nps 863868 hashfull 888 tbhits 0 time 3964 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4 f8c5 d4b3 c5b6 d1e2 d7d6 c1e3 d8h4 b1c3 c8g4 e2d2 b6e3 d2e3 e8c8 h2h3 g4e6 e1c1 c8b8 g2g3 h4h6 e3h6 g8h6 f1g2 h8e8"
        )
        self._respond(
            "info depth 30 seldepth 39 multipv 1 score cp -29 nodes 3761084 nps 856348 hashfull 920 tbhits 0 time 4392 pv e7e5 g1f3 b8c6 d2d4 e5d4 f3d4 f8c5 d4b3 c5b6 d1e2 d7d6 c1e3 d8h4 b1c3 c8g4 e2d2 b6e3 d2e3 e8c8 h2h3 g4d7 e1c1 g8e7 g2g3 h4f6 f2f4 c8b8 f1g2 a7a6 d1d3 h8e8 h1d1"
        )
        self._respond(
            "info depth 31 seldepth 48 multipv 1 score cp -29 nodes 6011633 nps 860648 hashfull 986 tbhits 0 time 6985 pv e7e5 g1f3 b8c6 f1b5 g8f6 e1g1 f6e4 f1e1 e4d6 f3e5 f8e7 b5f1 c6e5 e1e5 e8g8 d2d4 e7f6 e5e1 d6f5 c2c3 d7d5 a2a4 c7c6 c1f4 f6e7 b1d2 e7d6 f4e5 a7a5 f1d3 g7g6"
        )
        self._respond(
            "info depth 32 seldepth 41 multipv 1 score cp -27 nodes 6212887 nps 863260 hashfull 987 tbhits 0 time 7197 pv e7e5 g1f3 b8c6 f1b5 g8f6 e1g1 f6e4 f1e1 e4d6 f3e5 f8e7 b5f1 c6e5 e1e5 e8g8 d2d4 e7f6 e5e1 d6f5 c2c3 d7d5 f1d3 c7c6 a2a4 g7g6 b1d2 f5g7 a4a5 f8e8 e1e8 d8e8 d2f3 c8g4"
        )
        self._respond(
            "info depth 33 seldepth 43 multipv 1 score cp -28 nodes 6454316 nps 865305 hashfull 990 tbhits 0 time 7459 pv e7e5 g1f3 b8c6 f1b5 g8f6 e1g1 f6e4 f1e1 e4d6 f3e5 f8e7 b5f1 c6e5 e1e5 e8g8 d2d4 e7f6 e5e1 d6f5 d4d5 f8e8 e1e8 d8e8 d1d3 d7d6 b1d2 c8d7 d2f3 a7a5 c1d2 b7b6 a1e1 e8d8 a2a3"
        )
        self._respond(
            "info depth 34 seldepth 49 multipv 1 score cp -30 nodes 7828439 nps 869247 hashfull 996 tbhits 0 time 9006 pv e7e5 g1f3 b8c6 f1b5 g8f6 e1g1 f6e4 f1e1 e4d6 f3e5 c6e5 e1e5 f8e7 b5f1 e8g8 d2d4 e7f6 e5e1 f8e8 c1f4 e8e1 d1e1 d6e8 c2c3 d7d5 b1d2 c8f5 d2b3 b7b6 e1e3 e8d6 b3d2"
        )

    def run(self):
        while True:
            try:
                line = input()
            except EOFError:
                break

            self.log("in", line)

            if line == "uci":
                self._respond("id name MyBot")
                self._respond("id author Me")
                self._respond("uciok")

            elif line == "isready":
                self._respond("readyok")

            elif line.startswith("position"):
                self.set_position(line)

            elif line.startswith("go"):
                [move_uci, ponder_move_uci] = self.select_move()
                # self.mockResponse()
                # self._respond("bestmove e7e5 ponder g1f3")
                self._respond(
                    f"info depth 5 seldepth 7 multipv 1 score cp -7 nodes 765 nps 109285 hashfull 0 tbhits 0 time 7 pv {move_uci}"
                )
                self._respond(f"bestmove {move_uci} ponder {ponder_move_uci}")

            elif line == "quit":
                break

    def set_position(self, line):
        tokens = line.split()

        if "startpos" in tokens:
            self.board.reset()
            moves_index = tokens.index("moves") + 1 if "moves" in tokens else None
            if moves_index:
                moves = tokens[moves_index:]
                for move in moves:
                    self.board.push_uci(move)
        elif "fen" in tokens:
            self.board.reset()
            moves_index = tokens.index("moves") + 1 if "moves" in tokens else None
            if moves_index:
                moves = tokens[moves_index:]
                for move in moves:
                    self.board.push_uci(move)

    def select_move(self):
        legal_moves = list(self.board.legal_moves)
        if not legal_moves:
            return "0000", None  # No legal move

        # Pick a "best" move — currently random
        move = random.choice(legal_moves)
        move_uci = move.uci()

        # Apply the move temporarily
        self.board.push(move)

        # Predict opponent's reply — also randomly for now
        opponent_moves = list(self.board.legal_moves)
        ponder_move_uci = None
        if opponent_moves:
            ponder = random.choice(opponent_moves)
            ponder_move_uci = ponder.uci()

        # Undo the temporary move
        self.board.pop()

        return move_uci, ponder_move_uci
