import { Chess, type Square } from "chess.js";

const chess = new Chess();

export function useChess() {
  function generateDests() {
    const moves = chess.moves({ verbose: true });
    const dests = new Map<Square, Square[]>();
    moves.forEach((m) => {
      if (!dests.has(m.from)) dests.set(m.from, []);
      dests.get(m.from)!.push(m.to);
    });
    return dests;
  }

  function shouldMoveBeAPromote(from: string, to: string): boolean {
    const moves = chess.moves({ verbose: true });
    const actualMove = moves.find((m) => m.from === from && m.to === to);
    if (actualMove === undefined) {
      throw new Error("Impossible Move");
    }
    return actualMove.isPromotion();
  }

  function getTurn(): "white" | "black" {
    return chess.turn() === "w" ? "white" : "black";
  }

  function movePiece(from: string, to: string, promotion: string | undefined) {
    try {
      chess.move({ from, to, promotion });
    } catch (e) {
      throw new Error("ILLEGAL");
    }
  }

  function getLastMove(): [from: Square, to: Square] | undefined {
    const lastMove = chess.history({ verbose: true }).at(-1);
    if (lastMove) {
      return [lastMove.from, lastMove.to];
    }
    return undefined;
  }
  return {
    chess,
    generateDests,
    shouldMoveBeAPromote,
    getLastMove,
    getTurn,
    movePiece,
  };
}
