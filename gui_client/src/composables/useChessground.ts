import { Chessground } from "@lichess-org/chessground";
import type { Api } from "@lichess-org/chessground/api";
import type { Chess } from "chess.js";
import { useChess } from "./useChess";
import type { Key } from "@lichess-org/chessground/types";

export function useChessground() {
  let ground: Api;

  const { generateDests, getTurn } = useChess();

  function initChessground(
    el: HTMLElement,
    chess: Chess,
    moveHandler: (from: string, to: string) => void
  ) {
    ground = Chessground(el, {
      fen: chess.fen(),
      turnColor: getTurn(),
      movable: {
        free: false,
        color: "both",
        dests: new Map(),
        events: {
          after: (from, to) => {
            moveHandler(from, to);
          },
        },
      },
      highlight: { lastMove: true, check: true },
      draggable: { enabled: true },
    });
  }

  function start() {
    ground.set({
      movable: {
        dests: generateDests(),
      },
    });
  }
  function updateBoard(chess: Chess) {
    ground.set({
      fen: chess.fen(),
      check: chess.inCheck(),
      turnColor: getTurn(),
      movable: {
        dests: generateDests(),
      },
    });
  }

  function moveOnBoard(from: Key, to: Key) {
    ground.move(from, to); // update UI
  }

  return { initChessground, start, updateBoard, moveOnBoard };
}
