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

  function onBestMove(
    callback: (from: string, to: string, promotion: string | undefined) => void
  ) {
    addWorkerListener((event) => {
      const move = event.data.match(
        /^bestmove\s([a-h][1-8])([a-h][1-8])([qrbn])?/
      );
      if (move) {
        const from = move[1];
        const to = move[2];
        const promotion = move[3]; // could be undefined

        callback(from, to, promotion);
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
