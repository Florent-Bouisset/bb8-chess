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

  function getTurn(): "white" | "black" {
    return chess.turn() === "w" ? "white" : "black";
  }

  function movePiece(from: string, to: string) {
    try {
      chess.move({ from, to });
    } catch (e) {
      throw new Error("ILLEGAL");
    }
  }

  return { chess, generateDests, getTurn, movePiece };
}
