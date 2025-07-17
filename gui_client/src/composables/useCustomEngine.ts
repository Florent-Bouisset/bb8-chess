import { type PyodideInterface } from "pyodide";
declare function loadPyodide(options?: {
  indexURL?: string;
}): Promise<PyodideInterface>;

export function useCustomEngine() {
  //   let pyodide: PyodideInterface | null = null;

  let engineOnMessage: ((arg: string) => void) | null = null;

  let engine = null as any;

  let pyodideInstance = null;

  // Initialize pyodide and load your engine files (simplified)
  async function initEngine() {
    console.log("init pyodide....");
    let pyodide = await loadPyodide();
    pyodideInstance = pyodide;
    await pyodide.loadPackage("micropip");
    const micropip = pyodide.pyimport("micropip");
    await micropip.install("chess");

    pyodide.FS.mkdir("/engine");
    pyodide.FS.mkdir("/engine/smart_engine");

    // Step 2: Load each Python file manually into Pyodide's filesystem
    const files = [
      "__init__.py",
      "logger.py",
      "base_engine.py",
      "random_engine.py",
      "smart_engine/position_evaluator.py",
      "smart_engine/__init__.py",
      "smart_engine/engine.py",
      "smart_engine/move_selector.py",
      "main.py",
    ];

    for (const file of files) {
      const response = await fetch(`/engine/${file}`);
      const code = await response.text();
      pyodide.FS.writeFile(`/engine/${file}`, code);
    }

    pyodide.globals.set("jsoutput", (output) => {
      console.info("[ENGINE OUT]", output);
      if (engineOnMessage) {
        engineOnMessage(output);
      }
    });

    await pyodide.runPythonAsync(`
        import sys
        sys.path.append("/")
        from engine.main import get_engine

        engine = get_engine()
        engine._respond = jsoutput
    `);

    engine = pyodide.globals.get("engine"); // instance

    window.engine = engine;
    engine.handle_command("uci");
    engine.handle_command("isready");
  }

  function onBestMove(callback: (from: string, to: string) => void) {
    engineOnMessage = (message: string) => {
      const move = message.match(/^bestmove\s([a-h][1-8])([a-h][1-8])/);
      if (move) {
        callback(move[1], move[2]);
      }
    };
  }

  // Update engine position and maybe start search
  async function updateEnginePosition(fen: string, turn: string) {
    console.info(`position fen ${fen}`);
    engine.handle_command(`position fen ${fen}`);
    if (turn !== "white") {
      console.info(`go`);

      engine.handle_command("go");
    }
  }

  return { initEngine, postMessage, onBestMove, updateEnginePosition };
}
