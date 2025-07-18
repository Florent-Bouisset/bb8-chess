export function useCustomEngine() {
  const engine = new Worker("pyodide-worker.js");
  const messageListeners: Array<(msg: MessageEvent) => void> = [];

  engine.onmessage = (event) => {
    for (const listener of messageListeners) {
      listener(event);
    }
  };
  function addWorkerListener(fn: (msg: MessageEvent) => void) {
    messageListeners.push(fn);
  }

  addWorkerListener((event) => {
    console.log("[Worker][OUT]:", event.data);
  });
  window.myworker = engine;

  function initEngine() {
    return new Promise((resolve, reject) => {
      let isReadyInterval: number | null = null;
      addWorkerListener((event) => {
        if (event.data === "readyok") {
          if (isReadyInterval !== null) {
            clearInterval(isReadyInterval);
          }
          resolve("readyok");
        }
      });
      isReadyInterval = setInterval(() => {
        engine.postMessage("isready");
      }, 2000);
      setTimeout(() => {
        clearInterval(isReadyInterval);
        reject("timed out");
      }, 30000);
    });
  }

  function onBestMove(callback: (from: string, to: string) => void) {
    addWorkerListener((event) => {
      const move = event.data.match(/^bestmove\s([a-h][1-8])([a-h][1-8])/);
      if (move) {
        callback(move[1], move[2]);
      }
    });
  }

  // Update engine position and maybe start search
  async function updateEnginePosition(fen: string, turn: string) {
    engine.postMessage(`position fen ${fen}`);
    if (turn !== "white") {
      engine.postMessage("go");
    }
  }

  return { initEngine, onBestMove, updateEnginePosition };
}
