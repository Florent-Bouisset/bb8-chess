import random
import time
import chess
from typing import List, Optional
from typing import Tuple
from ..logger import log


def select_best_move(
    board: chess.Board, evaluate_position, depth: int = 3
) -> Tuple[float, List]:
    """
    Checks all legal moves, applies them to a copy of the board,
    evaluates resulting positions using the provided evaluation function,
    and returns the move with the highest evaluation score.
    If multiple moves have the same evaluation, one is selected randomly.

    If no legal moves, returns None.
    """

    global nodes_searched
    nodes_searched = 0  # Reset before search
    start_time = time.time()
    best_score = float("-inf")
    best_lines = []

    for move in board.legal_moves:
        board.push(move)  # Make the move on the board
        # Evaluate new position from current player (i.e opponent turn), so negate it
        score, line = evaluate_with_depth(board, depth - 1, evaluate_position)
        score = -score
        board.pop()  # Undo move
        full_line = [move] + line
        log("DEBUG", f"line: {board.variation_san([move] + line)}, eval: {score}")

        if score > best_score:
            best_score = score
            best_lines = [full_line]

        elif score == best_score:
            best_lines.append(full_line)

    best_line = random.choice(best_lines) if best_lines else []
    best_move = best_line[0] if best_line else None

    end_time = time.time()
    elapsed = end_time - start_time
    log(
        "INFO",
        f"Positions evaluated : {nodes_searched}, Time Elapsed : {elapsed:.2f} seconds, Positions par seconde (NPS) : {nodes_searched / elapsed:.2f}",
    )
    return best_move, best_score


def evaluate_with_depth(
    board: chess.Board, depth: int, evaluate_position
) -> Tuple[float, List[chess.Move]]:
    global nodes_searched
    nodes_searched += 1

    if depth == 0 or board.is_game_over():
        return evaluate_position(board), []

    best_score = float("-inf")
    best_line: List[chess.Move] = []

    for move in board.legal_moves:
        board.push(move)
        score, line = evaluate_with_depth(board, depth - 1, evaluate_position)
        # Négation du score parce qu'on change de joueur
        score = -score
        board.pop()

        if score > best_score:
            best_score = score
            best_line = [move] + line

    return best_score, best_line
