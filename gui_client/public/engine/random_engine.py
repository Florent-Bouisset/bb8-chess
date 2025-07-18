import chess
import random
from .base_engine import BaseEngine
from .logger import log


class RandomEngine(BaseEngine):
    def __init__(self, debug=True, log_path=None):
        super().__init__(debug, log_path)
        self.board = chess.Board()

    def run(self):
        while True:
            try:
                line = input()
            except EOFError:
                break

            log("in", line)

            if line == "uci":
                self._respond("id name BB-8 - randomEngine")
                self._respond("id author Florent Bouisset")
                self._respond("uciok")

            elif line == "isready":
                self._respond("readyok")

            elif line.startswith("position"):
                self.set_position(line)

            elif line.startswith("go"):
                [move_uci, ponder_move_uci] = self.select_move()
                # TO DO: the compute time, depth and so on are just hardcode value
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
