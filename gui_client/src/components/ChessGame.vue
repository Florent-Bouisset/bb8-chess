<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useChess } from "../composables/useChess";
import { useEngine } from "../composables/useEngine";
import { useChessground } from "../composables/useChessground";
import type { Key } from "@lichess-org/chessground/types";

const boardRef = ref<HTMLDivElement | null>(null);
const { chess, generateDests, getTurn, movePiece } = useChess();
const { engine, initEngine, onBestMove, updateEnginePosition } =
  useEngine(chess);
const { initChessground, moveOnBoard, updateBoard } = useChessground();

onMounted(() => {
  initEngine();

  const onHumanMove = (from: string, to: string) => {
    movePiece(from, to);
    updateBoard(chess);
    updateEnginePosition(chess.fen(), getTurn());
  };

  onBestMove((from, to) => {
    onHumanMove(from, to);
    // moveOnBoard(from as Key, to as Key); // update UI ✅
    // updateEnginePosition(chess.fen(), getTurn()); // possibly queue next move
  });

  if (boardRef.value) {
    initChessground(boardRef.value, chess, onHumanMove);
  }
});
</script>

<template>
  <div>
    <h1>Play against chess engine</h1>
    <div ref="boardRef" class="chessground" id="chess-1"></div>
  </div>
</template>

<style>
body {
  display: flex;
  flex-wrap: wrap;
  margin: 10px;
}

.chessground {
  width: 500px;
  height: 500px;
}

cg-board {
  background-color: #bfcfdd;
}
</style>
