from typing import Dict


class TTEntry:
    def __init__(self, score, depth, best_line):
        self.score = score
        self.depth = depth
        self.best_line = best_line


class TranspositionTable:
    def __init__(self):
        self.table: Dict[str, TTEntry] = {}

    def store(self, key, score, depth, best_line):
        entry = self.table.get(key)

        # replace only if depth is higher than existing
        if entry is None or depth >= entry.depth:
            self.table[key] = TTEntry(score, depth, best_line)

    def lookup(self, key, depth: int):
        entry = self.table.get(key)
        if entry and entry.depth >= depth:
            return [entry.score, entry.best_line]
        return None
