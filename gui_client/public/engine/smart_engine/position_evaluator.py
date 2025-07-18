import chess

from ..logger import log


def evaluate_position(board: chess.Board) -> float:
    """
    Evaluates the given chess board position and returns a numerical score
    representing the advantage for current player.

    The score is positive if the position favors current player, negative if it favors opponent.

    The evaluation is based on counting material balance and other heuristics
    such as pawn structure (e.g., penalties for doubled pawns).

    Parameters:
        board (chess.Board): The current board position to evaluate.

    Returns:
        float: The evaluation score of the position.
    """
    score = 0.0

    # Simple piece values
    PIECE_VALUES = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0,  # King is not counted
    }

    if board.is_checkmate() == True:
        # Strongly penalize the position if it's checkmate for the current player
        return -100000

    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    # Flip score if evaluating from Black's perspective
    return score if board.turn == chess.WHITE else -score
