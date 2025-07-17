<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useChess } from "../composables/useChess";
// import { useEngine } from "../composables/useEngine";
import { useChessground } from "../composables/useChessground";
import { useCustomEngine } from "../composables/useCustomEngine";

const boardRef = ref<HTMLDivElement | null>(null);
const { chess, getTurn, movePiece } = useChess();
// const { initEngine, onBestMove, updateEnginePosition } = useEngine();
const { initEngine, onBestMove, updateEnginePosition } = useCustomEngine();

const { initChessground, start, updateBoard } = useChessground();

onMounted(async () => {
  initEngine().then(() => {
    start();
  });

  const onMove = (from: string, to: string) => {
    movePiece(from, to);
    updateBoard(chess);
    updateEnginePosition(chess.fen(), getTurn());
  };

  onBestMove((from, to) => {
    onMove(from, to);
  });

  if (boardRef.value) {
    initChessground(boardRef.value, chess, onMove);
  }
});
</script>
<template>
  <div ref="boardRef" class="chessground" id="chess-1"></div>
</template>

<style scoped>
.chessground {
  width: 85vmin;
  height: 85vmin;
  box-sizing: border-box;
}

/* .chessground {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
} */
</style>
