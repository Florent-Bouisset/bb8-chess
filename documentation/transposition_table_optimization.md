# Transposition table


A **transposition table** stores the results of previously evaluated positions, allowing the engine to skip redundant calculations when the same position arises via a different move sequence.

Below is a benchmark comparing performance **with and without** a transposition table, using the position:

FEN: r1bqk1nr/pppp1ppp/2n5/2b5/3NP3/4B3/PPP2PPP/RN1QKB1R b KQkq - 0 1
Depth: 4


---

## 🔁 Without Transposition Table

- **Positions evaluated**: 2,140,636  
- **Time elapsed**: 36.88 seconds  
- **Nodes per second (NPS)**: 58,044

---

## ✅ With Transposition Table

- **Positions evaluated**: 1,237,893  
- **Time elapsed**: 21.30 seconds  
- **Nodes per second (NPS)**: 58,107

---

### 🚀 Result

Using a transposition table reduced the number of evaluated positions by **over 40%**, with **no loss in nodes-per-second performance**. This leads to a more efficient and deeper search — crucial for competitive engine strength.

