import random
import chess
from typing import Optional
from typing import Tuple
from engine.logger import log


def select_best_move(
    board: chess.Board, evaluate_position
) -> Tuple[Optional[chess.Move], float]:
    """
    Checks all legal moves, applies them to a copy of the board,
    evaluates resulting positions using the provided evaluation function,
    and returns the move with the highest evaluation score.
    If multiple moves have the same evaluation, one is selected randomly.

    If no legal moves, returns None.
    """
    best_score = float("-inf")
    best_moves = []

    # Determine who's turn it is
    current_color = board.turn

    for move in board.legal_moves:
        board.push(move)  # Make the move on the board
        score = evaluate_position(board, current_color)  # Evaluate new position
        board.pop()  # Undo move

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

    # logger.info("Evaluating position...")
    # logger.warning("No legal moves available.")

    return [random.choice(best_moves) if best_moves else None, best_score]
