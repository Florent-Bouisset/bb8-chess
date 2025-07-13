<script setup lang="ts">
import { Chessground } from "@lichess-org/chessground";
import type { Api } from "@lichess-org/chessground/api";
import { Chess, type Square } from "chess.js";

import { onMounted, ref } from "vue";

const engine = new Worker("/stockfish.js-10.0.2/stockfish.js");

const chessBoard = ref();
let config;
let ground: Api;

// Initialize chess.js game state
const chess = new Chess();
// Listen to messages from the engine
engine.onmessage = (e) => {
  const move = e.data.match(/^bestmove\s([a-h][1-8])([a-h][1-8])/);
  if (move) {
    ground.move(move[1], move[2]);
    updateConfig(move[1], move[2], {});
  }
  ground.set({ turnColor: getTurn() });
};

engine.onerror = function (event) {
  console.error("Stockfish error:", event);
};
engine.onmessageerror = function (event) {
  console.log("Stockfish on messageerorr", event);
};

engine.postMessage("uci");
engine.postMessage("isready");
engine.postMessage("ucinewgame");

// engine.postMessage('position startpos moves e2e4 e7e5') // set board position
// engine.postMessage('go depth 15') // ask it to calculate

function generateDests() {
  const moves = chess.moves({ verbose: true });
  const dests: Map<Square, Square[]> = new Map();
  moves.forEach((m) => {
    if (!dests.has(m.from)) {
      dests.set(m.from, []);
    }
    dests.get(m.from)!.push(m.to);
  });

  return dests;
}

function getTurn(): "white" | "black" {
  return chess.turn() === "w" ? "white" : "black";
}

const dests = generateDests();

const playerColor = "white";

function updateConfig(from: string, to: string, _meta: {}) {
  chess.move({ from, to });

  ground.set({
    check: chess.inCheck(),
    turnColor: getTurn(),
    movable: { dests: generateDests() },
  });

  const fen = chess.fen();
  engine.postMessage(`position fen ${fen}`);
  if (getTurn() !== playerColor) {
    engine.postMessage("go");
  }
}

config = {
  fen: chess.fen(),
  trustAllEvents: false,
  highlight: {
    lastMove: true, // add last-move class to squares
    check: true,
  },
  turnColor: getTurn(),
  movable: {
    free: false,
    dests: dests,
    color: "both",
    // color: playerColor,
    events: {
      after: (from: string, to: string, meta: {}) =>
        updateConfig(from, to, meta),
      // afterNewPiece: (args) => console.log("After newpiece!", args),
    },
  },

  premovable: {
    enabled: true, // allow premoves for color that can not move
    showDests: true, // whether to add the premove-dest class on squares
    castle: true, // whether to allow king castle premoves
    // dests?: cg.Key[]; // premove destinations for the current selection
    // customDests?: cg.Dests; // use custom valid premoves. {"a2" ["a3" "a4"] "b1" ["a3" "c3"]}
    events: {
      // set: (args) => undefined, // called after the premove has been set
      // unset: (arg) => undefined, // called after the premove has been unset
    },
  },

  draggable: {
    enabled: true, // allow moves & premoves to use drag'n drop
    deleteOnDropOff: false, // delete a piece when it is dropped off the board
  },
  // events: {
  //   change: (arg) => console.log("change event"),
  //   // called after a piece has been moved.
  //   // capturedPiece is undefined or like {color: 'white'; 'role': 'queen'}
  //   move: (arg) => console.log("move event"),
  //   dropNewPiece: (arg) => console.log("dorp new piece event"),
  //   select: (arg1, arg2) => undefined,
  //   insert: (arg) => undefined,
  // },
};

onMounted(() => {
  // Generate legal moves object for chessground config

  if (chessBoard.value) {
    ground = Chessground(document.getElementById("chess-1")!, config);
  } else {
    console.error("No chess element defined...");
  }
});
</script>

<template>
  <div>
    <h1>Chess demo</h1>
    <div ref="chessBoard" class="chessground" id="chess-1"></div>
  </div>
</template>

<style>
body {
  display: flex;
  flex-wrap: wrap;
}

body > div {
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
