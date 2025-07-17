export function useEngine() {
  const engine = new Worker("/stockfish.js-10.0.2/stockfish.js");

  function initEngine() {
    engine.postMessage("uci");
    engine.postMessage("isready");
    engine.postMessage("ucinewgame");
  }

  function onBestMove(callback: (from: string, to: string) => void) {
    engine.onmessage = (e) => {
      const move = e.data.match(/^bestmove\s([a-h][1-8])([a-h][1-8])/);
      if (move) {
        callback(move[1], move[2]);
      }
    };
  }

  function updateEnginePosition(fen: string, turn: string) {
    engine.postMessage(`position fen ${fen}`);
    if (turn !== "white") {
      engine.postMessage("go");
    }
  }

  return { engine, initEngine, onBestMove, updateEnginePosition };
}
