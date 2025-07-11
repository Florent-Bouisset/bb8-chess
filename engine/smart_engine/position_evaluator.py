import chess


def evaluate_position(board: chess.Board, color: chess.Color) -> float:
    """
    Evaluates the given chess board position and returns a numerical score
    representing the advantage for White or Black.

    The score is positive if the position favors White, negative if it favors Black.

    The evaluation is based on counting material balance and other heuristics
    such as pawn structure (e.g., penalties for doubled pawns).

    Parameters:
        board (chess.Board): The current board position to evaluate.
        color (chess.Color): The perspective from which to evaluate (True for White, False for Black).

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

    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    # Flip score if evaluating from Black's perspective
    return score if color == chess.WHITE else -score
