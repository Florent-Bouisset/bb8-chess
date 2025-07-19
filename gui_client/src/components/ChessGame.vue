<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useChess } from "../composables/useChess";
// import { useEngine } from "../composables/useEngine";
import { useChessground } from "../composables/useChessground";
import { useCustomEngine } from "../composables/useCustomEngine";
import { h, render } from "vue";
import PromotionPopup from "./PromotionPopup.vue";

const boardRef = ref<HTMLDivElement | null>(null);
const { chess, getTurn, movePiece, shouldMoveBeAPromote } = useChess();
// const { initEngine, onBestMove, updateEnginePosition } = useEngine();
const { initEngine, onBestMove, updateEnginePosition } = useCustomEngine();

const { initChessground, start, updateBoard } = useChessground();

const askUserPromotion = async (): Promise<string> => {
  return new Promise((resolve) => {
    const container = document.createElement("div");
    document.body.appendChild(container);

    const vnode = h(PromotionPopup, {
      onSelected: (piece: string) => {
        render(null, container); // unmount
        container.remove();
        resolve(piece);
      },
    });
    render(vnode, container);
  });
};

onMounted(async () => {
  initEngine().then(() => {
    start();
  });

  const onMove = async (
    from: string,
    to: string,
    promotion: string | undefined
  ) => {
    const shouldAskPromote = !promotion && shouldMoveBeAPromote(from, to);
    if (shouldAskPromote) {
      askUserPromotion().then((askedPromoted) => {
        movePiece(from, to, askedPromoted);
        updateBoard(chess);
        updateEnginePosition(chess.fen(), getTurn());
      });
    } else {
      movePiece(from, to, promotion);
      updateBoard(chess);
      updateEnginePosition(chess.fen(), getTurn());
    }
  };

  onBestMove((from, to, promotion) => {
    onMove(from, to, promotion);
  });

  if (boardRef.value) {
    initChessground(boardRef.value, chess, onMove);
  }
});
</script>
<template>
  <div ref="boardRef" class="chessground" id="chess-1"></div>
  <!-- <div id="promotion" class="promotion-popup cg-wrap">
    <piece class="white queen" style="transform: translate(0, 0px)"></piece>
    <piece class="white rook" style="transform: translate(0, 0px)"></piece>
    <piece class="white bishop" style="transform: translate(0, 0px)"></piece>
    <piece class="white knight" style="transform: translate(0, 0px)"></piece>
  </div> -->
</template>

<style scoped>
.chessground {
  width: 85vmin;
  height: 85vmin;
  box-sizing: border-box;
}

.promotion-popup {
  position: absolute;
  display: flex;
  background: #bfcfdd;
  border: 1px solid black;
  z-index: 10;
  display: flex;
  top: 100px;
  left: 100px;
  width: 320px;
  height: auto;
}
.promotion-piece {
  padding: 5px;
  cursor: pointer;
}

piece {
  width: 80px;
  height: 80px;
  position: static;
}

/* .chessground {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
} */
</style>
