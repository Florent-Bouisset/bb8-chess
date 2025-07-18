importScripts("https://cdn.jsdelivr.net/pyodide/v0.23.4/full/pyodide.js");

let pyodide = null;
let engine = null;
let initialized = false;
let engineOnMessage = null;

const worker = self;

async function loadPyodideAndPackages() {
  pyodide = await loadPyodide();
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  await micropip.install("chess");
  console.log("Pyodide loaded in worker");

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
  try {
    pyodide.globals.set("jsoutput", (output) => {
      self.postMessage(output);
    });
    await pyodide.runPythonAsync(`
        import sys
        sys.path.append("/")
        from engine.main import get_engine

        engine = get_engine()
        engine._respond = jsoutput
    `);

    engine = pyodide.globals.get("engine");
  } catch (err) {
    console.error("Worker error:", err);
  }
}

loadPyodideAndPackages().then(() => {
  initialized = true;
});

self.onmessage = async (event) => {
  if (!initialized) {
    console.log("Too early, engine not initialized.");
    return;
  }

  console.log("[Worker][IN]:", event.data);
  try {
    engine.handle_command(event.data);
  } catch (err) {
    console.error("Worker error:", err);
  }
};
